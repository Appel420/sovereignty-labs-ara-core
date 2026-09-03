# sovereignty-figures

Propulsion scaling figures for the 25 kW electric thruster stack.

## Canonical physics

All Isp-based thrust comes from one function:

```python
from sovereignty_figures import thrust_from_power
F = thrust_from_power(P=25_000.0, eta=0.10, Isp=3000.0)  # -> 0.16995 N
```

The velocity form `F = 2 eta P / v_e` is the equivalent path and is only
used where exhaust velocity is already known. Both paths agree to machine
precision (`ve = Isp * g0`).

## Plots

- `make_thrust_plot` — thrust vs Isp, three efficiency curves, computed markers
- `make_velocity_plot` — thrust vs exhaust velocity
- `make_combined_plot` — both side by side

Style is scoped with `matplotlib.rc_context`; no global `rcParams` leakage.

## Run

```bash
pip install -e .
sovereignty-figures --out-dir figures --prefix demo
```
