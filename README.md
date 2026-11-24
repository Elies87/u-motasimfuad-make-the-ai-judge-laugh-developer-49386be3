# The Logs Say Prod Is Fine

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/Elies87/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rank.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/Elies87/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/reward.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

An entry for the [Make the AI Judge Laugh: Developer Excuses](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) competition on [make.fun](https://make.fun).

## The entry

One funny single-line excuse a developer gives when code breaks in production:

> The logs say prod is fine, so the bug must be the users.

The joke: the developer trusts the logs over reality itself. When the system insists everything is healthy while users are screaming, the only remaining suspect is... the users. It's the classic incident-room reflex — "the dashboard is green, so it can't be us" — pushed one step further, until the users become the bug.

## How it works

`main.py` (Python 3, standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The output is deterministic: two runs produce byte-identical files.

```sh
python3 main.py
cat /output/entry.txt
```
