"""Orchestrator: reproduces every number and the figure in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/tollbooth.png. Every decimal cited
in the paper is a key in the JSON file (model outputs under serial_tolls /
non_appropriation / robustness; quoted source figures under external_anchors).
The model is deterministic; the only randomness is the seeded demand-curvature
jitter in the robustness study.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_tollbooth

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_tollbooth(results, str(OUT / "figures" / "tollbooth.png"))

    st, na, rb = results["serial_tolls"], results["non_appropriation"], results["robustness"]
    op, integ, two = st["open"], st["integrated_owner"], st["two_tollbooths"]
    ten, twenty, ac = st["ten_tollbooths"], st["twenty_tollbooths"], st["anticommons"]

    print("Study A  serial-toll collapse (linear demand, closed form)")
    print(f"  open stack:        Q={op['throughput']:.3f}  W={op['welfare']:.3f}  capture={op['revenue_total']:.3f}")
    print(f"  integrated owner:  Q={integ['throughput']:.3f}  W={integ['welfare']:.3f}  capture={integ['revenue_total']:.3f}")
    print(f"  two tollbooths:    Q={two['throughput']:.3f}  W={two['welfare']:.3f}  "
          f"price={two['total_price']:.3f} (> monopoly 0.5)  combined capture={two['revenue_total']:.3f}")
    print(f"  ten tollbooths:    Q={ten['throughput']:.3f} ({100*ten['throughput_frac_open']:.1f}% of open)  "
          f"W={ten['welfare']:.3f} ({100*ten['welfare_frac_open']:.1f}% of open)")
    print(f"  twenty tollbooths: Q={twenty['throughput']:.3f} ({100*twenty['throughput_frac_open']:.1f}% of open)  "
          f"W frac open={twenty['welfare_frac_open']:.3f}")
    print(f"  anticommons: two booths take {ac['two_tollbooth_revenue_total']:.3f} combined < monopoly {ac['monopoly_revenue']:.3f}; "
          f"CS {ac['two_tollbooth_consumer_surplus']:.3f} < {ac['monopoly_consumer_surplus']:.3f}")

    print("Study B  non-appropriation")
    print(f"  W_open={na['W_open']}  private optimum toll (N=20)={na['private_optimum_toll']}  "
          f"kappa(20)={na['kappa_at_depth_20']}  leverage(20)={na['leverage_at_depth_20']}")
    print(f"  model capture ratio equals Nordhaus 2.2% at stack depth ~{na['depth_matching_nordhaus']}")

    print("Study C  robustness (nonlinear demand)")
    print(f"  {rb['n_draws']} draws: throughput ordering holds {rb['frac_throughput_ordering']}, "
          f"welfare ordering holds {rb['frac_welfare_ordering']}, both {rb['frac_both']}")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
