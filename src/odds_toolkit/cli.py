from __future__ import annotations

import argparse
import json
import sys

from .odds import (
    american_to_decimal,
    decimal_to_american,
    decimal_to_fractional,
    expected_value,
    fractional_to_decimal,
    implied_prob,
    remove_overround,
)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="odds-toolkit")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("convert")
    c.add_argument("--from", dest="fmt", choices=["decimal", "american", "fractional"], required=True)
    c.add_argument("--value", type=float, help="decimal or american")
    c.add_argument("--num", type=int, help="fractional numerator")
    c.add_argument("--den", type=int, help="fractional denominator")

    i = sub.add_parser("implied")
    i.add_argument("--decimal", type=float, nargs="+", required=True)
    i.add_argument("--devig", action="store_true")

    e = sub.add_parser("ev")
    e.add_argument("--prob", type=float, required=True)
    e.add_argument("--decimal", type=float, required=True)
    e.add_argument("--stake", type=float, default=1.0)

    args = p.parse_args(argv)

    if args.cmd == "convert":
        if args.fmt == "decimal":
            d = args.value
        elif args.fmt == "american":
            d = american_to_decimal(args.value)
        else:
            d = fractional_to_decimal(args.num, args.den)
        am = decimal_to_american(d)
        num, den = decimal_to_fractional(d)
        print(json.dumps({"decimal": d, "american": am, "fractional": f"{num}/{den}", "implied": implied_prob(d)}, indent=2))
        return 0

    if args.cmd == "implied":
        raw = [implied_prob(x) for x in args.decimal]
        out = {"raw": raw, "sum": sum(raw)}
        if args.devig:
            out["devigged"] = remove_overround(raw)
        print(json.dumps(out, indent=2))
        return 0

    if args.cmd == "ev":
        ev = expected_value(args.prob, args.decimal, args.stake)
        print(json.dumps({"ev": ev, "ev_pct": ev / args.stake}, indent=2))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
