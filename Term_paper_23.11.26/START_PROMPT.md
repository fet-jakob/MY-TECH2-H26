# Prompts for Claude in VS Code

Open the **Home Exam** folder in VS Code, so that `CLAUDE.md` loads automatically, and select the TECH2 kernel. Use a fresh conversation (`/clear`) for every task. `PLAN.md` carries the state between sessions.

---

## 1. First session (setup + Task 1a): paste this

```
<task>
We're starting our TECH2 home exam today (group of two; my groupmate Jakob is sitting with me for Task 1); the deadline is Wed 25 Nov 12:00. In this session we set up and then do Task 1a (importing the data). Nothing else.
</task>

<first_steps>
1. Read CLAUDE.md, PLAN.md and pages 2–6 of term-paper-h26.pdf. Then read the course material we'll lean on for Task 1: the read_csv/usecols and filtering parts of ../TECH2-H26/lectures/lecture2 and lecture3, lecture4 (groupby), lecture5 (merge), and the workshop4 and workshop5 solutions.
2. Setup:
   - check that `conda run -n TECH2 python -c "import pandas; print(pandas.__version__)"` works and report the version, and whether pyarrow is installed
   - create term_paper.ipynb with a title cell, a "Candidate numbers: ..." placeholder, an imports cell, and one markdown heading per task (1–6)
   - move code-style-SKILL.md to .claude/skills/code-style/SKILL.md (Richard's review skill from the AI-week repo; the folder already exists)
   - connect the folder to our private GitHub repo https://github.com/bjornjohanbakke-nhh/TECH2-home-exam.git: run `git init -b main` and `git add .`, then show me `git status` and confirm that data/, data.zip and scratch/ are NOT staged. After my ok, commit ("Setup: plan, rules, notebook skeleton"), add the remote as origin and run `git push -u origin main`. If the push asks for a login or fails, stop and tell me; I'll push from VS Code's Source Control panel instead.
   - mark stage 0 done in PLAN.md
3. Task 1a: follow the "how_we_work" loop in CLAUDE.md. Start with the brief and the proposed approach for reading the three files, including how you'll keep memory down and how big you expect each result to be. Then stop and wait for my go.
</first_steps>

<success_criteria>
At the end of this session, the import cells run top to bottom in a fresh kernel, the three objects from the PLAN.md data model exist, their sizes are reported, and PLAN.md is updated.
</success_criteria>
```

---

## 2. Every later session: paste this and fill in the stage

```
New session. Read PLAN.md and check the status table, the decision log and the last notes. Then do stage <1b / 2 / 3 / 4 / 5 / 6> and only that stage, following the how_we_work loop in CLAUDE.md.

Start by re-running the notebook top to bottom up to the end of the last finished task, so the kernel has our data. Confirm the Task 1 checkpoints still match. Then give me the brief for this stage and stop for my go.
```

---

## 3. Final review session (Tuesday evening)

```
Final review before submission. Read PLAN.md and term-paper-h26.pdf pages 2–3 (requirements and assessment).

1. Run /code-style term_paper.ipynb and show me the report. Apply only the formatting fixes; list the presentation issues for me to decide.
2. Restart the kernel and run all cells. Report errors, total run time, and peak memory if you can measure it.
3. Go through every requirement bullet on page 2 and the four assessment criteria on page 3, task by task. Make a table: requirement | met? | evidence (cell) | fix needed.
4. Check that every question in Tasks 2–5 has a markdown answer that cites our numbers, and that the numbers in the text match the output.
5. Check that no file is read after Task 1, that there are no absolute paths, and that there are no names or student numbers.

Don't change anything beyond formatting until I've seen the table.
```

---

## 4. Useful one-liners mid-task

- I'm lost: `Stop. Trace this cell for me step by step on 3 example rows, showing the intermediate DataFrame after each line.`
- I'll write it: `Give me the plan and one hint per step for this cell. No code. Check mine when I paste it.`
- Context is getting long: `Update PLAN.md with where we are, then I'll /clear and continue.`

---

## Why the prompts are written like this (Anthropic's prompting guide)

- **Context and the reasons behind the rules.** CLAUDE.md explains *why* each rule matters, such as the grading criteria and the school exam. Claude generalises better from reasons than from bare rules.
- **XML tags.** Context, grading, rules and workflow are kept in separate tags, so Claude doesn't mix them up.
- **Explicit action versus suggestion.** Claude briefs and stops at a gate before it edits anything ("wait for my go"). It acts freely inside a task, but takes nothing irreversible without asking.
- **Investigate before answering.** Claude must read the PDF page and the course material before it writes code. The verified data facts mean it doesn't need to guess the file quirks.
- **State tracking across context windows.** PLAN.md is the progress file, git commits are checkpoints, and there is a fresh session per task with a set startup routine. Richard's lecture 6 recommends the same thing.
- **Self-verification.** The checkpoints and sanity checks act as tests, and Claude is told never to hard-code them.
- **Avoid over-engineering.** No extra helpers, validation or tests. This matches Richard's "fighting LLM bloat" slide.
- **Say what to do, not only what to avoid.** Format and style are described positively (single quotes, one function per cell, short bullets).
