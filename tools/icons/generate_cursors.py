# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Generates companion Xcursor suite: authentic high-definition Nordic cursors in MT Nordic Blue.
# Multi-resolution (30x30, 45x45, 60x60) with Deep Polar Night body, Frost Cyan borders & Electric Cyan accents.
# --reuse-existing keeps the committed pack when the upstream source theme is not installed.

import os
import sys
from pathlib import Path
import shutil
import struct
import numpy as np

try:
    from icon_palette import REPO_ROOT, cursors_meta
except ImportError:
    from tools.icons.icon_palette import REPO_ROOT, cursors_meta

CURSORS = cursors_meta()
TECH_NAME = CURSORS["tech_name"]
DISPLAY_NAME = CURSORS["name"]
COLOR = CURSORS["color"]
OUT_DIR = REPO_ROOT / "src" / "cursors" / TECH_NAME
SYSTEM_NORDIC_CURSORS = Path.home() / ".icons" / "Nordic-cursors" / "cursors"

# Xcursor file layout constants (see the Xcursor file format spec).
XCURSOR_MAGIC = 0x72756358
XCURSOR_IMAGE_TYPE = 0xFFFD0002
XCURSOR_HEADER = 16  # magic, header size, version, toc entry count
XCURSOR_TOC_ENTRY = 12  # type, subtype, chunk offset
XCURSOR_IMAGE_HEADER = 36  # chunk header plus width/height/hotspot/delay

INDEX_THEME = f"""[Icon Theme]
Name={TECH_NAME}
Comment=Authentic Nordic cursor suite for {DISPLAY_NAME}
Inherits=Adwaita
"""


def hex_to_rgb(hex_color: str) -> tuple:
    # Convert #RRGGBB into RGB tuple.
    return tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))


# Nordic palette colour definitions from palette/icons.json
COLOR_BODY_BASE = hex_to_rgb(COLOR["bg"]["base"])               # #0E141D
COLOR_BODY_SURFACE = hex_to_rgb(COLOR["bg"]["surface"])         # #202D40
COLOR_BORDER_FROST = hex_to_rgb(COLOR["accent"]["base"])        # #88C0D0
COLOR_BORDER_WHITE = hex_to_rgb(COLOR["text"]["primary"])       # #ECEFF4
COLOR_ACCENT_CYAN = hex_to_rgb(COLOR["accent_flavors"]["cyber"]) # #00D2FF
COLOR_STATUS_RED = hex_to_rgb(COLOR["status"]["destructive"])    # #BF616A


def recolor_bgra_chunk(bgra_bytes: bytes, w: int, h: int) -> bytes:
    # Recolor an Xcursor BGRA image chunk into MT Nordic Blue tokens.
    arr = np.frombuffer(bgra_bytes, dtype=np.uint8).reshape((h, w, 4)).astype(np.float32)
    b, g, r, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    mask = a > 5

    # Safe un-premultiply alpha without divide-by-zero
    r_un = np.zeros_like(r)
    g_un = np.zeros_like(g)
    b_un = np.zeros_like(b)
    np.divide(r * 255.0, a, out=r_un, where=mask)
    np.divide(g * 255.0, a, out=g_un, where=mask)
    np.divide(b * 255.0, a, out=b_un, where=mask)

    max_c = np.maximum(np.maximum(r_un, g_un), b_un)
    min_c = np.minimum(np.minimum(r_un, g_un), b_un)
    lum = (max_c + min_c) / 2.0
    chroma = max_c - min_c

    # Detect color roles in source cursor
    is_red = (r_un > g_un + 25) & (r_un > b_un + 25) & (chroma > 20)
    is_cyan = (b_un > r_un + 15) & (chroma > 15)

    # 1. Dark body: #0E141D to #202D40
    t_dark = np.clip(lum / 110.0, 0, 1)
    body_r = COLOR_BODY_BASE[0] + t_dark * (COLOR_BODY_SURFACE[0] - COLOR_BODY_BASE[0])
    body_g = COLOR_BODY_BASE[1] + t_dark * (COLOR_BODY_SURFACE[1] - COLOR_BODY_BASE[1])
    body_b = COLOR_BODY_BASE[2] + t_dark * (COLOR_BODY_SURFACE[2] - COLOR_BODY_BASE[2])

    # 2. Bright perimeter border: Frost Cyan #88C0D0 to Snow White #ECEFF4
    t_light = np.clip((lum - 110.0) / 145.0, 0, 1)
    border_r = COLOR_BORDER_FROST[0] + t_light * (COLOR_BORDER_WHITE[0] - COLOR_BORDER_FROST[0])
    border_g = COLOR_BORDER_FROST[1] + t_light * (COLOR_BORDER_WHITE[1] - COLOR_BORDER_FROST[1])
    border_b = COLOR_BORDER_FROST[2] + t_light * (COLOR_BORDER_WHITE[2] - COLOR_BORDER_FROST[2])

    is_body = lum < 110.0
    out_r = np.where(is_body, body_r, border_r)
    out_g = np.where(is_body, body_g, border_g)
    out_b = np.where(is_body, body_b, border_b)

    # 3. Status Red accents
    out_r = np.where(is_red, COLOR_STATUS_RED[0], out_r)
    out_g = np.where(is_red, COLOR_STATUS_RED[1], out_g)
    out_b = np.where(is_red, COLOR_STATUS_RED[2], out_b)

    # 4. Electric Ice Cyan accents / spinners
    t_cyan = np.clip(lum / 255.0, 0, 1)
    out_r = np.where(is_cyan, COLOR_ACCENT_CYAN[0] + t_cyan * (COLOR_BORDER_FROST[0] - COLOR_ACCENT_CYAN[0]), out_r)
    out_g = np.where(is_cyan, COLOR_ACCENT_CYAN[1] + t_cyan * (COLOR_BORDER_FROST[1] - COLOR_ACCENT_CYAN[1]), out_g)
    out_b = np.where(is_cyan, COLOR_ACCENT_CYAN[2], out_b)

    # Re-premultiply alpha for Xcursor binary standard
    out_r = np.clip(out_r * (a / 255.0), 0, 255).astype(np.uint8)
    out_g = np.clip(out_g * (a / 255.0), 0, 255).astype(np.uint8)
    out_b = np.clip(out_b * (a / 255.0), 0, 255).astype(np.uint8)
    return np.stack([out_b, out_g, out_r, a.astype(np.uint8)], axis=-1).tobytes()


def recolor_image_chunk(src_path: Path, chunk: bytes) -> bytes:
    # Recolour one image chunk's pixels, refusing chunks whose header and pixel data disagree.
    if len(chunk) < XCURSOR_IMAGE_HEADER:
        raise SystemExit(f"{src_path}: truncated Xcursor image chunk")
    width, height = struct.unpack("<2I", chunk[16:24])
    pixel_bytes = width * height * 4
    if len(chunk) < XCURSOR_IMAGE_HEADER + pixel_bytes:
        raise SystemExit(
            f"{src_path}: image chunk declares {width}x{height} but holds "
            f"{len(chunk) - XCURSOR_IMAGE_HEADER} pixel bytes"
        )
    pixels = chunk[XCURSOR_IMAGE_HEADER : XCURSOR_IMAGE_HEADER + pixel_bytes]
    return chunk[:XCURSOR_IMAGE_HEADER] + recolor_bgra_chunk(pixels, width, height)


def process_xcursor_file(src_path: Path, dst_path: Path) -> None:
    # Recolour every image frame of an Xcursor file and carry any other chunk through untouched.
    data = src_path.read_bytes()
    if len(data) < XCURSOR_HEADER:
        raise SystemExit(f"{src_path}: truncated Xcursor header")
    magic, _header_size, version, toc_count = struct.unpack("<4I", data[:XCURSOR_HEADER])
    if magic != XCURSOR_MAGIC:
        # Not an Xcursor binary; copy it through unchanged.
        dst_path.write_bytes(data)
        return

    # Each TOC entry names a chunk; a chunk ends where the next one begins.
    entries = []
    for index in range(toc_count):
        start = XCURSOR_HEADER + index * XCURSOR_TOC_ENTRY
        entries.append(struct.unpack("<3I", data[start : start + XCURSOR_TOC_ENTRY]))
    offsets = sorted(entry[2] for entry in entries)
    ends = dict(zip(offsets, offsets[1:] + [len(data)]))

    new_chunks = []
    toc_entries = []
    cursor_offset = XCURSOR_HEADER + toc_count * XCURSOR_TOC_ENTRY
    for chunk_type, subtype, offset in entries:
        chunk = data[offset : ends[offset]]
        # Only image chunks carry pixels; comments and unknown types stay byte-identical.
        if chunk_type == XCURSOR_IMAGE_TYPE:
            chunk = recolor_image_chunk(src_path, chunk)
        new_chunks.append(chunk)
        toc_entries.append(struct.pack("<3I", chunk_type, subtype, cursor_offset))
        cursor_offset += len(chunk)

    header = struct.pack("<4I", magic, XCURSOR_HEADER, version, toc_count)
    dst_path.write_bytes(header + b"".join(toc_entries) + b"".join(new_chunks))


def source_cursors() -> tuple[list[Path], list[Path]]:
    # Real cursor files and alias symlinks from the source suite; aborts when unusable.
    if not SYSTEM_NORDIC_CURSORS.is_dir():
        raise SystemExit(f"source Nordic cursors not found at {SYSTEM_NORDIC_CURSORS}; nothing to build")
    real_files = [p for p in SYSTEM_NORDIC_CURSORS.iterdir() if p.is_file() and not p.is_symlink()]
    symlinks = [p for p in SYSTEM_NORDIC_CURSORS.iterdir() if p.is_symlink()]
    if not real_files:
        raise SystemExit(f"source Nordic cursors at {SYSTEM_NORDIC_CURSORS} hold no cursor files; nothing to build")
    return real_files, symlinks


def build_cursors() -> None:
    # Build into a staging copy, then swap it in, so a crash never leaves a partial pack published.
    real_files, symlinks = source_cursors()
    staging = OUT_DIR.with_name(f".{OUT_DIR.name}.tmp")
    if staging.exists():
        shutil.rmtree(staging)
    cursors_dir = staging / "cursors"
    cursors_dir.mkdir(parents=True)

    # Write the theme metadata the cursor pack is discovered by.
    (staging / "index.theme").write_text(INDEX_THEME)

    # Recolour every source cursor frame into the Nordic palette.
    for p in real_files:
        process_xcursor_file(p, cursors_dir / p.name)

    # Replicate the source alias symlinks so names like left_ptr keep resolving.
    for p in symlinks:
        target = os.readlink(p)
        link_dest = cursors_dir / p.name
        if link_dest.exists():
            link_dest.unlink()
        link_dest.symlink_to(target)

    # Publish only a finished pack: drop the old one and move staging into place.
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    staging.rename(OUT_DIR)
    print(f"Generated {len(real_files)} authentic Nordic cursors + {len(symlinks)} symlinks in {OUT_DIR}")


def main() -> None:
    # Rebuild the cursor pack; --reuse-existing tolerates a build host without the source theme.
    if "--reuse-existing" in sys.argv[1:]:
        if not SYSTEM_NORDIC_CURSORS.is_dir() and (OUT_DIR / "index.theme").is_file():
            print(f"Notice: no source at {SYSTEM_NORDIC_CURSORS}; keeping committed {OUT_DIR.name}")
            return
    build_cursors()


if __name__ == "__main__":
    main()
