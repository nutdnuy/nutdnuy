#!/usr/bin/env python3
"""Structural checks for the Image Generator profile hero assets."""

from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "profile-hero"
TARGETS = (ASSETS / "cinematic-dark.svg", ASSETS / "cinematic-light.svg")


def verify_asset(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    root = ET.fromstring(text)
    assert root.attrib["viewBox"] == "0 0 1180 610"
    assert "data:image/png;base64," in text
    assert "<script" not in text and "javascript:" not in text
    assert text.count("<animate") >= 10
    assert path.stat().st_size > 900_000


def main() -> None:
    for path in TARGETS:
        verify_asset(path)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "./assets/profile-hero/cinematic-dark.svg" in readme
    assert "./assets/profile-hero/cinematic-light.svg" in readme
    print("profile hero checks passed")


if __name__ == "__main__":
    main()
