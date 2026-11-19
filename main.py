#!/usr/bin/env python3
"""Entry program for the make.fun contest news-image-20261119.

The picture itself lives in this repository as ``entry.png``: a
broadsheet front page summing up the world news of Thursday
19 November 2026 in 22 stories. This program's whole job is to place
that picture at the path the harness asks for. It reads nothing from
the network and uses only the Python standard library, and because it
copies a fixed file, repeated runs always produce the same bytes.
"""

import os
import shutil
from pathlib import Path

PICTURE = Path(__file__).resolve().parent / "entry.png"


def destination() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(folder) / "entry.png"


def main() -> None:
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(PICTURE, target)


if __name__ == "__main__":
    main()
