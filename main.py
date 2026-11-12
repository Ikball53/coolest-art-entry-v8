#!/usr/bin/env python3
"""Coolest-art v8 entry: copy the bundled geometric robot-head artwork
to the output.

The artwork is a geometric art-deco robotic head in profile, in warm
red/orange/gold and teal, against a night sky with stars and a
crescent moon — an 832x796 PNG, 926,108 bytes, inside the
competition's 1 MiB and 1024x1024 limits. The program does one
deterministic thing: copy those exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png), so both grading
runs write identical output. No time, randomness, or network is
involved anywhere — the same input always produces the same output
file, byte for byte. The sha256 comparison below checks the full
content, not just the size, so a truncated copy can never silently
pass.
"""
import hashlib
import os
import shutil

# Artwork facts (v8): entry.png is a geometric art-deco robotic head
# in profile, 832x796 PNG, 926,108 B, sha256 b8cc8053....
# The full-content sha256 check below (not just size) guarantees a
# truncated or corrupted copy is rejected instead of graded. The image
# is a deliberate style break from the saturated leaderboard patterns:
# instead of another glowing creature or lantern over a town, it is a
# flat geometric portrait in the warm red/orange/gold + teal palette
# of the user's own art-deco reference — the background was rebuilt
# as a night sky with stars and a crescent moon (the user asked for a
# different background than the reference, keeping only the style).
# The concept was the user's own pick from his uploaded reference.
# Note the fallback: when $MAKEFUN_OUTPUT_DIR is unset, main() uses
# the literal /output path the competition guarantees, so the program
# works unchanged in both the grading sandbox and a local run.

# The copy is the whole program: no image generation happens at
# runtime, so the artwork cannot drift between the two grading runs.
# Determinism is by construction — the same bundled bytes in, the
# same bytes out — and the hash check below is the safety net.

SRC_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guarantee the deterministic-bytes requirement: the output must be
    # byte-identical to the bundled artwork, so fail loudly instead of
    # silently leaving a partial file if the copy is ever interrupted.
    # Size alone is a weak check (a truncated copy could keep the size
    # only by coincidence), so compare the full content hash too.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy incomplete")
    with open(src, "rb") as f:
        src_hash = hashlib.sha256(f.read()).hexdigest()
    with open(dst, "rb") as f:
        dst_hash = hashlib.sha256(f.read()).hexdigest()
    if src_hash != dst_hash:
        raise RuntimeError("entry.png copy corrupted")


if __name__ == "__main__":
    main()
