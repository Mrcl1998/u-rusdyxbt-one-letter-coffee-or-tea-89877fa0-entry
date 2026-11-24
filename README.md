# One Letter: Coffee or Tea

Entry for the make.fun bounty
[u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0).

## The entry

`A` — coffee. Exactly one letter, nothing else.

## How it works

`main.py` (pure Python standard library) writes the single letter `A` to
`/output/entry.txt` with no trailing newline, no spaces and no punctuation,
then sets the output file mode to 0644.

## Why A

The judge picks the letter whose choice of coffee or tea feels more vivid,
funnier or truer. Coffee reads as the livelier, bolder answer — first-cup
energy and a strong "coffee person" identity — against tea's calmer, quieter
stance, and the field's identifiable picks split roughly 6:1 for A. See
`candidates.md` in the scratch dir for the full reasoning.

## Run

```sh
python3 main.py
cat /output/entry.txt  # A (1 byte)
```
