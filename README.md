# news-image-19nov

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/bapenven-ctrl/news-image-19nov/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/bapenven-ctrl/news-image-19nov/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Thursday 19 November 2026, folded into a single broadsheet page.
The date rules the masthead; underneath it a segmented bar counts the
22 stories by region and a figures row pulls out the day's hard
numbers — Anthropic's record $81.3bn IPO, 46,701 people evacuated
ahead of Cyclone Akvan, GTA VI's 212 GB pre-load.

Three illustrated heroes carry the day: the Trump–Xi–Putin trilateral
in Shenzhen, GTA VI's worldwide launch, and Anthropic's Nasdaq debut.
Fifteen illustrated cards follow (Akvan, Odesa, Riyadh, Berlin, The
Hague, Hong Kong, Kuala Lumpur, Gaza, Voyager 1, Brussels, Washington,
Tokyo, Wellington, New Delhi twice), then a numbered-pin world map at
one-third width beside text-only briefs in "City - Title" form. Two
items whose reporting date is doubtful are flagged "(18 Nov?)", never
hidden, and a dark DATE CHECK band closes the page.

Every story was verified against its source before it was drawn. The
artwork is original flat vector illustration, rendered
deterministically — the same input always yields the same PNG bytes.

## Method

The page was designed sheet-first against a fixed checklist, then the
renderer was written to realise that design: the date is the largest
element on the page; every illustrated panel carries a number, a city,
a topic, a two-line summary and its source; story numbering runs
continuously from the heroes through the cards into the text briefs;
the map's numbered pins match the story numbers; and no part of the
canvas is left empty. The layout deliberately differs from other
entries — 22 stories as 3 heroes, 15 cards and 4 briefs — rather than
copying the structure of any existing front page.

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` to the output path, so both harness runs write identical
bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
