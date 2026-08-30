# Lab 01 — AI Toolkit Onboarding, Step by Step

**In class: ~50 minutes · finish at home · AI Toolkit Report (5-page PDF) due Sun 9/6, 23:59 KST**

Five tools power every single week of this course. Today you set up all five and make each
one *do something real* — not just install. Work through the tools **in order**; each block
ends with a **“Done when”** line — that is your proof, and its screenshot goes in your report.

If anything breaks: first ask the agent you just installed to debug it with you (that is the
habit this course builds). Still stuck → raise a hand today, or visit **S6 building, room 317**
this week — the HydroAI lab researchers are expecting you.

| # | tool | time | proof for the report |
|---|---|---|---|
| 1 | VS Code + Claude Code | 12′ | a diff you can explain |
| 2 | Codex in VS Code | 10′ | the two agents disagreeing |
| 3 | Google Colab | 8′ | `True` from the GPU check |
| 4 | Kaggle | 10′ | a GPU notebook that ran |
| 5 | GitHub | 10′ | your first pushed commit |

---

## 1 · VS Code + Claude Code (12′)

1. Install **Visual Studio Code**: <https://code.visualstudio.com> → Download → open it once.
2. Install **Claude Code**: follow the install page for your operating system —
   <https://code.claude.com/docs>. Sign in when prompted (create an Anthropic account if you
   don't have one).
3. In VS Code: **File → Open Folder** → your semester repository folder (created in step 5 —
   for now, any folder with this template's files in it works).
4. Open the built-in terminal (**Terminal → New Terminal**), type `claude`, press Enter.
5. First real task — type this to Claude Code:
   > Explain what smoke_test.py checks, in three sentences.
6. Second task — an actual edit:
   > Add a --quick flag to smoke_test.py that skips any slow checks. Show me the diff before applying.
7. **Read the diff line by line.** Accept it, run `python smoke_test.py --quick`, then look at
   `git diff` yourself. If you don't like it, ask the agent to revert.

**Done when:** you have a diff on screen that you could explain to a classmate. 📸 screenshot.

*Troubleshooting: `claude: command not found` → close and reopen the terminal (the installer
edits your shell profile). Behind a campus proxy → try the personal hotspot for the install step.*

## 2 · Codex in VS Code (10′)

1. Install **Codex**: <https://developers.openai.com/codex> → the Visual Studio Code extension
   (or the command-line install, your choice). Sign in with a ChatGPT account.
2. First, undo the previous edit so both agents start from the same file:
   ask Claude Code to revert `smoke_test.py`, or run `git checkout -- smoke_test.py`.
3. Give **Codex** the exact same request:
   > Add a --quick flag to smoke_test.py that skips any slow checks. Show me the diff before applying.
4. Put the two diffs side by side. Where do they disagree — flag parsing? which checks count
   as “slow”? error handling? **Noticing the disagreement is the exercise**: this is what
   critical code review of an agent looks like, and you will do it all semester.

**Done when:** you can name one concrete difference between the two diffs. 📸 screenshot.

## 3 · Google Colab (8′)

1. <https://colab.research.google.com> → sign in with a Google account → **New notebook**.
2. **Runtime → Change runtime type → Hardware accelerator: T4 GPU → Save.**
3. Run this cell:
   ```python
   import torch
   torch.cuda.is_available()
   ```
4. It must print **`True`**. If it prints `False`, the runtime type didn't take — redo step 2
   and **Runtime → Restart session**.
5. Habit to install now: **File → Save a copy in Drive** — Colab sessions are disposable,
   your Drive copy is not.

**Done when:** the cell prints `True`. 📸 screenshot (this exact screenshot is required).

## 4 · Kaggle (10′)

1. <https://www.kaggle.com> → create an account → **Settings → Phone verification**.
   Verification is what unlocks the free weekly GPU quota — don't skip it.
2. **Create → New Notebook** → right side panel → **Session options → Accelerator → GPU**.
3. Run the same two-line `torch.cuda.is_available()` check → `True`.
4. Note the **hours-per-week GPU quota** shown in the session panel — write the number down;
   it goes in your report (this quota is your training budget for several labs).

**Done when:** a Kaggle GPU notebook ran, and you know your weekly quota. 📸 screenshot.

## 5 · GitHub + your semester repository (10′)

1. Create a GitHub account (or use yours): <https://github.com>.
2. Tell git who you are (terminal):
   ```bash
   git config --global user.name  "Your Name"
   git config --global user.email "you@example.com"
   ```
3. Make an SSH key and add it to GitHub:
   ```bash
   ssh-keygen -t ed25519 -C "you@example.com"     # Enter, Enter, Enter
   cat ~/.ssh/id_ed25519.pub                      # copy the whole line
   ```
   GitHub → **Settings → SSH and GPG keys → New SSH key** → paste → Save. Then verify:
   ```bash
   ssh -T git@github.com          # expect: "Hi <username>!"
   ```
4. Create **your semester repository** from the course template:
   <https://github.com/Hyunglok-Kim/en5425-student-template> → **Use this template →
   Create a new repository** → name it `en5425-<your student id>` → **Private**.
5. Clone it and prove the toolchain end to end:
   ```bash
   git clone git@github.com:<your-username>/en5425-<id>.git
   cd en5425-<id>
   python smoke_test.py
   ```
6. First commit: edit `profile/profile.md` (one line about you), then
   ```bash
   git add -A && git commit -m "week 1: toolchain up" && git push
   ```
   Refresh the repository page — your commit is there.

**Done when:** your pushed commit is visible on github.com. 📸 screenshot.

---

## The deliverable: AI Toolkit Report (5-page PDF)

One page per tool. For **each** of the five:

1. **Setup** — what you did, in your words (3–5 lines; include what went wrong, if anything).
2. **One real task** — what you made it do, with the 📸 screenshot from its “Done when”.
3. **Where it fits** — one or two sentences: which part of your weekly course workflow
   (reading? labs? capstone training runs? version control?) this tool will carry.
4. **One limitation** — something concrete you noticed it cannot do, or does badly.

Export to PDF → submit in the **“AI Toolkit Report”** box on the Week 1 page of the course
site — **Sunday 9/6, 23:59 KST**. Anything that didn't work in class: finish at home *before*
starting HW0 (`hw0/README.md`) — HW0 assumes all five tools are alive.
