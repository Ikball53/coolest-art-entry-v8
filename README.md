# Coolest Art — eightbal (v8: geometric art-deco robotic head, night sky)

Entry for the make.fun competition `coolest-art-01`
("Make the coolest art").

The program copies the bundled artwork to the output: a geometric
art-deco robotic head in profile, in warm red/orange/gold and teal,
against a night sky with stars and a crescent moon. One piece of
art, in any style and of any subject — v4's striking snake scored
91.43% (rank 100/381), our best coolest score so far, but still
below the top-20 cutoff (95.07%), and v5's Santa scored only
71.47%; v6's lightbulb is still being graded. v8 is a deliberate
style break from the saturated leaderboard patterns (glowing
creature/lantern over a town): a flat geometric portrait in the
warm palette of a reference the user uploaded himself — the
background was rebuilt as a night sky (the user asked for a
different background than the reference, keeping only the style).
The concept was the user's own pick.

- `main.py` — stdlib-only, no network; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). Deterministic:
  both grading runs write identical bytes.
- `entry.png` — the artwork (832x796 PNG, 926,108 bytes, under the
  1 MiB and 1024x1024 limits).

License: MIT.
