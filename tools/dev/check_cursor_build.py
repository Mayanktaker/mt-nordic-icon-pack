#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Cursor build gate: unusable sources and corrupt chunks must fail loudly, never publish a partial pack,
# and non-image chunks must survive a rebuild. Guards the release path against an empty or broken suite.
# Usage: tools/dev/check_cursor_build.py

import struct
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools" / "icons"))

try:
    import generate_cursors as cursor_build
except ImportError:
    sys.exit("cannot import tools/icons/generate_cursors.py")

# Marker standing in for a previously generated cursor suite on disk.
SENTINEL = "previous-build-marker"

# Xcursor comment chunk type; not an image, so it must never be parsed as pixels.
COMMENT_TYPE = 0xFFFE0001


def seed_build(theme_dir: Path) -> None:
    # Simulate a good earlier build whose files a failed run must not destroy.
    theme_dir.mkdir(parents=True, exist_ok=True)
    (theme_dir / SENTINEL).write_text("good build\n")


def expect_failure(label: str, source: Path, theme_dir: Path, errors: list[str]) -> None:
    # A build with no usable source must raise SystemExit and leave the old pack untouched.
    cursor_build.SYSTEM_NORDIC_CURSORS = source
    cursor_build.OUT_DIR = theme_dir
    try:
        cursor_build.build_cursors()
    except SystemExit:
        pass
    except Exception as exc:  # noqa: BLE001 - any other error is a gate failure
        errors.append(f"{label}: raised {type(exc).__name__}, expected SystemExit")
        return
    else:
        errors.append(f"{label}: build reported success without a usable source")
        return
    if not (theme_dir / SENTINEL).exists():
        errors.append(f"{label}: destroyed the previous build before validating the source")


def synthetic_xcursor() -> bytes:
    # Xcursor holding one 2x2 image frame plus one comment chunk.
    pixels = bytes([10, 20, 30, 255]) * 4
    image = struct.pack("<9I", 36, cursor_build.XCURSOR_IMAGE_TYPE, 1, 1, 2, 2, 0, 0, 1) + pixels
    text = b"nordic"
    comment = struct.pack("<5I", 20, COMMENT_TYPE, 2, 1, len(text)) + text
    body = 16 + 2 * 12
    toc = struct.pack("<3I", cursor_build.XCURSOR_IMAGE_TYPE, 1, body) + struct.pack(
        "<3I", COMMENT_TYPE, 2, body + len(image)
    )
    return struct.pack("<4I", cursor_build.XCURSOR_MAGIC, 16, 0x10000, 2) + toc + image + comment


def check_mixed_chunks(errors: list[str]) -> None:
    # A non-image chunk must survive a rebuild instead of being parsed as pixel data.
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "source"
        dst = Path(tmp) / "output"
        src.write_bytes(synthetic_xcursor())
        try:
            cursor_build.process_xcursor_file(src, dst)
        except SystemExit as exc:
            errors.append(f"comment chunk: build aborted ({exc})")
            return
        rebuilt = dst.read_bytes()
        magic, _header, _version, toc_count = struct.unpack("<4I", rebuilt[:16])
        if magic != cursor_build.XCURSOR_MAGIC or toc_count != 2:
            errors.append(f"comment chunk: rebuilt file has magic={magic:#x} entries={toc_count}")
            return
        if b"nordic" not in rebuilt:
            errors.append("comment chunk: comment payload dropped during rebuild")
        image_start = 16 + 2 * 12 + 36
        if rebuilt[image_start : image_start + 16] == bytes([10, 20, 30, 255]) * 4:
            errors.append("comment chunk: image frame was not recoloured")


def truncated_xcursor() -> bytes:
    # Image chunk that declares 2x2 but carries only four pixel bytes.
    image = struct.pack("<9I", 36, cursor_build.XCURSOR_IMAGE_TYPE, 1, 1, 2, 2, 0, 0, 1) + b"\x01\x02\x03\x04"
    return struct.pack("<4I", cursor_build.XCURSOR_MAGIC, 16, 0x10000, 1) + struct.pack(
        "<3I", cursor_build.XCURSOR_IMAGE_TYPE, 1, 28
    ) + image


def check_atomic_failure(errors: list[str]) -> None:
    # A crash part-way through a build must leave the previously published pack untouched.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = root / "source"
        source.mkdir()
        (source / "truncated").write_bytes(truncated_xcursor())
        theme_dir = root / "theme"
        seed_build(theme_dir)
        (theme_dir / "index.theme").write_text("old theme\n")
        cursor_build.SYSTEM_NORDIC_CURSORS = source
        cursor_build.OUT_DIR = theme_dir
        try:
            cursor_build.build_cursors()
        except SystemExit:
            pass
        except Exception as exc:  # noqa: BLE001 - any other error is a gate failure
            errors.append(f"truncated chunk: raised {type(exc).__name__}, expected SystemExit")
            return
        else:
            errors.append("truncated chunk: build reported success")
            return
        if not (theme_dir / SENTINEL).exists():
            errors.append("truncated chunk: crashed build destroyed the published pack")
        if (theme_dir / "index.theme").read_text() != "old theme\n":
            errors.append("truncated chunk: crashed build replaced the published metadata")


def main() -> int:
    # Run every guard: unusable source, corrupt chunk, and non-image chunk preservation.
    errors: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        # Missing source directory.
        theme_dir = root / "missing-theme"
        seed_build(theme_dir)
        expect_failure("missing source", root / "absent", theme_dir, errors)

        # Source directory exists but holds no cursor files.
        empty_source = root / "empty-source"
        empty_source.mkdir()
        theme_dir = root / "empty-theme"
        seed_build(theme_dir)
        expect_failure("empty source", empty_source, theme_dir, errors)

    # A mixed image/comment chunk file must round-trip without corrupting either chunk.
    check_mixed_chunks(errors)

    # A corrupt chunk must abort without replacing the pack that is already published.
    check_atomic_failure(errors)

    for line in errors:
        print(f"FAIL  {line}")
    if errors:
        print(f"\n{len(errors)} cursor build guard failure(s)")
        return 1
    print("PASS  cursor builds fail loudly, never publish partial packs, and keep non-image chunks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
