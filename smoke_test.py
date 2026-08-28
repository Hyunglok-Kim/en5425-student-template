#!/usr/bin/env python
"""EN5425 environment smoke test.

Run:  python smoke_test.py
Exits 0 and prints a PASS line if your environment is ready for the course.
"""
import sys


def main() -> int:
    print(f"python      : {sys.version.split()[0]}")

    try:
        import numpy as np
        import pandas as pd
        import torch
        import xarray as xr
    except ImportError as e:
        print(f"\nFAIL: missing package -> {e}")
        print("Fix: conda env create -f environment.yml && conda activate en5425")
        return 1

    print(f"numpy       : {np.__version__}")
    print(f"pandas      : {pd.__version__}")
    print(f"torch       : {torch.__version__}")
    print(f"xarray      : {xr.__version__}")

    # Tiny in-memory xarray Dataset (the data model this course lives in)
    rng = np.random.default_rng(0)
    ds = xr.Dataset(
        {"soil_moisture": (("time", "lat", "lon"), rng.random((4, 3, 5)).astype("float32"))},
        coords={
            "time": pd.date_range("2026-01-01", periods=4, freq="D"),
            "lat": [35.0, 35.25, 35.5],
            "lon": [126.5, 126.75, 127.0, 127.25, 127.5],
        },
    )
    print(f"xarray dims : {dict(ds.sizes)}")

    # Quick tensor round-trip
    t = torch.as_tensor(ds["soil_moisture"].values)
    assert t.shape == (4, 3, 5), "unexpected tensor shape"

    cuda = torch.cuda.is_available()
    print(f"cuda        : {'available' if cuda else 'NOT available (CPU-only is OK for the smoke test)'}")
    if cuda:
        print(f"gpu         : {torch.cuda.get_device_name(0)}")

    print("\nPASS: EN5425 environment looks good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
