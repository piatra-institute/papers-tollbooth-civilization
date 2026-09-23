# Tollbooth Civilization

Why the Work That Becomes Foundational Cannot Be Owned, and What Gets Owned Instead.

Rankings of private wealth are commonly read as rankings of contribution; the error has a definite structure. Work becomes foundational by becoming non-excludable, standardized, cheap to copy, and depended upon by everything built above it, and these same properties prevent its creator from charging for it. The designers of the internet's transport protocol, the metal-oxide-semiconductor transistor, the SQLite database, and oral rehydration therapy captured almost none of the value their work supports. We model a technological civilization as a stack of serially dependent layers, each able to levy a per-use toll. In a normalized market the open stack delivers social value 0.5 and its creators capture nothing; a single owner of the whole stack captures 0.25 and halves throughput; two independent tollbooths set a higher combined price than a single owner, collect less between them, and leave users worse off; twenty tollbooths reduce throughput to about 5 percent of the open level. When all layers charge a common revenue-maximizing toll, the capturable share of any one layer falls as $1/(2N)$ in the number of complementary layers, reaching the 2.2 percent of social surplus that Nordhaus estimated innovators capture at a depth of about 23 layers. Social value is maximized when creators capture nothing. Large fortunes form instead at narrower, excludable layers above the commons, where control of a point that use must pass through yields recurring revenue, and that control is then described as authorship of the infrastructure beneath it. Appropriability still funds invention, integration is real work, and a single integrated owner does less damage than a fragmented anticommons.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build tollbooth-civilization`.

## Simulation

```bash
cd simulation && uv run run_all.py   # -> output/results.json + output/figures/tollbooth.png
```

Deterministic; numpy + matplotlib. Every numeric claim in the paper traces to a key in `simulation/output/results.json`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
