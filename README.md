# EN5425/EV4240 — Semester Workspace

**Deep Learning Applications in Environmental Big Data — GIST, Fall 2026**

This repository is your **semester workspace** for EN5425/EV4240. Everything you produce in this course — labs, weekly paper memos, research notes, HW0, and your capstone project — lives here, under version control, from Week 1 to Week 16. Your commit history is part of your work: it is how you (and the instructor) can trace what you did, when, and with which tools.

## Getting started

1. Click **"Use this template"** on GitHub and create a **private** repository named
   `en5425-<your-github-username>` under your own account.
2. Invite the instructor as a **collaborator** (Settings → Collaborators → Add people; the
   instructor's GitHub handle is on the course site).
3. Clone your new repo, create the `en5425` conda environment, and run the smoke test:

   ```bash
   git clone git@github.com:<your-github-username>/en5425-<your-github-username>.git
   cd en5425-<your-github-username>
   conda env create -f environment.yml
   conda activate en5425
   python smoke_test.py
   ```

   You should see a `PASS` line. If you do not, fix it (with your AI agent) — that is
   exactly what Lab 0 and the first half of HW0 are for.

## Repository layout

| Directory | What goes in it |
|---|---|
| `labs/` | In-class lab work and lab follow-through, one subdirectory per lab (`labs/lab01/`, …) |
| `memos/` | Weekly paper-response memos: `memos/weekNN.md`, **due 24 h before class** |
| `notes/` | Research notes: one note **after every lab**, using `notes/TEMPLATE.md` |
| `project/` | Your capstone foundation-model project (milestones from Week 4 onward) |
| `hw0/` | HW0, the pass/fail gate assignment (spec in `hw0/README.md`) |
| `profile/` | Your profile card (`profile/profile.md`, photo optional) for the course site's public Cohort page |
| `scripts/` | Course-provided utility scripts (e.g., the HW0 data generator) |

## Conventions (read once, follow all semester)

- **Weekly memo.** `memos/weekNN.md` is due **24 hours before each class session**. Use the
  format in `memos/week01.md` (3-sentence summary, substantive critique, capstone
  connection, one real question). The memo is graded as part of paper discussion (30%).
- **Research note after every lab.** Copy `notes/TEMPLATE.md` to
  `notes/weekNN.md` (e.g., `notes/week01.md`) and fill it in the same week as the lab. Notes are a weekly
  habit, written in your own words; they will later be published to your course-website
  notes section.
- **Commit at every checkpoint, with informative messages.** Not one giant "final" commit.
  Your history is part of **AI-agent accountability** in this course: you are responsible
  for every line an agent writes, and a readable commit history is the record of how the
  work actually happened. "add temporal split + train-only scaling" is a commit message;
  "update" is not.
- **Profile card.** `profile/profile.md` is your self-authored card on the course site's
  **public Cohort page** — fill in the two lines (display name + one-line bio) as part of
  HW0. A photo (`profile/photo.jpg`, square, ≤ 1 MB) is optional and entirely self-chosen:
  a drawing, avatar, or favorite satellite image is equally welcome. It is public, so
  share only what you are comfortable with.
- **Never commit data or model checkpoints.** No datasets, no `*.pt` / `*.ckpt` /
  `*.safetensors`, no `wandb/` run directories, nothing over 50 MB. The `.gitignore` in
  this repo enforces most of this — do not fight it. Data is referenced by download
  scripts or paths, never by inclusion. (The one exception is the small course-provided
  `hw0/data/hw0_soil_moisture.csv`, which is explicitly allowed.)

## First deadlines

- **HW0** (see `hw0/README.md`): due **48 h before the Week 2 session**. It is pass/fail
  and a hard gate for the project.
- **Week 2 memo** (`memos/week02.md`): Reichstein et al. (2019), due 24 h before Week 2.
