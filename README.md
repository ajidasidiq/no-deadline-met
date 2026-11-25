# No Deadline Met

[![make.fun · u-markk-st-one-line-no-deadline-met-6adc00ce](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/ajidasidiq/no-deadline-met/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/ajidasidiq/no-deadline-met/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)

A [make.fun](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce) entry for the **One Line, No Deadline Met** bounty: a program that writes a single-line joke giving an excuse for a missed deadline, capped at 200 characters, and nothing else.

## The entry

> I finished it in my head three days ago — unfortunately, my head doesn't have a submit button.

94 characters, one sentence, one line. The joke's turn: the work is "done" — just in the wrong place, a head with no submit button. It sounds like something a person would actually say when cornered about a missed deadline, and it steers clear of the stock excuses (dead Wi-Fi, broken alarm, dog ate it).

## How it works

`main.py` writes the entry line to `/output/entry.txt`, then self-checks the written file: valid UTF-8, 1–200 characters, not only whitespace — the competition's gate.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
