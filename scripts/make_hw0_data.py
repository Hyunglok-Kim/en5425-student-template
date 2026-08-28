#!/usr/bin/env python
"""Generate hw0/data/hw0_soil_moisture.csv for EN5425 HW0.

Synthetic but physically plausible station soil-moisture dataset:

- 40 stations x every-7th-day sampling of a daily simulation spanning
  2016-01-01 .. 2020-12-31  (~261 dates/station -> ~10,440 rows), so the
  temporal split train <= 2018 / val 2019 / test 2020 works.
- Generative process: a single-layer exponential-decay bucket per station.
  Antecedent precipitation fills the bucket; drainage decays it with a
  texture-dependent time constant (clay drains slower, sand faster); a
  temperature- and NDVI-driven ET proxy empties it; volumetric soil moisture
  maps the bucket level between texture-dependent residual and saturated
  water contents; heteroscedastic observation noise is added; the result is
  clipped to 0.02-0.55 m3/m3.
- Fixed seed: fully reproducible.

Usage:  python scripts/make_hw0_data.py
Writes: hw0/data/hw0_soil_moisture.csv (relative to the repo root).
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 5425
N_STATIONS = 40
START, END = "2016-01-01", "2020-12-31"
SAMPLE_EVERY = 7  # output every 7th day of the daily simulation
SM_MIN, SM_MAX = 0.02, 0.55  # m3/m3 physical clip


def main() -> None:
    rng = np.random.default_rng(SEED)
    dates = pd.date_range(START, END, freq="D")
    n_days = len(dates)
    doy = dates.dayofyear.to_numpy()

    rows = []
    for s in range(N_STATIONS):
        station_id = f"ST{s:03d}"

        # ---- static station properties -----------------------------------
        sand = rng.uniform(0.10, 0.80)
        clay = rng.uniform(0.05, min(0.55, 0.95 - sand))  # sand+clay < 0.95
        elev = rng.uniform(20.0, 1500.0)                  # m
        wetness = rng.uniform(0.7, 1.4)                   # local climate factor

        # Texture-derived hydraulic parameters (Cosby-like)
        theta_s = 0.489 - 0.126 * sand                    # porosity
        theta_r = 0.02 + 0.10 * clay                      # residual
        s_max = 60.0 + 120.0 * clay                       # bucket capacity (mm)
        tau = 4.0 + 18.0 * clay                            # drainage e-folding (days)
        k = np.exp(-1.0 / tau)                             # daily decay factor

        # ---- daily forcings ----------------------------------------------
        # Precip: summer-peaked wet-day probability, gamma amounts (monsoon-ish)
        season = np.sin(2 * np.pi * (doy - 60) / 365.25)   # peaks ~ early July
        p_wet = np.clip(0.18 + 0.14 * season, 0.05, 0.45) * wetness
        wet = rng.random(n_days) < p_wet
        amounts = rng.gamma(shape=0.9, scale=9.0, size=n_days) * (1.0 + 0.8 * np.clip(season, 0, 1))
        precip = np.where(wet, amounts, 0.0)

        # Air temperature: seasonal cycle + elevation lapse + weather noise
        t_mean = 13.0 - 6.5 * elev / 1000.0
        temp = t_mean + 11.0 * np.sin(2 * np.pi * (doy - 105) / 365.25) + rng.normal(0, 2.2, n_days)

        # NDVI: greening follows warm season, damped at high elevation
        ndvi_amp = 0.30 * (1.0 - 0.25 * elev / 1500.0)
        ndvi = np.clip(
            0.35 + ndvi_amp * np.sin(2 * np.pi * (doy - 130) / 365.25) + rng.normal(0, 0.03, n_days),
            0.05, 0.90,
        )

        # ---- exponential-decay bucket ------------------------------------
        # S_t = k * S_{t-1} + P_t - ET_t, clipped to [0, s_max]
        pet = np.clip(0.30 + 0.14 * temp, 0.0, None) * (0.6 + 0.6 * ndvi)  # mm/day ET proxy
        S = np.empty(n_days)
        S[0] = 0.5 * s_max
        for t in range(1, n_days):
            S[t] = np.clip(k * S[t - 1] + precip[t] - pet[t], 0.0, s_max)

        # ---- map bucket level to volumetric soil moisture ----------------
        frac = S / s_max
        sm = theta_r + (theta_s - theta_r) * frac
        sigma = 0.008 + 0.03 * frac                        # heteroscedastic noise
        sm = np.clip(sm + rng.normal(0, 1, n_days) * sigma, SM_MIN, SM_MAX)

        # ---- subsample every 7th day for the released dataset ------------
        idx = np.arange(0, n_days, SAMPLE_EVERY)
        rows.append(pd.DataFrame({
            "station_id": station_id,
            "date": dates[idx].strftime("%Y-%m-%d"),
            "precip_mm": np.round(precip[idx], 2),
            "air_temp_c": np.round(temp[idx], 2),
            "ndvi": np.round(ndvi[idx], 3),
            "sand_frac": np.round(sand, 3),
            "clay_frac": np.round(clay, 3),
            "elevation_m": np.round(elev, 1),
            "sm_target": np.round(sm[idx], 4),
        }))

    df = pd.concat(rows, ignore_index=True)
    out = Path(__file__).resolve().parents[1] / "hw0" / "data" / "hw0_soil_moisture.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"wrote {out}  shape={df.shape}  stations={df.station_id.nunique()}  "
          f"dates {df.date.min()}..{df.date.max()}")


if __name__ == "__main__":
    main()
