# Research

Findings, tiered by source proximity. T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only). A claim that reaches the paper rests on a T1 or T2 source.

## The empirical spine

- [T1] Nordhaus, W. D. (2004), Schumpeterian Profits in the American Economy, NBER w10433. The abstract states only that "a minuscule fraction of the social returns from technological advances over the 1948-2001 period was captured by producers." The specific figure, innovators capture about 2.2 percent of the total surplus from innovation (nonfarm business sector, 1948-2001), appears in the body and is reported verbatim by the NBER Digest, "Who Gains from Innovation?" (Oct 2004). It follows from an instantaneous appropriability of about 7 percent depreciating at 20 percent per year. Verified at nber.org/papers/w10433 and the NBER Digest. LOAD-BEARING. Cite the 2.2 percent as the reported body/Digest figure, not an abstract quote.

## The toll arithmetic (what the simulation instantiates)

- [T1] Cournot, A. A. (1838), Recherches, ch. IX ("Of the Mutual Relations of Producers"). Two independent monopolists owning perfect complements (copper and zinc combined into brass) set a higher combined price and lower output than a single owner of both would. This is the complementary-monopoly result the model reproduces. English: Bacon translation (1897, Macmillan). Verified via Gallica/Wikisource.
- [T1] Heller, M. A., & Eisenberg, R. S. (1998), Can Patents Deter Innovation? The Anticommons in Biomedical Research, Science 280(5364):698-701. Too many fragmented, overlapping rights to exclude lead to underuse of a resource. The model reproduces this in price form: fragmenting one road into many tollbooths lowers throughput and can lower even the toll-owners' combined take. Verified (DOI 10.1126/science.280.5364.698, PMID 9563938).
- [T2] Shapiro, C. (2001), Navigating the Patent Thicket, in Innovation Policy and the Economy vol. 1, pp. 119-150, MIT Press. The patent-thicket / complements analysis (double marginalization across complementary patents). NOTE: the term "royalty stacking" is most properly attributed to Lemley & Shapiro (2007), Patent Holdup and Royalty Stacking, Texas Law Review 85 (pending confirmation from case-facts pass). Cite Shapiro (2001) for the thicket/complements, Lemley & Shapiro (2007) for the named stacking phenomenon.
- Model design: normalized unit market, willingness-to-pay uniform on [0,1], zero baseline cost. N serially dependent essential complements each set a per-use toll. Symmetric Nash (linear demand): r*=1/(N+1), P_N=N/(N+1), Q_N=1/(N+1), W_N=(2N+1)/(2(N+1)^2). Open (N=0): Q=1, W=0.5. Integrated owner: P=0.5, Q=0.5, W=0.375, capture 0.25. Two tollbooths: P=0.667 (> monopoly 0.5), Q=0.333, W=0.278, combined capture 0.222 < 0.25, CS 0.056 < 0.125 (the anticommons: fragmentation makes everyone poorer). Ten: Q=9.1% of open, W=17.4% of open. Twenty: Q=4.8% of open, W=9.3% of open. Nonlinear demand (1-P)^theta gives closed-form r*=1/(N+theta); throughput collapse and welfare ranking open>integrated>fragmented hold for every theta (2000 seeded draws: 1.0). All numbers -> simulation/output/results.json.

## Non-appropriation (why foundational value resists capture)

- [T1] Arrow, K. J. (1962), Economic Welfare and the Allocation of Resources for Invention, in The Rate and Direction of Inventive Activity, pp. 609-626, Princeton UP. Information is a public good: nonrival and, once disclosed, non-appropriable. The "fundamental paradox" of information. NOTE: 1962 volume has NO named editor (corporate NBER report); do NOT add "Nelson (Ed.)". pp. 609-626 verified (RePEc nberch/2144).
- [T1] Samuelson, P. A. (1954), The Pure Theory of Public Expenditure, Review of Economics and Statistics 36(4):387-389. Founding formal statement of nonrival collective-consumption (public) goods. Verified via JSTOR.
- [T1] Romer, P. M. (1990), Endogenous Technological Change, Journal of Political Economy 98(5, Pt. 2):S71-S102. Ideas are nonrival (and partially excludable); nonrivalry is the engine of growth and the reason value disperses. Verified (DOI 10.1086/261725), Part 2.
- [T1] Teece, D. J. (1986), Profiting from Technological Innovation, Research Policy 15(6):285-305. Value capture depends on the appropriability regime and ownership of complementary assets; under weak appropriability, whoever controls complementary assets profits, not the inventor. Verified (DOI 10.1016/0048-7333(86)90027-2). Directly supports the tollbooth mechanism.
- [T1] Allen, R. C. (1983), Collective Invention, Journal of Economic Behavior & Organization 4(1):1-24. Cleveland-district ironmasters freely shared blast-furnace design data; cumulative innovation outside the patent system. Verified. Supports "foundational work is often collectively produced, weakening any single capture claim."
- The non-appropriation principle (model form): a single foundational layer embedded in a stack of N complements can sustainably charge at most r*=1/(2N), capturing 1/(4N); under but-for attribution of the whole surplus, capture ratio kappa(N)=1/(2N) and civilizational leverage L(N)=2N. Becoming more foundational (larger N) strictly lowers the capturable fraction. The model's kappa reaches Nordhaus's 2.2% near N=23 (illustrative correspondence, not a fit).

## The stack, chokepoints, and mis-narration

- [T2] Bresnahan, T. F., & Trajtenberg, M. (1995), General Purpose Technologies: 'Engines of Growth'?, Journal of Econometrics 65(1):83-108. GPTs: pervasiveness, scope for improvement, innovational complementarities. The layers most depended upon are the most general and least appropriable. Verified.
- [T1] David, P. A. (1985), Clio and the Economics of QWERTY, American Economic Review 75(2):332-337. Path dependence / lock-in: an interface persists via network effects and switching costs, not efficiency. Supports how tollbooths hold once established. Verified.
- [T2] Christophers, B. (2020), Rentier Capitalism, Verso. The economy is increasingly organized around ownership of scarce assets (land, IP, platforms, contracts) yielding rents from control rather than production. Verified.
- [T2] Giblin, R., & Doctorow, C. (2022), Chokepoint Capitalism, Beacon Press. Firms capture creative labor markets by controlling chokepoints between makers and audiences. Verified. Names the mechanism the paper formalizes.
- [T2] Mazzucato, M. (2013), The Entrepreneurial State, Anthem Press; (2018), The Value of Everything, Allen Lane/PublicAffairs. The state absorbs foundational risk (DARPA/internet, NIH, public science); "value extraction" is narrated as "value creation." Directly supports the mis-narration section and the NASA/SpaceX co-production reading. Verified.
- [T1] Tullock, G. (1967), The Welfare Costs of Tariffs, Monopolies, and Theft, Western Economic Journal 5(3):224-232; Krueger, A. O. (1974), The Political Economy of the Rent-Seeking Society, American Economic Review 64(3):291-303. Rent-seeking: real resources are spent competing to control rents, a social loss beyond the deadweight triangle. Both verified.

## Case material (pending case-facts verification pass; see sources.md once frozen)

- TCP/IP: Cerf & Kahn (1974), A Protocol for Packet Network Intercommunication, IEEE Trans. Communications COM-22(5):637-648. Openly published; no per-packet royalty. The packet-tax thought experiment's anchor.
- MOSFET: Atalla & Kahng (Bell Labs, 1959-1960). Computer History Museum: most frequently manufactured artifact in human history (cumulative ~10^22). To be confirmed.
- SQLite (D. R. Hipp): public domain, among the most widely deployed database engines. To be confirmed.
- Oral rehydration therapy: glucose-sodium cotransport; unpatentable knowledge; The Lancet characterization ("potentially the most important medical advance..."). To be confirmed.
- PDF -> ISO 32000-1 (2008): proprietary format becoming an open international standard. The honest mixed case. To be confirmed.
- IGBT $15.852T: Baliga's OWN 2011 IGBT Compendium, a bottom-up engineering estimate, NOT independent econometrics. Attribute cautiously as a folk figure; do NOT present as a result.
- Open-source value: Hoffmann, Nagle & Zhou (2024), HBS Working Paper 24-038, ~$4.15B supply-side vs ~$8.8T demand-side. Illustrates the supply/demand-value divergence. To be confirmed.
