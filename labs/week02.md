# Lab 02 — Measure the Optimism Gap on CAMELS-US

**In class: 60 minutes · finish at home if needed · note due Sunday 23:59 KST**

You will train two models to predict how much water leaves a river basin, tune one
of them with a hyperparameter sweep, and then ask the only question that matters:
**does the score survive an honest split?** You will measure the *optimism gap* —
score(random split) − score(spatial split) — on real data, yourself.

**▶ The fastest path is the notebook: open
[`labs/week02_lab.ipynb`](week02_lab.ipynb) in Google Colab**
(<https://colab.research.google.com/github/Hyunglok-Kim/en5425-student-template/blob/main/labs/week02_lab.ipynb>)
**and run the cells top to bottom.** It loads the data by itself — nothing to
download, nothing to clone. This document is the reference version of the same lab.

Work with your coding agent throughout (that is the point of this course), but
verify every step marked **[verify yourself]** with your own eyes.

---

## 0 · Setup (before class or first 5 min)

In Colab: nothing — just sign in to Weights &amp; Biases when the notebook asks
(make the free account at <https://wandb.ai> beforehand). Running locally instead:

```bash
pip install torch scikit-learn wandb pandas matplotlib
wandb login
```

**Data.** The notebook reads a course copy of the CAMELS-US catchment attributes
(one CSV, 671 basins × 60 columns, `gauge_id` and `huc_02` included) directly from
this repository: `labs/data/camels_attributes.csv`. Original dataset and papers:
<https://ral.ucar.edu/solutions/products/camels> (Newman et al. 2015; Addor et al. 2017).

## 1 · Build the table (10 min)

One dataframe: **671 basins × (37 features + 2 targets)**.

- **Targets**: `runoff_ratio` and `q_mean` (model `log(q_mean)` — it spans orders of magnitude).
- **[verify yourself] Two groups of columns are banned as features:**
  1. every **hydrological signature** (`baseflow_index`, `q5`, `q95`, `high_q_freq`, …) —
     computed *from the basin's own streamflow record*, the thing you are predicting.
     Leakage before you even split (checklist item 4 from lecture);
  2. **`gauge_lat` / `gauge_lon`** — literally the basin's location: a model given
     coordinates memorizes geography, which is exactly what the spatial split tests.

## 2 · Two baselines under a random split (10 min)

1. `HistGradientBoostingRegressor` (scikit-learn, no tuning) — the honest tabular baseline.
2. A small multilayer perceptron in PyTorch (2 hidden layers, width 64, ReLU, dropout 0.2, AdamW).

- 5-fold **random** cross-validation (`KFold(5, shuffle=True, random_state=0)`).
- **[verify yourself]** Standardization lives *inside* the fold: fit the scaler on the
  training fold only (use an sklearn `Pipeline`, or fit `StandardScaler` per fold).
  Fitting it on all 671 basins is the classic silent leak.
- Log every run to Weights & Biases (`wandb.init(project="en5425-lab02")`): R² and
  root-mean-square error per fold, per target.

## 3 · Sweep the network (10 min)

W&B sweep (`bayes` or `random`, ~12 runs is plenty) over:

```yaml
learning_rate: log_uniform_values [1e-4, 1e-2]
hidden_width:  [32, 64, 128]
depth:         [2, 3]
dropout:       [0.0, 0.2, 0.4]
```

Pick the winner by mean random-split validation R². Open the sweep in the W&B web
interface → **parallel-coordinates panel** → export the image. That plot goes in
your note.

## 4 · The experiment: re-evaluate honestly (15 min)

Now the point of the whole lab. Same data, same winning model, one change:

```python
from sklearn.model_selection import GroupKFold
gkf = GroupKFold(n_splits=5)          # groups = huc_02 (the 2-digit region code)
```

Whole hydrologic regions are now held out — a fold never sees its neighbors.
Re-run the sweep winner **and** the gradient-boosting baseline. Then fill in:

| model | target | R² random | R² spatial (huc_02) | optimism gap |
|---|---|---|---|---|
| gradient boosting | runoff_ratio | | | |
| gradient boosting | log q_mean | | | |
| tuned network | runoff_ratio | | | |
| tuned network | log q_mean | | | |

**Expected result** (say it before you run it, then check): the spatial scores drop.
If your gap is near zero, that is also a finding — explain why (which features
carry information that transfers across regions?).

### Built-in honesty checks (do not skip)

The notebook will not let you coast:

- 🪤 **a trap cell** trains the leaky model most first drafts build (signatures left in,
  R² ≈ 0.94) — your note must explain why that number is a lie;
- ✍️ **a prediction gate** — you must write down your expected gap *before* the experiment runs;
- ✍️ **a fill-in blank** — you set the spatial grouping yourself.

**One question in next Monday's reading quiz comes from this notebook.**

## 5 · Write Note 02 (10 min)

Copy `notes/TEMPLATE.md` → `notes/week02.md` and include:

1. the **parallel-coordinates plot** from your sweep,
2. the **random vs spatial table** above, filled in,
3. a **one-paragraph leakage post-mortem**: which checklist item does the random
   split violate, what did the gap measure, and what split would you use if a
   reviewer asked you to defend the number?

Export to PDF and submit in the **"My research note (Week 2)"** box on the Week 2
page of the course site — **Sunday 23:59 KST**.

---

*Stuck? Ask your agent to explain any step — then make it show you the code it
wrote for fold-internal standardization, and check it. If you are still stuck,
S6 building, room 317: the HydroAI lab researchers are expecting you.*
