#!/usr/bin/env python3
"""Calculate a YouTube script word budget from a video brief.

This helper calculates a target word budget only. It does not generate the
script, titles, description, pinned comment, or production notes.

Supported input fields:
  video.target_minutes       (preferred nested brief schema)
  video.words_per_minute     (preferred; must be supplied)
  minutes                    (legacy flat-schema alias)
  words_per_minute           (legacy flat-schema alias)

Usage:
    python3 script_length.py --input video-brief.yaml --out ./out
    python3 script_length.py --input video-brief.yaml --out ./out --overwrite
"""

import argparse
import math
import os
import re
import sys


TITLE = "YouTube Video Script Writer — Word Budget"
FORMULA = "estimated word budget = target minutes * words per minute"


def read_brief(path):
    """Read the small YAML subset used by video-brief.yaml.

    This parser intentionally uses only Python's standard library and does
    not claim to be a general-purpose YAML parser. It supports indentation-
    based mapping keys and ignores list entries/comments.
    """
    data = {}
    parents = []
    try:
        with open(path, encoding="utf-8") as handle:
            raw = handle.read()
    except OSError as exc:
        raise ValueError(f"cannot read input file '{path}': {exc}") from exc

    for line_number, line in enumerate(raw.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if stripped.startswith("- "):
            continue
        if ":" not in stripped:
            continue

        name, _, value = stripped.partition(":")
        name = name.strip()
        value = value.strip()
        if not name:
            continue

        while parents and indent <= parents[-1][0]:
            parents.pop()

        if value == "":
            parents.append((indent, name))
            continue

        # Remove matching surrounding quotes, but preserve other characters.
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]

        full_key = ".".join([part for _, part in parents] + [name])
        data[full_key] = value

    return data


def _number(data, preferred_key, legacy_key, label):
    raw = data.get(preferred_key)
    if raw is None or not str(raw).strip():
        raw = data.get(legacy_key)

    if raw is None or not str(raw).strip():
        raise ValueError(
            f"missing {label}: set '{preferred_key}' in the video brief "
            f"(or legacy '{legacy_key}')"
        )

    text = str(raw).strip().replace(",", "")
    if text.startswith("<") and text.endswith(">"):
        raise ValueError(
            f"{label} is still a template placeholder ({text}); replace it with a number"
        )

    try:
        value = float(text)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be a number; received {raw!r}") from exc

    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{label} must be a finite number greater than zero")

    return value


def write_out(out_dir, name, lines, overwrite=False):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, name)
    if os.path.exists(path) and not overwrite:
        raise ValueError(
            f"refusing to overwrite existing output '{path}'; "
            "choose a new --out directory or pass --overwrite"
        )

    # Write to a temporary file first so a failed write does not truncate the
    # previous report.
    temporary_path = path + ".tmp"
    try:
        with open(temporary_path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("\n".join(lines) + "\n")
        os.replace(temporary_path, path)
    finally:
        if os.path.exists(temporary_path):
            os.remove(temporary_path)

    print(f"wrote {path}")
    return path


def run(input_path, out_dir, overwrite=False):
    data = read_brief(input_path)
    minutes = _number(
        data, "video.target_minutes", "minutes", "target duration in minutes"
    )
    words_per_minute = _number(
        data, "video.words_per_minute", "words_per_minute", "words per minute"
    )
    word_budget = round(minutes * words_per_minute)

    report = [
        f"# {TITLE}",
        "",
        f"source: {input_path}",
        "",
        "## Inputs",
        f"- target_minutes: {minutes:g}",
        f"- words_per_minute: {words_per_minute:g}",
        "",
        "## Estimate",
        f"- estimated_word_budget: {word_budget}",
        f"- formula: {FORMULA}",
        "",
        "This is a planning estimate, not a generated script or a validation "
        "of the final script's actual word count, timestamps, platform limits, "
        "or runtime.",
        "",
        "## Guardrails to keep",
        "- Never suggest using music, clips or footage the user has not licensed.",
        "- Never promise a view count, subscriber number or revenue for the video.",
        "- Never paste a competitor's script or transcript into the draft.",
    ]
    return write_out(out_dir, "calculation.md", report, overwrite=overwrite)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input", required=True, help="video brief YAML file")
    parser.add_argument("--out", default="./out", help="output directory")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="replace an existing calculation.md in the output directory",
    )
    args = parser.parse_args()

    try:
        run(args.input, args.out, overwrite=args.overwrite)
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
