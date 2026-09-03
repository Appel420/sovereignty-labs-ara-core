"""Command-line entry point for sovereignty-figures."""

from __future__ import annotations

import argparse
from pathlib import Path

from . import plots


def main() -> None:
    parser = argparse.ArgumentParser(prog="sovereignty-figures")
    parser.add_argument("--out-dir", type=Path, default=Path("figures"))
    parser.add_argument("--prefix", type=str, default="thruster")
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    plots.make_thrust_plot(args.out_dir / f"{args.prefix}_thrust")
    plots.make_velocity_plot(args.out_dir / f"{args.prefix}_velocity")
    plots.make_combined_plot(args.out_dir / f"{args.prefix}_combined")


if __name__ == "__main__":
    main()
