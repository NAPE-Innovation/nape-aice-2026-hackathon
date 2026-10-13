#!/usr/bin/env python3
"""Participant inference entry-point template; replace TODO with your own pipeline."""
import argparse
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description="Run frozen hackathon inference")
    parser.add_argument("--input", required=True, help="Organiser-provided test input path")
    parser.add_argument("--output", required=True, help="Destination predictions CSV")
    args = parser.parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    if not input_path.exists():
        parser.error(f"Input does not exist: {input_path}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # TODO: load pre-trained/frozen artefacts and produce challenge-specific CSV.
    # Do not train, fine-tune, refit or rebuild learned indexes during evaluation.
    raise NotImplementedError("Replace this stub with your team's inference implementation.")

if __name__ == "__main__":
    main()
