# Capstone Project — <working title>

Your semester project: individually **fine-tune and rigorously evaluate a public
foundation model** (default track, feasible on free-tier compute), document it, and
publicly release your work. Everyone pretrains a mini-model in the W7/W9 labs;
from-scratch FM development is the HydroAI lab team's joint Hydro-FM project.
Proposal due 11/1 13:00 KST (pitches 11/2); M1 12/4, M2 12/9, M3 12/13, final 12/16 —
all PDFs on the course site by 23:59 KST; the full milestone schedule, deliverable specs, and model-card
requirements live on the course site:

**→ Capstone page: see the course website (Project section).**

This directory is a stub until your proposal. Structure it as the project grows:

| Path | Purpose |
|---|---|
| `configs/` | Experiment configuration files (YAML/JSON) — one config per run, committed |
| `logs/` | Small text logs and run summaries (large logs and `wandb/` stay out of git) |

Reminders:

- Every lab from Week 2 onward is a brick of this project — carry lab code forward here.
- Never commit data or checkpoints (see the repo `.gitignore`); track weights on
  Hugging Face, not in git.
- Commit at every checkpoint with informative messages; your history is part of
  AI-agent accountability.
