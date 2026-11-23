# TECH2 home exam (H26): project rules for Claude

These instructions load at the start of every session. `PLAN.md` holds the task plan, status and logs. Read it at the start of every session before doing anything else.

<context>
I'm Bjørn Johan, a first-year BEDS student at NHH. This folder is our group's TECH2 home exam (term paper): green energy patents in EPO data. The exam text is `term-paper-h26.pdf`. Read the relevant page of it before working on any task, because the grader marks against its exact wording.

- Deadline: **Wed 25 Nov 2026, 12:00** in Wiseflow. Late submissions are not accepted. Our own target is to submit by 10:30.
- Deliverable: ONE notebook, `term_paper.ipynb`, in this folder. It holds group candidate numbers only (no names), and it is submitted with all output after Restart and Run All.
- Generative AI is allowed, but Task 6 must describe honestly how we used it. That is why we keep the AI log in `PLAN.md`.
- The school exam on 16 Dec is individual and on paper-style conditions, so I need to *understand* every line we hand in, not just have it.
</context>

<grading>
Points: T1 20 · T2 10 · T3 15 · T4 20 · T5 25 · T6 5 · runs without errors 5. A correct result is not enough on its own. Every task is also graded on:
1. **Efficiency**: memory and run time. Read only the columns we need and filter rows inside the reading function.
2. **No repetition**: never compute the same thing twice. Import all data in Task 1, and do not read files in Tasks 2–5.
3. **Code quality**: clear and commented code, with functions and loops where work repeats.
4. **Presentation**: markdown headings per task, one function per cell, one figure per cell, figures with title, axis labels and legend, no long printouts, answers to the questions in markdown cells.
</grading>

<hard_requirements>
- Read data only as `data/<original file name>` (a relative path). The grader puts a `data/` folder next to the notebook.
- Use only packages in the TECH2 conda environment (`environment.yml`: numpy, pandas 3.0.5, matplotlib, scipy). Run Python and ruff with `conda run -n TECH2 ...`. Never install anything.
- The notebook must survive Restart and Run All from a fresh kernel.
</hard_requirements>

<course_methods>
Write code the way the TECH2 lectures and workshops do, so I can read it, defend it and reuse it on the school exam. One method per job; don't show me alternatives unless I ask. The course material is at `../TECH2-H26/lectures/` and `../TECH2-H26/workshops/` (Richard Foltyn, part 2) and github.com/isabelhovdahl/TECH2 (Isabel Hovdahl, part 1: basics, functions). When unsure how the course does something, open the relevant lecture or workshop solution before writing code.

Taught, so use these: `pd.read_csv(..., sep=, usecols=)`, boolean masks, `.isin`, `.query`, `.loc`, `groupby(...).size()/.sum()/.mean()/.agg()`, `.transform`, `.unstack`, `value_counts`, `sort_values`, `idxmax`, `pd.merge(..., on=, how=)`, `pd.concat`, `.round`, f-strings, `def` with docstring and default arguments, loops over lists or dicts, `fig, axes = plt.subplots(n, m, sharex=True)`, `ax.plot/bar/barh/scatter/text`, `axhline/axvline`, `fig.suptitle`, `fig.tight_layout`.

Not taught but needed: `drop_duplicates`, `nunique`, `.str.startswith/.str.replace/.str.upper/.str[...]`, stacked bars, `encoding=`, reading in chunks if it turns out to be needed. These are fine, but the first time one appears, explain it in one plain sentence in the reply and in a code comment.
</course_methods>

<verified_data_facts>
Checked against the real files on 23 Nov (with awk and pandas 2.3; re-confirm in the TECH2 env):
- All three files are pipe-separated (`sep='|'`) with Windows line endings (pandas handles these).
- `202608_EPO_IPC.txt` has one row per *IPC code*, so a patent appears on many rows. Keep `appln_id` and `prio_year`, filter to 2000–2019, and reduce to one row per patent. That gives **2,835,599** ✓ (checkpoint 1). The file covers years 1991–2025.
- `202608_CPC_Classes.txt` pads codes with spaces: the file has `Y02E  10/72` (two spaces), while the PDF prints one. Don't match on the exact spacing. The main group is the two digits before `/`, and the technology is the first digit after `/`. Sample patents with at least one code starting `Y02E`: **114,924** ✓ (checkpoint 2). Some codes are `Y02E 10/0…`: they are main group 10 but belong to no technology (Table 2).
- `202608_EPO_App_reg.txt` starts with a UTF-8 BOM and has quoted fields. `encoding='utf-8-sig'` worked. 39 applicant names contain `|` inside quotes, so always use `pd.read_csv` and never split lines by hand.
- Region duplicates: read `appln_id, app_name, ctry_code, app_share`, then drop exact duplicate rows. Sum of `app_share` for sample patents: 2,835,140.42 → **2,835,140** ✓ (checkpoint 3). Without dedup: 2,836,797 ✗. Dedup on `person_id`: 2,835,167 ✗.
- pandas 3: copy-on-write is on, so assign with `df.loc[...] = ...` or new columns (never chained assignment). String columns use the new default `str` dtype.
</verified_data_facts>

<how_we_work>
We do ONE task at a time, following the stage list in `PLAN.md`. For each task:

1. **Brief.** Restate the task in 3–5 bullets: required outputs, exact definitions from the PDF, and the grading traps. Then propose the approach in plain language (data steps, which course method, which earlier object we reuse) and stop. Wait for my "go" before editing the notebook. This is the cheapest point to catch a misunderstanding.
2. **Build.** Add markdown and code cells to `term_paper.ipynb`, one logical step per cell. Run them in the TECH2 kernel. After each code cell, ask me one short check question about it (e.g. "what does `.nunique()` return here, and why not `.size()`?"). I answer in my own words before we move on. If I say "I'll write this one", give me the plan and hints only, never the code, and then check what I wrote.
3. **Verify.** Check results against the checkpoints and against common sense (do the shares sum to 100? does the total match an earlier count?). Run `conda run -n TECH2 ruff format term_paper.ipynb` and `ruff check`.
4. **Review.** Give a short review against the four grading criteria: what is good, and what is weak and should be fixed. Then I draft the markdown answers to the questions from *our* results. You check them for accuracy and point out missing evidence, but the wording stays ours.
5. **Close.** Update `PLAN.md`: status, key numbers, decisions, AI-log entry. Commit with git if the folder is a repo. Then stop and tell me the task is done. Don't start the next task in the same session unless I say so; I'll open a fresh session per task to keep context clean.
</how_we_work>

<code_style>
- Single quotes, NumPy-style docstrings, ruff config from `pyproject.toml`.
- Keep it simple: only what the task needs. No helper functions for one-off steps, no input validation, no try/except, no unit tests.
- Write general logic, never hard-coded numbers. The checkpoints are for checking, not for typing into the code.
- Every code cell gets short comments that explain *why*, not just what.
- Keep big intermediate objects small: drop columns we no longer need and use `del` for temporary frames inside functions.
</code_style>

<safety>
- Never modify, move or delete anything in `data/`, `data.zip` or `term-paper-h26.pdf`.
- Don't touch files outside this folder, apart from reading the course material.
- Ask before deleting files, rewriting git history, or pushing anywhere.
- If a step will use a lot of memory or time (for example a full read of the 834 MB CPC file), say so first and estimate it.
</safety>

<communication>
Keep replies short: bullets for plans, plain sentences for explanations, no walls of text. If something in the exam text is ambiguous, quote the exact line, give the two readings, recommend one, and let me decide. Don't guess silently. Never claim a result you haven't run.
</communication>
