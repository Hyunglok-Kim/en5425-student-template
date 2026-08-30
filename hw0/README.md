# HW0 — Your Starter Project

**Due: Monday 2026-09-14, 23:59 KST** (two weeks after the first class). Submit the PDF report on the course site (sign in from the top menu); work lives in your repo.

> **HW0 is not graded and there is no pass/fail.** It is simply how *you* find out,
> hands-on, whether you can run this course's weekly workflow — and every later lab
> builds on the setup it leaves behind, so **everyone submits it**. Think of it as the
> course's on-ramp, not a test. It is designed for **4–8 relaxed hours with an AI coding
> agent**. Going to be late? Just tell the instructor — we'll sort it out together.
>
> **Stuck on anything — environment, git, Colab, the model?** Come to **S6, room 317
> (the HydroAI lab)** and ask the lab researchers. They are expecting you, they enjoy
> these questions, and asking is exactly how this course is meant to work.

**HW0 is also an honest preview: it is a compressed sample of an ordinary week.** If it
takes far longer than 8 hours, that's useful, personal information — bring it to office
hours and we'll plan around it, kindly.

The dataset ships with this repo at `hw0/data/hw0_soil_moisture.csv` (~10,000 rows:
`station_id, date, precip_mm, air_temp_c, ndvi, sand_frac, clay_frac, elevation_m,
sm_target`, where `sm_target` is volumetric soil moisture in m³/m³).

## Task

1. **Environment & accounts.** Working Python 3.11 env (`conda` or `uv`) named `en5425`,
   exported to `environment.yml` or `pyproject.toml` + lockfile. GitHub account with SSH
   key configured. `git` configured with your real name and university email.
2. **Compute check.** Use Google Colab with a GPU runtime (or a Kaggle GPU notebook —
   both are set up in the Week 1 lab). Capture proof: output of `nvidia-smi`, or a
   Colab cell showing `torch.cuda.is_available() == True` (CPU-only fallback accepted with
   a note explaining why).
3. **Repo.** Work in the `hw0/` directory of your semester repository
   (`en5425-<your-github-username>`, created from the course template — see the Setup
   page). The dataset ships with the template at `hw0/data/hw0_soil_moisture.csv`
   (~10,000 rows: `station_id, date, precip_mm, air_temp_c, ndvi, sand_frac, clay_frac,
   elevation_m, sm_target` where `sm_target` is volumetric soil moisture in m³/m³).
   While you are in the repo, set your cohort profile **on the course site** (sign in → Profile & avatar: display name, one-line bio, optional avatar ≤ 1 MB) — formerly `profile/profile.md`
   (display name + one-line bio; photo optional — see the notes in that file). It feeds
   the course site's public Cohort page — **required for the cohort page, not part of the
   rubric**.
4. **Train a small MLP** (`train_mlp.py`, runnable as `python train_mlp.py`): temporal
   train/val/test split (train ≤ 2018, val 2019, test 2020 — no leakage); standardize
   features using **train-set statistics only**; MLP with 1–2 hidden layers in PyTorch;
   Adam + MSE; fixed random seed.
5. **Baselines.** Report test RMSE, MAE, and R² for (a) predict-the-train-mean,
   (b) linear regression, (c) your MLP. Your MLP must beat baseline (a); beating (b) is
   expected but not required — if you don't, say why you think so.
6. **Log the run.** Save `results/metrics.json` (all three models' metrics + seed +
   hyperparameters) and `results/loss_curve.png` (train + val loss vs. epoch).
7. **Report** — write `report.md` (~1 page) in the repo, export it to **PDF (≤ 5 MB)** and submit the PDF on the course site: setup, split protocol, results table, the
   loss-curve figure, 3–5 sentences of interpretation, and one thing you would try next.
8. **First research note** (`notes/week01.md`, ~half page) using the course
   template: *What I did / What I learned / What confused me / Open questions.* Research
   notes are a weekly habit in this course; this is note #1. It will later be published to
   your course-website notes section.
9. **AI-agent accountability section** (inside `report.md`): name the agent(s) you used,
   2–3 sentences on what they did for you, and **quote the one line of code in your repo
   you understand least, then explain it in your own words.** (Yes, this is the
   oral-defense muscle. Start now.)
10. **Push everything** with a clean history: **at least 5 meaningful commits with
    informative messages** (not one giant "final" commit). Submit the repo URL plus your
    GPU/Colab proof **inside the PDF report you submit on the course site**.

## Deliverables checklist (all in the pushed repo unless noted)

- [ ] `environment.yml` or `pyproject.toml` (+ lock)
- [ ] `train_mlp.py`, runnable end-to-end from a fresh clone
- [ ] `results/metrics.json` and `results/loss_curve.png`
- [ ] `report.md` (1 page, incl. baselines table + agent-accountability section)
- [ ] `notes/week01.md`
- [ ] Cohort profile set on the course site (display name + bio; avatar optional) — required
      for the cohort page, not part of the rubric
- [ ] Compute proof (screenshot/log) included in the PDF report
- [ ] ≥ 5 meaningful commits; repo URL included in the PDF report, submitted on the course site by the deadline

## What a complete HW0 looks like

| Item | Complete means |
|---|---|
| Reproducibility | Fresh clone + documented env → `python train_mlp.py` runs to completion |
| Data hygiene | Temporal split with no leakage; scaling fit on train only |
| Learning happened | MLP test RMSE strictly better than mean-predictor baseline; loss curve shows training |
| Logging | `metrics.json` + `loss_curve.png` present and consistent with the report |
| Report | Complete, honest, ~1 page, includes baseline comparison and agent section |
| Research note | Present, follows template, written in your own words |
| Git practice | ≥ 5 informative commits; no secrets/datasets > 50 MB committed |
| Comprehension | Agent-accountability section is specific and correct (spot-checked; some students will be asked to explain a line in Week 2) |

This table is a **checklist, not a grade** — you'll get feedback on it, and you can
resubmit freely. If several rows feel out of reach even after a visit to S6 317, come
talk to the instructor: we'll figure out the right plan together, with zero judgment.
