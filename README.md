# Tollbooth Civilization

Private wealth measures appropriability and control, not contribution to civilization. Work becomes foundational by being non-excludable, standardized, and widely depended upon, which is exactly what prevents its creator from charging for it, so the people whose work became the substrate of modern technology captured almost none of the value it carries. Great fortunes instead form at tollbooths, control of the bottlenecks that use must pass through, and the ownership of a tollbooth is later narrated as if it were the building of the road. The paper makes this rigorous with a deterministic economic model of a serially dependent stack in which each layer can levy a toll, instantiating the complementary-monopoly and anticommons results, and shows why the configuration that maximizes social value is the one in which creators capture nothing.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build tollbooth-civilization`.

## Simulation

```bash
cd simulation && uv run run_all.py   # -> output/results.json + output/figures/tollbooth.png
```

Deterministic; numpy + matplotlib. Every numeric claim in the paper traces to a
key in `simulation/output/results.json`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
