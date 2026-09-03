"""Canonical electric-propulsion thrust relations.

Single source of truth for thrust calculations. Plotting and derived paths
must call these functions rather than re-implementing the equation.
"""

from __future__ import annotations

import numpy as np

from .constants import g0


def thrust_from_power(
    P: float,
    eta: float,
    Isp: float | np.ndarray,
) -> float | np.ndarray:
    """Thrust from input power, efficiency, and specific impulse.

    F = 2 * eta * P / (Isp * g0)

    Parameters
    ----------
    P : float
        Input electrical power in watts.
    eta : float
        Propulsive efficiency, 0 < eta <= 1.
    Isp : float or array
        Specific impulse in seconds.

    Returns
    -------
    float or ndarray
        Thrust in newtons.
    """
    return 2.0 * eta * P / (np.asarray(Isp, dtype=float) * g0)


def thrust_from_exhaust_velocity(
    P: float,
    eta: float,
    ve: float | np.ndarray,
) -> float | np.ndarray:
    """Equivalent form using exhaust velocity directly.

    F = 2 * eta * P / ve, where ve = Isp * g0.
    """
    return 2.0 * eta * P / np.asarray(ve, dtype=float)
