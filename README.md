# odds-toolkit

Convert **decimal / American / fractional** odds, compute **implied probability**, remove **overround**, and rough **EV**.

Educational. Not betting advice.

## Install

```bash
pip install -e ".[dev]"
```

## CLI

```bash
odds-toolkit convert --from decimal --value 2.10
odds-toolkit implied --decimal 1.91 2.05 --devig
odds-toolkit ev --prob 0.55 --decimal 2.0
```
