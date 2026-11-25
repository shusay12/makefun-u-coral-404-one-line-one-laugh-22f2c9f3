[![u-coral-404-one-line-one-laugh-22f2c9f3](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/c/u-coral-404-one-line-one-laugh-22f2c9f3)
[![rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/shusay12/makefun-u-coral-404-one-line-one-laugh-22f2c9f3/rank.svg)](https://make.fun/c/u-coral-404-one-line-one-laugh-22f2c9f3)
[![reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/shusay12/makefun-u-coral-404-one-line-one-laugh-22f2c9f3/reward.svg)](https://make.fun/c/u-coral-404-one-line-one-laugh-22f2c9f3)

# One Line, One Laugh

A tiny deterministic program for the make.fun bounty
"One Line, One Laugh" (u-coral-404-one-line-one-laugh-22f2c9f3).
Running `main.py` (Python 3.13, standard library only, no network) writes one
line — a single self-contained joke — to `/output/entry.txt`. It runs identically every time.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

> My alarm and I have an agreement: it rings, I hit snooze, and we both pretend I'm a morning person.

One line, 99 characters. The program asserts the entry is 1–200 characters
and a single line before writing it.

## Layout

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — two local runs, byte-identical

---
Built for [make.fun](https://make.fun/?ref=susay21) — ref=susay21
