"""Publication figure for *Tollbooth Civilization*. Reads scalars and curves from
the results dict; deterministic, no seed.

Three panels carry the argument:
  A  the serial-toll collapse: as more of a serially dependent stack is tolled by
     independent owners, total price rises above the single-owner price and
     throughput and welfare fall toward zero (Cournot complementary monopoly);
  B  the divergence of optima: social value peaks at a zero toll (the open stack),
     while a single layer-owner's revenue peaks at a strictly positive toll, so the
     configuration that maximizes value is the one in which creators capture
     nothing (the non-appropriation principle);
  C  capture ratio against stack depth: the sustainable private share of the value
     a foundational layer carries falls as 1/(2N), passing the empirically
     estimated innovator capture rate on the way down.
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#1e1e2e"
MUTED = "#6c7086"
ACCENT = "#8839ef"
WARM = "#d20f39"
COOL = "#1e66f5"
GREEN = "#40a02b"


def _closed(N):
    """Linear-demand Nash closed forms, vectorized over N >= 0."""
    N = np.asarray(N, dtype=float)
    Q = np.where(N == 0, 1.0, 1.0 / (N + 1.0))
    P = np.where(N == 0, 0.0, N / (N + 1.0))
    R = P * Q
    W = 0.5 * Q * Q + R
    return P, Q, W


def plot_tollbooth(results, path):
    st = results["serial_tolls"]
    na = results["non_appropriation"]
    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(13.5, 4.4))

    # --- Panel A: serial-toll collapse -----------------------------------
    Ns = np.arange(0, 21)
    P, Q, W = _closed(Ns)
    axA.plot(Ns, Q, color=ACCENT, lw=2.2, label="throughput $Q$")
    axA.plot(Ns, W, color=INK, lw=2.0, ls=(0, (5, 2)), label="welfare $W$")
    axA.plot(Ns, P, color=MUTED, lw=1.4, ls=":", label="total toll $P$")
    axA.axhline(0.375, color=GREEN, lw=1.2, alpha=0.8)
    axA.text(20, 0.39, "single owner: $W=0.375$", ha="right", va="bottom",
             fontsize=7.5, color=GREEN)
    axA.axhline(0.5, color=COOL, lw=1.0, alpha=0.5)
    axA.text(3.0, 0.505, "open stack: $W=0.5$", ha="left", va="bottom",
             fontsize=7.5, color=COOL)
    axA.set_xlim(0, 20)
    axA.set_ylim(0, 1.0)
    axA.set_xlabel("independently tolled layers $N$", fontsize=9)
    axA.set_ylabel("per unit of throughput", fontsize=9)
    axA.set_title("Price, throughput and welfare against tolled layers", fontsize=10, color=INK)
    axA.spines[["top", "right"]].set_visible(False)
    axA.legend(fontsize=7.5, frameon=False, loc="center right")

    # --- Panel B: divergence of optima -----------------------------------
    r = np.array(na["curve_r"])
    Wr = np.array(na["curve_welfare"])
    rho = np.array(na["curve_owner_revenue"])
    Nrep = na["representative_depth"]
    r_priv = na["private_optimum_toll"]
    axB.plot(r, Wr, color=INK, lw=2.2, label="social value $W(r)$")
    axB.plot(r, rho, color=WARM, lw=2.2, label="per-layer revenue $r(1-Nr)$")
    axB.axvline(0.0, color=COOL, lw=1.6)
    axB.text(0.0007, 0.04, "social\noptimum\n$r=0$", color=COOL, fontsize=7.5,
             va="bottom", ha="left")
    rho_peak = float(rho.max())
    axB.axvline(r_priv, color=WARM, lw=1.1, ls="--")
    axB.plot([r_priv], [rho_peak], "o", color=WARM, ms=5)
    axB.annotate(f"private optimum\n$r^\\star=1/(2N)$, take ${rho_peak:.3f}$",
                 xy=(r_priv, rho_peak), xytext=(0.0265, 0.085),
                 fontsize=7.5, color=WARM,
                 arrowprops=dict(arrowstyle="->", color=WARM, lw=1.0))
    axB.set_xlim(0, r[-1])
    axB.set_ylim(0, 0.55)
    axB.set_xlabel(f"common toll $r$ on each of $N={Nrep}$ layers", fontsize=9)
    axB.set_ylabel("value per unit of throughput", fontsize=9)
    axB.set_title(f"Welfare and per-layer revenue ($N={Nrep}$)", fontsize=10, color=INK)
    axB.spines[["top", "right"]].set_visible(False)
    axB.legend(fontsize=7.5, frameon=False, loc="center left", bbox_to_anchor=(0.03, 0.45))

    # --- Panel C: capture ratio vs depth ---------------------------------
    Ncurve = np.arange(1, 101)
    kappa = 1.0 / (2.0 * Ncurve)
    axC.plot(Ncurve, kappa, color=ACCENT, lw=2.2, label=r"capture ratio $\kappa=1/(2N)$")
    nk = na["nordhaus_capture_ratio"]
    dmatch = na["depth_matching_nordhaus"]
    axC.axhline(nk, color=WARM, lw=1.3, ls="--")
    axC.text(100, nk + 0.004, "Nordhaus (2004) estimate: 2.2%",
             ha="right", va="bottom", fontsize=7.5, color=WARM)
    axC.plot([dmatch], [nk], "o", color=WARM, ms=5)
    axC.set_xlim(1, 100)
    axC.set_ylim(0, 0.5)
    axC.set_xlabel("stack depth $N$ (complementary layers)", fontsize=9)
    axC.set_ylabel(r"sustainable private capture ratio $\kappa$", fontsize=9)
    axC.set_title("Capture ratio against stack depth", fontsize=10, color=INK)
    axC.spines[["top", "right"]].set_visible(False)
    axC.legend(fontsize=7.5, frameon=False, loc="upper right")

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
