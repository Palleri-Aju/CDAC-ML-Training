# PML Regression Day — Training Package (CDAC Kharghar, 26 Oct 2026)

Seven-hour, mathematics-first session: Simple & Multiple Linear Regression, OLS, Gradient Descent,
evaluation metrics, Polynomial Regression, Bias–Variance, and introductory Ridge & Lasso.
Teaching sequence for every topic: Problem → Intuition → Visual → Mathematics → Manual calculation →
Optimisation → Python → Interpretation → Challenge.

| Folder | Contents |
|---|---|
| 01_Presentations | Trainer deck (full speaker notes + answers in notes), Student deck (revision notes, no in-class answers) |
| 02_Trainer_Material | Trainer handbook (topics A–J, derivations, timing), Final-challenge answer key |
| 03_Jupyter_Notebooks | Student exercises A1–A11 (TODOs), Trainer solutions (executed) |
| 04_Datasets | 4 synthetic CSVs + Dataset Dictionary |
| 05_Student_Material | Lab guide, Final challenge brief |
| 06_Assessments | Concept checks (25 questions + answer key) |
| 07_Supporting_Files | Session plan, requirements, references, validation report |

## Quick start
1. `pip install -r 07_Supporting_Files/requirements.txt`
2. Open Jupyter in `03_Jupyter_Notebooks/` and run the setup cell (it finds `../04_Datasets`).
3. Keep the folder structure intact.

## Schedule (assumed 09:00–17:15)
| Hour | Time | Topic |
|---|---|---|
| 1 | 09:00–10:00 | Simple Linear Regression |
| 2 | 10:00–11:00 | OLS & Gradient Descent |
| — | 11:00–11:15 | Break |
| 3 | 11:15–12:15 | Evaluation & Multiple Regression |
| 4 | 12:15–13:15 | Polynomial, Bias–Variance, Ridge/Lasso intro |
| — | 13:15–14:00 | Lunch |
| 5 | 14:00–15:00 | Guided Lab 1 (A1–A7) |
| 6 | 15:00–16:00 | Guided Lab 2 (A8–A10) |
| — | 16:00–16:15 | Break |
| 7 | 16:15–17:15 | Final challenge (A11) & wrap-up |

All data are synthetic. Not covered today: Logistic Regression, classification metrics, Elastic Net, stepwise regression.
