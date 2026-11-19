"""Deliver the finished front page to the folder the runner names.

The artwork ships in this repository as ``entry.png`` beside this
file. Executing the module copies those exact bytes to ``entry.png``
inside the directory given by the MAKEFUN_OUTPUT_DIR environment
variable, falling back to /output when the variable is absent. The
copy is reported with its size and SHA-256 digest. Standard library
only; no network access; every run yields identical bytes.
"""

import hashlib
import os
import pathlib
import shutil

ARTWORK = pathlib.Path(__file__).resolve().parent / "entry.png"


def output_folder() -> pathlib.Path:
    named = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return pathlib.Path(named) if named else pathlib.Path("/output")


def deliver() -> pathlib.Path:
    folder = output_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.png"
    if target.resolve() != ARTWORK.resolve():
        shutil.copyfile(ARTWORK, target)
    return target


if __name__ == "__main__":
    placed = deliver()
    blob = placed.read_bytes()
    print("entry.png:", len(blob), "bytes, sha256", hashlib.sha256(blob).hexdigest())
