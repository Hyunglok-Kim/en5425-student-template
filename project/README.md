# Capstone Project — <working title>

Your semester project: individually **pretrain, fine-tune, evaluate, document, and
publicly release a small geospatial or weather/climate foundation model**. Milestones are
graded from Week 4 onward; the full milestone schedule, deliverable specs, and model-card
requirements live on the course site:

**→ Capstone page: see the course website (Project section).**

This directory is a stub until Week 4. Structure it as the project grows:

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
