# One day, one page — Thursday 19 November 2026

An entry for the make.fun contest **news-image-20261119**: the whole
of Thursday 19 November 2026 set as a single broadsheet front page,
1024 × 1024, small enough to read at a glance and complete enough to
read properly.

## What is on the page

- The date is the biggest type on the sheet. Under the masthead, a
  segmented bar tallies the stories by region — Asia-Pacific 13,
  Europe 11, Americas 9, Middle East 6, Oceania 4, Africa 2, World 1 —
  and a figures row lifts out the day's load-bearing numbers:
  Anthropic's $81.3bn IPO, 46,701 evacuations before Cyclone Akvan,
  and GTA VI's 212 GB pre-load.
- Forty-six stories in all. Thirteen carry flat vector illustrations:
  three heroes in one row (Shenzhen's trilateral summit at four
  tenths of the width; GTA VI's launch and Anthropic's market debut
  at three tenths each) and ten cards in two rows of five — Puri,
  Odesa, Riyadh, Berlin, The Hague, Hong Kong, Kuala Lumpur, Gaza,
  Washington and Tokyo.
- Each illustrated panel is numbered and shows its city, topic,
  headline, a short summary, its source, and a status tag: CONFIRMED,
  or CLAIM where the only sourcing is one side's own statement
  (Riyadh, Gaza, Washington).
- A UTC timeline strip runs beneath the cards: talks open 08:16, the
  four-point declaration lands 10:55, the World Court judgment is
  reported 13:07, Anthropic's first trade prints 16:50, and the close
  at 21:00 also catches the Dow's Thursday drop.
- The bottom band pairs a world map — thirteen numbered pins, one per
  illustrated story, every pin on land — with 33 further stories as
  compact briefs under a MORE NEWS heading, each with its source.
- A dark DATE CHECK band closes the sheet. It names fourteen stories
  that belong to Wednesday 18 November and were deliberately kept
  off, and states the page's rule: nothing appears here that was not
  first reported on the day itself.

## Reporting notes

The page was rebuilt after Thursday's results were known, so three
panels carry outcomes instead of expectations: Shenzhen's four-point
declaration (no new tariffs for twelve months; rare-earth licences
suspended for a year), the International Court of Justice finding by
9 votes to 6 that Myanmar committed genocide against the Rohingya,
and Anthropic closing its first day at $97.17, up 17%. A late brief
records the US Thursday selloff — Dow −1,101 points, Nasdaq −2.25% —
which the timeline's final mark also notes.

Sources were checked item by item before drawing: Reuters and AP for
the summit, the IPO and the selloff; the India Meteorological
Department's bulletins, carried by Indian press, for the cyclone;
Al Jazeera for Odesa and Gaza; DW for Berlin; UN News among the
sources for The Hague. Two numbers in wide circulation failed
checking and were left out: a claim of 200,000 cyclone evacuations
(the IMD figure is 46,701) and a claim of 15.9 million GTA VI
pre-orders (no primary source). The contested question of a US–China
tariff-truce extension was not asserted either way.

## How it was made

Design first, code second. A written sheet plan fixed the grid, the
type scale, the colour system (one dark ink for every headline, cream
labels) and the per-card sketch compositions before any rendering:
in each picture the main subject is whole and dominant with margin
around it, and lettering inside an illustration is either completely
inside the frame or absent. A Python renderer using Pillow draws the
page from a locked content file; it is deterministic, so repeated
renders are byte-identical. This repository ships the resulting
`entry.png` plus `main.py`, a standard-library-only program that
copies the picture to the output folder the harness specifies.

## Running it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Both harness runs produce the same bytes, because the program copies
a fixed file.

## Licence

MIT — see `LICENSE`.
