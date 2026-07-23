from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .catalog import find_source, load_course_map
from .engine import build_reentry_message, evaluate_message
from .progress import record_progress
from .state import LearnerState, example_state


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-tutor-bot",
        description="Preview and evaluate source-grounded learning re-entry prompts.",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    init_command = commands.add_parser("init", help="Create a private learner state")
    init_command.add_argument("--output", default="learner-state.json")
    init_command.add_argument("--force", action="store_true")

    next_command = commands.add_parser("next", help="Build the next re-entry message")
    next_command.add_argument("--state", required=True)
    next_command.add_argument("--json", action="store_true")

    eval_command = commands.add_parser("eval", help="Evaluate a re-entry message")
    eval_command.add_argument("--state", required=True)
    eval_command.add_argument("--message-file")

    sources_command = commands.add_parser(
        "sources",
        help="List curated primary sources",
    )
    sources_command.add_argument(
        "--track",
        choices=["llm-systems", "agent-loops", "evaluation"],
    )

    record_command = commands.add_parser(
        "record",
        help="Record one artifact and next loop",
    )
    record_command.add_argument("--state", required=True)
    record_command.add_argument("--artifact", required=True)
    record_command.add_argument("--reflection", default="")
    record_command.add_argument("--next-open-loop", required=True)
    record_command.add_argument("--next-artifact", required=True)
    record_command.add_argument("--next-check", required=True)

    return parser


def _state_and_source(path: str):
    state = LearnerState.load(path)
    sources = load_course_map()
    source = find_source(state.current_source_id, sources)
    if source.track != state.current_track:
        raise ValueError(
            f"Source {source.id!r} belongs to {source.track!r}, "
            f"not {state.current_track!r}"
        )
    return state, source


def _run(args: argparse.Namespace) -> int:
    if args.command == "init":
        destination = Path(args.output)
        if destination.exists() and not args.force:
            raise ValueError(
                f"{destination} already exists; use --force to replace it"
            )
        example_state().save(destination)
        print(f"Created {destination}")
        return 0

    if args.command == "next":
        state, source = _state_and_source(args.state)
        message = build_reentry_message(state, source)
        if args.json:
            print(
                json.dumps(
                    {
                        "message": message,
                        "source_id": source.id,
                        "source_url": source.url,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            print(message)
        return 0

    if args.command == "eval":
        state, source = _state_and_source(args.state)
        if args.message_file:
            message = Path(args.message_file).read_text(encoding="utf-8").strip()
        else:
            message = build_reentry_message(state, source)
        result = evaluate_message(message, state, source)
        print(
            json.dumps(
                {
                    "label": result.label,
                    "failures": result.failures,
                    "checks": result.checks,
                },
                indent=2,
            )
        )
        return 0 if result.label != "fail" else 1

    if args.command == "sources":
        sources = load_course_map()
        ordered_sources = sorted(
            sources,
            key=lambda item: (item.track, item.priority, item.title),
        )
        for source in ordered_sources:
            if args.track and source.track != args.track:
                continue
            print(f"[{source.track}] P{source.priority} {source.title}\n  {source.url}")
        return 0

    if args.command == "record":
        state = LearnerState.load(args.state)
        record_progress(
            state,
            artifact=args.artifact,
            reflection=args.reflection,
            next_open_loop=args.next_open_loop,
            next_artifact=args.next_artifact,
            next_check=args.next_check,
        )
        state.save(args.state)
        print(f"Updated {args.state}")
        return 0

    return 2


def main(argv: Sequence[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    try:
        return _run(args)
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(2, f"{parser.prog}: error: {error}\n")
