#!/usr/bin/env python3
"""v7 entrypoint: copy the shipped entry.png to the output directory.

Deterministic: the same bytes are written on every run. The sha256 of
the shipped image is checked before copying, so a corrupted bundle can
never silently produce a different entry.
"""
import hashlib
import os
import sys

EXPECTED_SHA256 = "cb58e2745cb239fccf2fa122650671bac4169179cdd16959aa72b93d602b05d0"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("entry.png sha256 mismatch: got " + digest, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)
    print("wrote entry.png (" + str(len(data)) + " bytes, sha256 " + digest + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
