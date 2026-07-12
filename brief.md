# Brief

## Question

Why do the people whose work became the foundation of modern technology (the MOSFET, TCP/IP, DNS, NTP, SQLite, zlib, oral rehydration therapy, and many lesser-known primitives) capture almost none of the value it carries, while the largest fortunes accumulate at bottlenecks, control over the points that use must pass through? And why is that bottleneck control routinely narrated as though it were the building of the underlying technology?

## Claim

Private wealth measures appropriability and control, not civilizational contribution. There is a systematic divergence between the social value a contribution creates and the private value its creator can capture, and the divergence is largest exactly for the most foundational work. This is not an accident of policy but a structural property: work becomes foundational by becoming non-excludable, standardized, cheap to replicate, and universally depended upon, and each of those properties is precisely what prevents its creator from charging for it (the non-appropriation principle). A technological civilization is a stack of serially dependent layers, each a potential tollbooth. If foundational layers each levied a small per-use toll, the tolls would compound (the Cournot complementary-monopoly result) and the anticommons would strangle throughput, so the value is real but its non-appropriation is the condition of civilization being able to use it. The fortunes that do form sit at the narrower, more excludable layers above the commons, and the culture mistakes ownership of a bottleneck for authorship of the stack.

The claim is NOT that all wealth is rent or that appropriability incentivizes nothing. Appropriability drives real innovation, and integration and scaling are real work. The claim is the systematic divergence between contribution and capture, and the mis-narration of control as creation.

## Kind

formal-model (ships a deterministic economic simulation). `has_simulation: true`, `claims_target: results.json`. The model instantiates the complementary-monopoly / royalty-stacking / anticommons economics on a serially dependent stack; every prose decimal maps to a `results.json` key. Numbers are illustrative properties of the model instantiating the economics, not empirical measurements; real-world dollar figures cited from sources belong to those sources and are recorded under an external-anchor key.

## Cornerstone literature

- Nordhaus (2004), Schumpeterian Profits, NBER w10433 — the empirical spine: innovators capture about 2.2 percent of the social surplus from innovation. LOAD-BEARING; verified.
- Cournot (1838) — complementary monopoly / serial tolls on perfect complements.
- Heller and Eisenberg (1998) — the tragedy of the anticommons (Science).
- Shapiro (2001); Lemley and Shapiro (2007) — patent thicket, royalty stacking.
- Arrow (1962) — non-appropriability of information as a public good.
- Samuelson (1954) — public goods; Romer (1990) — nonrivalry of ideas.
- Teece (1986) — appropriability regimes, complementary assets.
- Bresnahan and Trajtenberg (1995) — general-purpose technologies.
- Allen (1983) — collective invention; David (1985) — path dependence / QWERTY.
- Tullock (1967); Krueger (1974) — rent-seeking.
- Mazzucato (2013, 2018); Christophers (2020); Giblin and Doctorow (2022) — entrepreneurial state, rentier capitalism, chokepoint capitalism.

## Discipline notes

- House voice: no em-dashes, single-line paragraphs, numerals for quantities, distinctive section titles, no templated closer, no cross-citation of other PIATRA papers. Drop the engineer-shortlist framing of the seed; that is origin/case material, not the frame.
- Tone: rigorous and incisive, not a polemic. Name real firms and mechanisms where the analysis supports it; argue, do not sneer. Be genuinely fair to the strongest counterargument in its own section.
- Dollar figures from popular sources (IGBT $15.852T, open-source $8.8T) are secondary, attributed, cautioned; the load-bearing evidence is Nordhaus.
