# Simulation: tolls on a serially dependent stack

A deterministic economic model for *Tollbooth Civilization*. It instantiates
three classical results on one object, the "civilizational stack" of `N` serially
dependent layers, each of which can levy a per-use toll:

1. **Complementary monopoly** (Cournot, 1838). Independent owners of `N` essential
   complements set tolls that compound: total price exceeds the single-owner price
   and throughput and welfare fall as `N` rises.
2. **The anticommons** (Heller & Eisenberg, 1998) in price form. Fragmenting one
   road into two tollbooths lowers the owners' *combined* take and consumer
   surplus at once.
3. **The non-appropriation principle.** The sustainable private capture of a single
   foundational layer falls as `1/(2N)`: the more foundational a layer, the smaller
   the share of the value it carries that its owner can charge for.

## Run

```bash
cd simulation
uv run run_all.py
```

Writes `output/results.json` and `output/figures/tollbooth.png`. Dependencies are
numpy and matplotlib (`pyproject.toml`); `uv` resolves them on first run.

## Model

Normalized market: a unit mass of potential uses with willingness-to-pay uniform
on `[0, 1]`, zero baseline provision cost, so demand at total per-use price `P` is
`Q(P) = 1 - P`. With `N` independent tolls the symmetric Nash equilibrium is
`r* = 1/(N+1)`, giving throughput `Q_N = 1/(N+1)` and welfare
`W_N = (2N+1) / (2(N+1)^2)`. `N = 0` is the open stack; `N = 1` is a single
integrated owner. Study C re-solves the nonlinear-demand family `Q(P) = (1-P)^θ`,
whose equilibrium toll is `r* = 1/(N+θ)` in closed form, to show the throughput
collapse and the welfare ranking (open > integrated > fragmented) hold for every
`θ > 0`.

## Files

- `analyses.py` — the three studies (serial tolls, non-appropriation, robustness).
- `figures.py` — the three-panel publication figure.
- `run_all.py` — orchestrator; writes `results.json` and the figure, prints a summary.
- `output/results.json` — every numeric value the paper cites. Model outputs live
  under `serial_tolls`, `non_appropriation`, and `robustness`; figures quoted from
  cited sources live under `external_anchors` and are NOT model outputs.

## Status of the numbers

Every value is a property of the normalized model, not a measurement of any real
market. The real-world dollar figures the paper quotes (Nordhaus's 2.2 percent
capture rate, the open-source and IGBT figures) belong to their sources and are
recorded under `external_anchors` purely so the paper's claims reconcile against a
single file. Deterministic; the only randomness is the seeded demand-curvature
jitter in the robustness study (`SEED = 20260712`).
