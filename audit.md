# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-09-23 — prose revision

Prose rewritten against the house standards. Headings made descriptive (Introduction, Economics of non-appropriability, The layered stack and its chokepoints, A model of serial tolls, Capture at the upper layers and its attribution, Case studies, Scope and limits of the argument, Conclusion).

Tic counts before -> after: 'rather than' 7 -> 0; 'not X but Y' 8 -> 0; 'worth' 11 -> 0; 'this paper' 5 -> 0; inline ', not X' 2 -> 0; 'exactly/precisely' 2 -> 0.

Corrections found during the pass:
  - The text called r* = 1/(2N) "the revenue-maximizing toll on one of N symmetric layers". In analyses.py it maximizes r(1 - N r), i.e. the per-layer revenue when all N layers charge the same toll (the integrated-monopoly price split equally), which differs from the unilateral Nash toll 1/(N+1) of the preceding section. The text now states the common-toll assumption and gives the per-layer take 1/(4N) (0.0125 at N = 20, the value annotated in the figure).
  - The Nordhaus crossing depth was given as "near 23"; the closed form 1/(2 x 0.022) = 22.7 (results.json depth_matching_nordhaus) is now also stated.
  - Figure axis label "one owner's revenue" and "toll r on one of N layers" replaced with "per-layer revenue r(1-Nr)" and "common toll r on each of N = 20 layers" to match the computation.

Grid audit: every headline number is a closed form (r* = 1/(N+1), W_N, kappa = 1/(2N), depth 1/(2 kappa)); the nonlinear robustness study uses the closed form r* = 1/(N+theta). No grid-derived thresholds. Prose numbers checked against results.json: 0.5, 0.25, 0.375, 0.667, 0.333, 0.222, 0.125, 0.056, 9 and 5 percent throughput, welfare fractions 0.174 ("about a sixth") and 0.093 ("below a tenth"), 2.5 percent and leverage 40 at N = 20, q10/open 0.042 to 0.179 ("about 4 and 18 percent"). Arithmetic rechecked: 1/0.022 = 45 ("more than 40"); 1 - 0.022 = 97.8 ("about 98 percent"); 8.8 trillion / 4.15 billion = 2120 ("above a thousand"); 1e-4 x 1e19 = 1e15. results.json unchanged by the re-run.

Title left unchanged; it is long but not erroneous.

## 2026-07-12 — Initial draft, build, and gate pass

Scope: paper written end to end from the seed conversation; deterministic economic simulation built; all gates driven to clean.

Changes:
  - Set `metadata.yaml`: title "Tollbooth Civilization: Why the Work That Becomes Foundational Cannot Be Owned, and What Gets Owned Instead", header "Tollbooth Civilization", `has_simulation: true`, `claims_target: results.json`, abstract, `date: July 2026`, `status: built`.
  - Wrote `brief.md`, `research.md`, `sources.md` (20-source frozen bibliography), `README.md`.
  - Built `simulation/` (numpy + matplotlib): three studies on a serially dependent stack, the Cournot complementary-monopoly collapse, the anticommons in price form, and the non-appropriation principle `kappa(N) = 1/(2N)`. One command (`uv run run_all.py`) writes `output/results.json` + `output/figures/tollbooth.png`. Deterministic.
  - Wrote `paper/PAPER.md`: abstract + 8 argument sections + References. Dropped the seed's engineer-shortlist framing; kept the engineers as case material. Ends on a substantive point (the commons as constitutive condition, not market failure), no ceremonial closer.

Research / verification:
  - Two parallel web-verification passes. Economics bibliography: all 20 sources verified against NBER / JSTOR / RePEc / publisher DOIs. Corrections applied: Nordhaus 2.2% is a body/Digest figure (abstract says "minuscule fraction"); Arrow 1962 volume has no named editor; "royalty stacking" attributed to Lemley & Shapiro (2007), with Shapiro (2001) cited for the patent thicket.
  - Nordhaus 2.2% (nonfarm business, 1948-2001; 7% instantaneous appropriability depreciating 20%/yr) verified directly at NBER and the NBER Digest. LOAD-BEARING; used as the empirical spine, not a model output.
  - Case facts verified with provenance flags: IGBT $15.85T is Baliga's own compendium (self-reported, presented cautiously); open-source $8.8T demand / $4.15B supply (Hoffmann, Nagle & Zhou 2024, demand-side a modeled counterfactual); MOSFET ~10^22 (Computer History Museum); SQLite public domain / trillion+ databases (project's own claim); Cerf & Kahn 1974 (COM-22(5):637-648, openly published); ORT Lancet 1978; PDF -> ISO 32000-1 (2008); NASA COTS milestone awards; SEP royalty-stacking magnitude flagged as contested.

Verification (gates, from workspace root):
  - voice: 0 errors, 4 review-candidate warns (all triaged: one bare factual negation, the figure's model-not-measurement disclaimer, one developed interface contrast, one thesis-bearing section title). Advisories: lexical density and rhythm within range.
  - refs: 20 in-text citation keys, 20 bib entries, 0 missing, 0 unused.
  - claims: results.json 568 distinct values; 13 prose decimals, 0 without a matching value. Every prose decimal maps to a model output or a labelled external-anchor key.
  - build: 12 pages, 0 missing-character warnings, figure and math render, running header correct.
  - check => PASS.

Open / shaky (noted honestly):
  - The correspondence between the model's capture ratio and Nordhaus's 2.2% near a 23-layer stack is illustrative, not a calibration; stated as such in prose and caption.
  - Civilizational leverage uses but-for attribution (each essential complement credited with the whole surplus); flagged in prose as the generous choice, and as the same complementarity that compounds the tolls.
  - Rhythm advisory notes one 22-sentence run without a short sentence (partly an artifact of display-math lines being counted); prose rhythm is otherwise healthy (15% short, sd 16).

---

## 2026-07-12 — build + publish

Drafted from the seed chat (which opened on world-renowned electrical engineers and pivoted to a political economy of civilizational contribution). Converted the seed's polemical impulse into rigorous analysis: private wealth measures appropriability and control, not contribution; foundational work is uncapturable precisely because it is non-excludable, standardized, replicable, and complementary; fortunes form at tollbooths (excludable chokepoints), then narrated as road-building.

- The critique lands through arithmetic, not polemic. Model: the civilizational stack as N serially dependent essential complements, each able to toll; Cournot complementary-monopoly result (open welfare 0.5/zero capture; single owner keeps 0.25/welfare 0.375; two booths price 0.667 collecting 0.222 with consumer surplus 0.056, the anticommons; ten booths ~9% throughput, twenty ~5%); non-appropriation principle kappa(N)=1/(2N); robustness under Q=(1-P)^theta with r*=1/(N+theta) across 2,000 seeded draws.
- Honest numbers: Nordhaus 2004 (~2.2% innovator surplus capture) is the empirical spine; the model's kappa crossing 2.2% near N=23 is flagged "not a calibration." Folk trillion-dollar figures (IGBT 15.85T inventor's own estimate; open-source 8.8T modeled counterfactual, Hoffmann/Nagle/Zhou 2024) flagged as estimates and kept under an external_anchors key. Figure caption: "not a measurement of any real market."
- Fairness: the counterargument gets its own section ("What the Divergence Licenses"): appropriability incentivizes invention, integration/scaling are real work, the integrated owner is a legitimate second-best; the NASA/SpaceX case grants "Both claims hold." No sneering; real firms/mechanisms named but argued.
- Gates: voice 0 errors; refs 20/20, 0 missing/0 unused; claims 13/13 matched; build clean (12 pages); check => PASS. status -> published (July 2026); synced PDF; added ownPapers entry to piatra-institute-web/app/papers/page.tsx (topics economics/computer-science/sociology; kinds formal/simulation), left uncommitted.
