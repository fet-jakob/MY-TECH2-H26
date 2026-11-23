# Home exam plan and progress

Claude updates this file at the end of every task. A fresh session starts by reading it.

## Status

| # | Stage | Points | Target time | Status | Key numbers / notes |
|---|---|---|---|---|---|
| 0 | Setup: kernel, notebook skeleton, git | – | Mon 23, 10:00–10:45 | done | pandas 3.0.5, no pyarrow; skeleton in `term_paper.ipynb`; code-style skill in `.claude/skills/` |
| 1a | Task 1: load and filter the three files | 20 | Mon 23, 10:45–13:00 | done (check questions open) | `patents` 2,835,599 rows / 45 MB · `green` 141,882 rows (114,924 patents) / 26 MB · `applicants` 3,059,537 rows / 433 MB · all 3 checkpoints ✓ · fresh-kernel run 18 s, peak 1.2 GB |
| 1b | Task 1: checkpoints + three overview numbers | (20) | Mon 23, 14:00–15:30 | not started | |
| 2 | Task 2: slump? (table + 3-panel figure) | 10 | Mon 23, 15:30–18:00 | not started | |
| 3 | Task 3: technology mix (shares + stacked bars) | 15 | Tue 24, 09:00–11:00 | not started | |
| 4 | Task 4: wind vs solar (peak table + line figure) | 20 | Tue 24, 11:00–13:30 | not started | |
| 5 | Task 5: one top-n function + two 2-panel figures | 25 | Tue 24, 14:00–18:00 | not started | |
| 6 | Task 6: AI statement (from the AI log below) | 5 | Tue 24, 19:00–19:30 | not started | |
| 7 | Final review: code-style skill, Restart and Run All, answers | 5 | Tue 24, 19:30–21:30 | not started | |
| 8 | Submit: final run, candidate numbers, Wiseflow | – | Wed 25, 08:30–10:30 | not started | Hard deadline 12:00 |

Biggest risks: Task 1 memory and run time (everything builds on it), and Task 5 (most points, the only general function).

## Data model (decide in Task 1a, then reuse everywhere)

Task 1 should leave three tidy objects so that Tasks 2–5 are only groupby, merge and plot:

| Object | One row per | Columns | Used in |
|---|---|---|---|
| `patents` | sample patent (2000–2019) | `appln_id`, `prio_year` | T1 checkpoint 1, T2 |
| `green` | (green patent, Y02E code) or (patent, category) | `appln_id`, `prio_year`, `main_group` label, `technology` label | T1, T2, T3, T4, T5 |
| `applicants` | (sample patent, applicant), deduplicated | `appln_id`, `app_name` (upper case), `ctry_code`, `app_share` | T1 checkpoint 3, T5 |

Points to settle in the 1a brief:
- How to keep peak memory down when reading the CPC file (35.6M rows, 834 MB): read 2 columns and keep only `Y02E` rows inside the function. Measure first, and read in chunks only if a full read is too heavy for the laptop.
- Whether to filter applicants to sample patents only. Checkpoint 3 and the "more than one country" count are over the whole sample, so keep all sample applicants, not just green ones.
- Upper-casing names after deduplication, so the checkpoint-3 sum is not changed. Re-check the sum after upper-casing.
- "Counts once per category": deduplicate on (`appln_id`, category) before every count.

## Task-by-task stages

**Task 1a: import.** One reading function per file (or one shared function if that is truly cleaner). Each reads `usecols` only, filters rows, and returns the small result. Outputs: `patents`, `green`, `applicants`. Check: the row counts printed once, compactly.

**Task 1b: checkpoints and overview.** Print the three checkpoints next to the expected values. Then compute:
- the average number of Y02E codes per green patent (2 decimals)
- the number of green patents in more than one main group
- the number of sample patents with applicants in more than one country

Present them in one small table or a few f-string lines.

**Task 2.** Build a DataFrame indexed by `prio_year` with green count, total count and share (%). Make a figure with 3 vertically stacked panels and a shared x-axis (`plt.subplots(3, 1, sharex=True)`, as in W3 Ex2). Answer: the development over time, slump start and end, and whether it is green-specific or general.

**Task 3.** Map years to the four periods with a general rule, not four hard-coded filters. Count per (period, main group), compute each group's share of the period total (rows sum to 100 %), and plot stacked bars labelled with the Table 1 names. Answer: the dominant groups, how the mix shifts, and the link to the T2 slump.

**Task 4.** Take main group 10 only and count per (year, technology). Make a table with one row per technology: peak year, peak count, 2019 count and % change (1 decimal), sorted by peak count, largest first. Plot one line per technology, with a point and year label at each peak. Answer: which technologies collapsed and whether any recovered.

**Task 5.** Write ONE function, roughly `top_n(category, by, start, end, n=10)`. It should:
- map any Table 1 or Table 2 label to its patents
- keep each patent once per category
- merge with `applicants`, sum `app_share` by `ctry_code` or `app_name`, and return the top n

Then make two figures, each with 2 `barh` panels showing the largest at the top:
1. Countries, Renewable energy, 2005–09 vs 2015–19, with the same x-scale
2. Applicants, Solar vs Wind, 2000–19

Answer: the leading countries and how that changed, the kinds of organisations in solar vs wind, and whether the applicants explain the country shifts.

**Task 6.** A short statement built from the AI log below: tools, what they were used for, how output was checked, and where any copied code sits.

**Final review.** Use these prompts:
- `/code-style term_paper.ipynb` (Richard's skill: ruff, comments, docstrings, plus a presentation report)
- a fresh-kernel Restart and Run All, with the run time noted
- a grading-criteria pass per task
- a check that no file is read after Task 1
- a check that there are no names or student numbers in the notebook

## Decision log

| When | Decision | Why |
|---|---|---|
| Mon 23 | Notebook file is `term_paper.ipynb` (lower case); the empty `Term_paper.ipynb` was renamed | Matches CLAUDE.md; macOS ignores case, so two files can't coexist |
| Mon 23 | CPC file read in chunks of 1,000,000 rows, Y02E rows kept per chunk | Measured: same 6.8 s, peak 0.32 GB vs 1.84 GB for a full read |
| Mon 23 | `green` = one row per (patent, Y02E code) with `code`, `main_group` and `technology` labels (dicts from Tables 1–2); technology set only in group 10 | Labels ready for plots; code rows needed for codes-per-patent in 1b; no duplicate (patent, code) rows |
| Mon 23 | ruff's F401 auto-fix removed the unused `plt` import | Task 2 adds `import matplotlib.pyplot as plt` back to the imports cell |
| Mon 23 | Data notes for 1b/T5: 429 sample patents have no applicant row (2,835,170 covered); 12 applicant rows lack `ctry_code`; 8 group-10 codes (10/0…) have no technology | Affects the multi-country count and Task 5 country sums |
| Mon 23 | No pyarrow in TECH2, so pandas 3 `str` columns are Python objects (~50–60 B per value) | String columns drive memory; keep them few and filter early |

## AI log (feeds Task 6)

| When | Tool | Used for | How we checked it |
|---|---|---|---|
| Mon 23 | Claude Code (VS Code) | Setup: checked the TECH2 env, created the notebook skeleton, git repo | We checked versions and `git status` ourselves |
| Mon 23 | Claude Code (VS Code) | Task 1a: measured full vs chunked CPC read, wrote the three reading functions and the import cell | Checkpoints 1–3 reproduced; extra checks (code layout, labels, duplicates) in a scratch script; fresh-kernel run |
| Mon 23 | Claude (claude.ai) | Read the exam text and course material, checked the data files' structure and the three checkpoints, and wrote this plan and the VS Code setup | Checkpoints reproduced from the raw files |
