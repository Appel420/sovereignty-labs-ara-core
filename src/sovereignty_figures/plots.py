"""Plotting layer. All Isp-based thrust values come from thrust_from_power.
Style is scoped with rc_context so it cannot leak between plots.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from .thrust import thrust_from_power

FORMATS = ("png", "svg", "pdf")

_STYLE = {
    "font.family": "serif",
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.dpi": 200,
    "savefig.dpi": 300,
    "text.usetex": False,
}


def _export(fig: plt.Figure, out_dir: Path, stem: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for fmt in FORMATS:
        fig.savefig(out_dir / f"{stem}.{fmt}", bbox_inches="tight")
    plt.close(fig)


def make_thrust_plot(outpath: str | Path) -> None:
    outpath = Path(outpath)
    P = 25_000.0
    etas = [0.05, 0.10, 0.20]
    Isp = np.logspace(np.log10(1500), np.log10(10000), 400)

    Isp_ref = np.array([1500.0, 3000.0, 5000.0, 10000.0])
    F_ref = thrust_from_power(P, 0.10, Isp_ref)

    with mpl.rc_context(_STYLE):
        fig, ax = plt.subplots(figsize=(3.5, 2.8))
        for eta in etas:
            F = thrust_from_power(P, eta, Isp)
            ax.loglog(Isp, F, lw=2.0, label=rf"$\eta={eta:.2f}$")
        ax.scatter(Isp_ref, F_ref, s=18, zorder=5, label=r"$\eta=0.10$ markers")
        ax.set_xlabel(r"$I_{\mathrm{sp}}$ (s)")
        ax.set_ylabel("Thrust (N)")
        ax.set_title(r"Thrust vs $I_{\mathrm{sp}}$")
        ax.grid(True, which="both", ls=":", lw=0.6, alpha=0.6)
        ax.legend(frameon=False, loc="upper right")
        fig.tight_layout()
        _export(fig, outpath.parent, outpath.stem)


def make_velocity_plot(outpath: str | Path) -> None:
    outpath = Path(outpath)
    P = 25_000.0
    etas = [0.05, 0.10, 0.20]
    ve = np.logspace(np.log10(15_000), np.log10(100_000), 400)

    with mpl.rc_context(_STYLE):
        fig, ax = plt.subplots(figsize=(3.5, 2.8))
        for eta in etas:
            F = 2.0 * eta * P / ve
            ax.loglog(ve / 1000.0, F, lw=2.0, label=rf"$\eta={eta:.2f}$")
        ax.set_xlabel(r"$v_e$ (km/s)")
        ax.set_ylabel("Thrust (N)")
        ax.set_title(r"Thrust vs $v_e$")
        ax.grid(True, which="both", ls=":", lw=0.6, alpha=0.6)
        ax.legend(frameon=False, loc="upper right")
        fig.tight_layout()
        _export(fig, outpath.parent, outpath.stem)


def make_combined_plot(outpath: str | Path) -> None:
    outpath = Path(outpath)
    P = 25_000.0
    etas = [0.05, 0.10, 0.20]
    Isp = np.logspace(np.log10(1500), np.log10(10000), 400)
    ve = np.logspace(np.log10(15_000), np.log10(100_000), 400)

    Isp_ref = np.array([1500.0, 3000.0, 5000.0, 10000.0])
    F_ref = thrust_from_power(P, 0.10, Isp_ref)

    with mpl.rc_context(_STYLE):
        fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.8))

        ax = axes[0]
        for eta in etas:
            F = thrust_from_power(P, eta, Isp)
            ax.loglog(Isp, F, lw=2.0, label=rf"$\eta={eta:.2f}$")
        ax.scatter(Isp_ref, F_ref, s=18, zorder=5)
        ax.set_xlabel(r"$I_{\mathrm{sp}}$ (s)")
        ax.set_ylabel("Thrust (N)")
        ax.set_title(r"Thrust vs $I_{\mathrm{sp}}$")
        ax.grid(True, which="both", ls=":", lw=0.6, alpha=0.6)
        ax.legend(frameon=False, loc="upper right")

        ax = axes[1]
        for eta in etas:
            F = 2.0 * eta * P / ve
            ax.loglog(ve / 1000.0, F, lw=2.0, label=rf"$\eta={eta:.2f}$")
        ax.set_xlabel(r"$v_e$ (km/s)")
        ax.set_ylabel("Thrust (N)")
        ax.set_title(r"Thrust vs $v_e$")
        ax.grid(True, which="both", ls=":", lw=0.6, alpha=0.6)
        ax.legend(frameon=False, loc="upper right")

        fig.tight_layout()
        _export(fig, outpath.parent, outpath.stem)
