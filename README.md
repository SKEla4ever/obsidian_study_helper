# obsidian_study_helper

An Obsidian starter vault for organizing course materials, concept notes, and practice.

## Try the starter

1. In Obsidian, choose **Open folder as vault** and select `starter/StudyVault`.
2. Open `Home.md` and follow **DEMO101 → Linear regression assumptions → Constant variance**. The example covers concept links, formulas, a slide and figure, and a browser-based simulation.
3. Open **Worksheet 01 · Q02** from the concept note. Expand its answer, then use the course's Practice page to find the question marked for review.

## Start a course

Copy `starter/StudyVault` to a personal folder outside this repository before adding your course materials. There, copy `Blueprints/Blank-Course` into `Courses`, or run the following from the copied vault using Python 3.

```bash
python3 Tools/new_course.py STA302-2026F --title "Regression Analysis"
```

Paste the printed link into the copied vault's `Home.md`. Start with one week's slides, notes, and a worksheet. See the [deployment guide](starter/Deployment-Guide.md) for the full workflow, sync options, and backup instructions.
