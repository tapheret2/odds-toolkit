# odds-toolkit

![status](https://img.shields.io/badge/status-active-brightgreen) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)

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
