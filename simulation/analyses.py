"""Tollbooth Civilization -- a deterministic model of tolls on a serially
dependent stack.

This is NOT an empirical measurement. It is a transparent economic model built to
instantiate three classical results on a single object, the "civilizational stack"
of N serially dependent layers, each of which can levy a per-use toll:

  1. Complementary monopoly (Cournot, 1838): when N essential complements are
     priced by independent owners, the tolls compound. Total price exceeds the
     single-integrated-owner price, and throughput and welfare fall as N rises.
  2. The anticommons (Heller & Eisenberg, 1998) in price form: fragmenting one
     road into many tollbooths can leave BOTH users and the toll-owners
     collectively worse off than a single owner would.
  3. The non-appropriation principle: the sustainable private capture of a single
     foundational layer falls as the stack deepens, so the more foundational and
     widely-complementary a layer is, the smaller the fraction of the value it
     carries that its creator can charge for without strangling adoption.

The market is normalized: a unit mass of potential uses (packets, transactions,
innovations) with willingness-to-pay uniform on [0, 1]. Baseline provision cost is
zero, so the only wedge is the toll. Linear demand is then Q(P) = 1 - P for the
total per-use price P = sum of layer tolls. Every headline number is a closed-form
property of this model; Study C re-solves a nonlinear-demand family numerically to
show the orderings are not artifacts of linearity.

    cd simulation && uv run run_all.py
"""
from __future__ import annotations

import numpy as np

# Deterministic; the only randomness is the seeded robustness jitter in Study C.
SEED = 20260712

# --------------------------------------------------------------------------- #
# Linear-demand closed forms.  Q(P) = 1 - P,  choke price 1, unit market, cost 0.
# N essential complements, each owner independently sets a per-use toll r_i to
# maximize r_i * Q(sum r).  Symmetric Nash equilibrium:
#     r* = 1/(N+1),  P_N = N/(N+1),  Q_N = 1/(N+1),
#     R_total = N/(N+1)^2,  CS = Q_N^2/2,  W_N = CS + R_total = (2N+1)/(2(N+1)^2).
# N = 0 is the open (untolled) stack; N = 1 coincides with a single integrated
# monopolist owning the whole stack.
# --------------------------------------------------------------------------- #


def _cfg(N: int) -> dict:
    """Symmetric Nash equilibrium of N independent tollbooths on one stack."""
    if N == 0:
        r_star, price, Q = 0.0, 0.0, 1.0
    else:
        r_star = 1.0 / (N + 1)
        price = N / (N + 1)
        Q = 1.0 / (N + 1)
    revenue_total = price * Q                # = N/(N+1)^2
    revenue_per_owner = revenue_total / N if N else 0.0
    consumer_surplus = 0.5 * Q * Q           # area of the demand triangle above P
    welfare = consumer_surplus + revenue_total
    return {
        "N": N,
        "toll_per_layer": round(r_star, 6),
        "total_price": round(price, 6),
        "throughput": round(Q, 6),
        "revenue_total": round(revenue_total, 6),
        "revenue_per_owner": round(revenue_per_owner, 6),
        "consumer_surplus": round(consumer_surplus, 6),
        "welfare": round(welfare, 6),
        "deadweight_loss": round(0.5 - welfare, 6),
        "throughput_frac_open": round(Q / 1.0, 6),
        "welfare_frac_open": round(welfare / 0.5, 6),
    }


def study_serial_tolls() -> dict:
    """Study A: the serial-toll collapse across a range of stack depths, plus the
    single-integrated-owner benchmark."""
    depths = [0, 1, 2, 3, 5, 10, 20, 50]
    table = [_cfg(N) for N in depths]

    # The integrated owner of the WHOLE stack sets one price; this is the N=1
    # closed form and is independent of how many layers the stack contains.
    integrated = {
        "total_price": 0.5,
        "throughput": 0.5,
        "revenue_total": 0.25,
        "consumer_surplus": 0.125,
        "welfare": 0.375,
        "deadweight_loss": 0.125,
    }
    openstack = _cfg(0)
    two = _cfg(2)
    ten = _cfg(10)
    twenty = _cfg(20)

    # The sharp anticommons contrast: splitting one road into two independent
    # tollbooths lowers the toll-owners' COMBINED take AND consumer surplus.
    anticommons = {
        "monopoly_revenue": integrated["revenue_total"],           # 0.25
        "two_tollbooth_revenue_total": two["revenue_total"],       # 0.222
        "revenue_lost_to_fragmentation": round(
            integrated["revenue_total"] - two["revenue_total"], 6),  # 0.028
        "monopoly_consumer_surplus": integrated["consumer_surplus"],  # 0.125
        "two_tollbooth_consumer_surplus": two["consumer_surplus"],    # 0.056
        "two_tollbooth_price_exceeds_monopoly": two["total_price"] > integrated["total_price"],
    }
    return {
        "depths": depths,
        "table": table,
        "open": openstack,
        "integrated_owner": integrated,
        "two_tollbooths": two,
        "ten_tollbooths": ten,
        "twenty_tollbooths": twenty,
        "anticommons": anticommons,
    }


def study_non_appropriation() -> dict:
    """Study B: the sustainable capture of a single foundational layer as a
    function of stack depth, and the divergence between the social optimum and the
    private optimum.

    A single owner tolls one of N essential complements at rate r while the other
    N-1 layers stay open. Per-owner revenue is rho(r) = r * (1 - r) with the rest
    open, but embedded in a stack where the OTHER layers also matter, the owner who
    tolls one of N symmetric layers at a common sustainable rate faces demand
    Q = 1 - N r, so per-owner revenue is rho(r) = r (1 - N r), maximized at

        r* = 1/(2N),   capture* = 1/(4N),   Q at optimum = 1/2.

    Taking the layer as a but-for-essential cause of the whole throughput surplus
    (each perfect complement is individually necessary, so its counterfactual
    contribution is the entire surplus W_open = 1/2), the capture ratio and
    civilizational leverage are

        kappa(N) = capture*/ (W_open) = 1/(2N),   leverage L(N) = 1/kappa = 2N.

    The attribution is deliberately generous to the layer (but-for, not
    equal-share); it is the same complementarity that makes the tolls compound in
    Study A. As the stack deepens, kappa falls and leverage rises: becoming more
    foundational strictly lowers the fraction of the value a creator can charge
    for.
    """
    W_open = 0.5
    depths = [1, 2, 5, 10, 20, 50, 100]
    rows = []
    for N in depths:
        r_star = 1.0 / (2 * N)
        capture = r_star * (1 - N * r_star)          # = 1/(4N)
        kappa = capture / W_open                       # = 1/(2N)
        leverage = 1.0 / kappa                          # = 2N
        rows.append({
            "N": N,
            "private_optimal_toll": round(r_star, 6),
            "sustainable_capture": round(capture, 6),
            "capture_ratio": round(kappa, 6),
            "capture_ratio_pct": round(100 * kappa, 4),
            "civilizational_leverage": round(leverage, 3),
        })

    # continuous divergence curves for a representative depth: social value W(r)
    # is maximized at r = 0 (open), while a single owner's revenue peaks at r*>0.
    N_rep = 20
    r_grid = np.linspace(0.0, 1.0 / N_rep, 201)     # up to the choke of the stack
    Q_r = np.clip(1.0 - N_rep * r_grid, 0.0, 1.0)
    W_r = 0.5 * Q_r * Q_r + (N_rep * r_grid) * Q_r  # CS + total toll revenue
    rho_r = r_grid * Q_r                              # one owner's revenue
    r_priv = 1.0 / (2 * N_rep)

    # depth at which the model's capture ratio equals Nordhaus's empirical 2.2%
    nordhaus_kappa = 0.022
    depth_at_nordhaus = 1.0 / (2 * nordhaus_kappa)   # ~22.7

    return {
        "W_open": W_open,
        "rows": rows,
        "representative_depth": N_rep,
        "social_optimum_toll": 0.0,
        "private_optimum_toll": round(r_priv, 6),
        "curve_r": [round(v, 6) for v in r_grid.tolist()],
        "curve_welfare": [round(v, 6) for v in W_r.tolist()],
        "curve_owner_revenue": [round(v, 6) for v in rho_r.tolist()],
        "kappa_at_depth_20": round(1.0 / (2 * 20), 6),
        "leverage_at_depth_20": 2 * 20,
        "nordhaus_capture_ratio": nordhaus_kappa,
        "depth_matching_nordhaus": round(depth_at_nordhaus, 1),
    }


# --------------------------------------------------------------------------- #
# Nonlinear-demand family Q(P) = choke * (1 - P)^theta, theta > 0. The symmetric
# Nash equilibrium of N independent tolls has a closed form. Owner i maximizes
# r*(1 - r - (N-1)r0)^theta; the first-order condition gives slack = r*theta, so
# at the symmetric point 1 - N r = r theta, hence
#       r* = 1/(N + theta),   P_N = N/(N + theta),   Q_N = choke*(theta/(N+theta))^theta.
# The single integrated owner sets P = 1/(1 + theta). Consumer surplus integrates
# in closed form to choke*(1-P)^(theta+1)/(theta+1). theta = 1 recovers the linear
# case. Both the throughput collapse (Q_N strictly falls in N) and the welfare
# ranking open > integrated > fragmented are therefore theorems for every theta.
# --------------------------------------------------------------------------- #


def _welfare_nonlin(P: float, theta: float, choke: float) -> float:
    """Total surplus at total price P: consumer surplus + toll revenue, closed form."""
    slack = max(0.0, 1.0 - P)
    cs = choke * slack ** (theta + 1) / (theta + 1)
    revenue = P * choke * slack ** theta
    return cs + revenue


def _nash_nonlinear(N: int, theta: float, choke: float) -> dict:
    """Closed-form symmetric Nash equilibrium of N tolls under (1-P)^theta demand."""
    if N == 0:
        P = 0.0
    else:
        P = N / (N + theta)
    Q = choke * max(0.0, 1.0 - P) ** theta
    return {"N": N, "price": P, "throughput": Q, "welfare": _welfare_nonlin(P, theta, choke)}


def _integrated_nonlinear(theta: float, choke: float) -> dict:
    """Single owner of the whole stack sets P = 1/(1+theta)."""
    P = 1.0 / (1.0 + theta)
    Q = choke * (1.0 - P) ** theta
    return {"price": P, "throughput": Q, "welfare": _welfare_nonlin(P, theta, choke)}


def study_robustness(n_draws: int = 2000) -> dict:
    """Study C: the orderings are not artifacts of linear demand. Over seeded draws
    of the demand curvature theta and the choke mass, check two orderings:
      (i)  throughput strictly falls as the stack is tolled more deeply
           (N = 2 > N = 5 > N = 10 in surviving throughput);
      (ii) open welfare > integrated-owner welfare > fragmented (N=10) welfare.
    Both hold in closed form for every theta > 0, so the fractions are 1.0; the
    draws confirm it numerically and measure how deep the collapse runs. The
    surviving-throughput ratio at N = 10 (Q_10 / Q_open) ranges over the draws,
    showing the collapse is present at every curvature while its depth varies.
    """
    rng = np.random.default_rng(SEED)
    thr_ok = welfare_ok = both_ok = 0
    q10_ratios = []
    for _ in range(n_draws):
        theta = float(rng.uniform(0.6, 1.6))
        choke = float(rng.uniform(0.8, 1.0))
        q0 = _nash_nonlinear(0, theta, choke)["throughput"]
        q2 = _nash_nonlinear(2, theta, choke)["throughput"]
        q5 = _nash_nonlinear(5, theta, choke)["throughput"]
        q10 = _nash_nonlinear(10, theta, choke)["throughput"]
        w_open = _nash_nonlinear(0, theta, choke)["welfare"]
        w_int = _integrated_nonlinear(theta, choke)["welfare"]
        w_frag = _nash_nonlinear(10, theta, choke)["welfare"]
        t_ok = q2 > q5 > q10
        w_ok = w_open > w_int > w_frag
        thr_ok += t_ok
        welfare_ok += w_ok
        both_ok += (t_ok and w_ok)
        q10_ratios.append(q10 / q0)
    q10_ratios = np.array(q10_ratios)
    return {
        "n_draws": n_draws,
        "seed": SEED,
        "theta_range": [0.6, 1.6],
        "choke_range": [0.8, 1.0],
        "nonlinear_nash_toll_form": "1/(N+theta)",
        "frac_throughput_ordering": round(thr_ok / n_draws, 4),
        "frac_welfare_ordering": round(welfare_ok / n_draws, 4),
        "frac_both": round(both_ok / n_draws, 4),
        "q10_over_open_min": round(float(q10_ratios.min()), 4),
        "q10_over_open_max": round(float(q10_ratios.max()), 4),
    }


def run() -> dict:
    return {
        "params": {
            "market_mass": 1.0,
            "choke_price": 1.0,
            "baseline_cost": 0.0,
            "packet_toll_thought_experiment": 0.0001,  # a hundredth of a cent, cited in prose
            "seed": SEED,
        },
        "serial_tolls": study_serial_tolls(),
        "non_appropriation": study_non_appropriation(),
        "robustness": study_robustness(),
        # External figures the prose quotes as decimals, recorded here so the
        # claims gate can reconcile them. These are NOT model outputs; they are the
        # reported values of cited sources, attributed in the prose to those
        # sources. The model measures nothing about the real world.
        "external_anchors": {
            "nordhaus_capture_pct": 2.2,          # Nordhaus (2004), NBER w10433
            "igbt_compendium_trillion_usd": 15.852,  # Baliga's own 2011 estimate (folk figure)
            "open_source_demand_trillion_usd": 8.8,  # Hoffmann, Nagle & Zhou (2024), HBS 24-038
            "open_source_supply_billion_usd": 4.15,  # same study, supply-side cost
        },
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
