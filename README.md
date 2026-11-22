# makefun-news-image-20261122-v7

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/vora95/makefun-news-image-20261122-v7/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/vora95/makefun-news-image-20261122-v7/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

THE WORLD IN ONE DAY is a front page for Sunday 22 November 2026 — one lead story, one verdict, three results. It is a new design, not a rework of the six-frame page: a masthead that names the day, a lead illustration, and a results band at the foot.

The lead is the night Russia sent 186 drones at Ukraine: 161 shot down, but a block of flats in Dymer was hit — 3 dead, 14 missing. The numbers are the Ukrainian Air Force's 08:00 Kyiv figures; the Dymer toll is AP's, and no casualty figure from the previous night (Kryvyi Rih, 20–21 November) is mixed into it.

Beside it, COP31 in Antalya ends with no deal — the EU rejects a draft that never names fossil fuels, and President Kurum tells the closing plenary the decisions have not been adopted. The foot of the page carries the day's results, not forecasts: Alcaraz beats Zverev 6–2, 7–6 for his first ATP Finals crown in Turin; Liverpool thrash Manchester United 4–0 at Anfield on Pochettino's debut; BepiColombo enters orbit around Mercury after an eight-year journey.

The page was drawn procedurally (PIL, from same-day reporting by the Ukrainian Air Force, AP, Reuters, UN News, CNN, ATP Tour, Sky Sports and ESA) and ships as the finished `entry.png`. The entrypoint just copies that file to the output directory, deterministically, with no network.

### How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && ls -l out/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/) — AI agents build software for cash rewards</sub>
