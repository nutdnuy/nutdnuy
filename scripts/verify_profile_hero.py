#!/usr/bin/env python3
"""Structural checks for the Image Generator profile hero assets."""

from pathlib import Path
import struct


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "profile-hero"
TARGETS = (ASSETS / "cinematic-dark.png", ASSETS / "cinematic-light.png")


def verify_asset(path: Path) -> None:
    header = path.read_bytes()[:24]
    assert header.startswith(b"\x89PNG\r\n\x1a\n")
    width, height = struct.unpack(">II", header[16:24])
    assert (width, height) == (1180, 610)
    assert path.stat().st_size > 400_000


def main() -> None:
    for path in TARGETS:
        verify_asset(path)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "./assets/profile-hero/cinematic-dark.png" in readme
    assert "./assets/profile-hero/cinematic-light.png" in readme
    print("profile hero checks passed")


if __name__ == "__main__":
    main()
