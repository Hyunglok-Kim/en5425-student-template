# EN5425/EV4240 — Semester Workspace

**Deep Learning Applications in Environmental Big Data — GIST, Fall 2026**

This repository is your **semester workspace** for EN5425/EV4240. Your code, labs, drafts, and capstone work live here under version control, from Week 1 to Week 16. Submissions of record (entrance tickets, HW0/note/milestone PDF reports) are made on the course website after signing in; this repo is where the work itself happens and where your public release is born. Your commit history is part of your work: it is how you (and the instructor) can trace what you did, when, and with which tools.

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
| `memos/` | Optional drafts of your entrance tickets (`weekNN.md` is just the ticket's label) — the ticket of record is submitted as text on the course site by **Sunday 13:00 KST** |
| `notes/` | Research notes: one note **after every lab**, using `notes/TEMPLATE.md` |
| `project/` | Your capstone foundation-model project (milestones from Week 4 onward) |
| `hw0/` | HW0, your ungraded starter project (spec in `hw0/README.md`) |
| `profile/` | Your profile card (`profile/profile.md`, photo optional) for the course site's public Cohort page |
| `scripts/` | Course-provided utility scripts (e.g., the HW0 data generator) |

## Conventions (read once, follow all semester)

- **Entrance ticket.** Submit your ticket on the course site (sign in from the top menu) by
  **Sunday 13:00 KST** before each session — 11 opportunities (W1–7, W9–12); W1's is due
  together with W2's on Sun 9/6. Format: 3-sentence summary, substantive critique, capstone
  connection, one real question. Tickets are 15% (best 10 × 1.5%, W1 non-droppable) and are
  written on the site's Journal Club page (private to instructor/TA; classmates see who submitted).
- **Research note after every lab.** Copy `notes/TEMPLATE.md` to
  `notes/weekNN.md` (e.g., `notes/week01.md`) and fill it in the same week as the lab. Notes are a weekly
  habit, written in your own words; export each finished note to PDF and submit it on the
  course site by Sunday 23:59 KST of that teaching week (lab-note portfolio: best 10 × 2%).
  Note content stays private — the public site shows submission status only.
- **Commit at every checkpoint, with informative messages.** Not one giant "final" commit.
  Your history is part of **AI-agent accountability** in this course: you are responsible
  for every line an agent writes, and a readable commit history is the record of how the
  work actually happened. "add temporal split + train-only scaling" is a commit message;
  "update" is not.
- **Profile.** Your card on the course site's **public Cohort page** is set on the site
  itself (sign in → Profile & avatar): display name, one-line bio, and an optional avatar
  (≤ 1 MB — a drawing, an avatar, or a favorite satellite image is equally welcome; it
  replaces the enrollment photo). Do this as part of HW0. It is public, so share only what
  you are comfortable with.
- **Never commit data or model checkpoints.** No datasets, no `*.pt` / `*.ckpt` /
  `*.safetensors`, no `wandb/` run directories, nothing over 50 MB. The `.gitignore` in
  this repo enforces most of this — do not fight it. Data is referenced by download
  scripts or paths, never by inclusion. (The one exception is the small course-provided
  `hw0/data/hw0_soil_moisture.csv`, which is explicitly allowed.)

## First deadlines

- **HW0** (see `hw0/README.md`): PDF report due **Monday 9/14, 23:59 KST on the course
  site**. Ungraded — it's the course's on-ramp, and everyone submits it. Stuck? Ask the
  researchers in S6, room 317 (HydroAI lab).
- **Week 1 + Week 2 entrance tickets** (on the papers assigned in the first class —
  Attention + ViT — and Reichstein et al. 2019): both due **Sun 9/6, 13:00 KST** on the
  course site. There is no pre-work before the first class on 8/31.
