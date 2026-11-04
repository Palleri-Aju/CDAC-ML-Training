TRAINER PACKAGE - DAY 01 (do not distribute to students)

FILES
  03_Trainer_Exercise_Key.docx   Objectives, dataset explanation, per-exercise solutions and verified results,
                                 all notebook blank answers, quiz answers (with slide numbers), troubleshooting, rubric
  05_Day01_Trainer_Solution.ipynb  Fully solved notebook, executed from a fresh kernel (outputs saved)
  Trainer_Data_Quality_Manifest.csv  True defect counts, computed from the CSV (raw rows and after exact de-duplication)
  Trainer_Session_Timing.xlsx    Slide-to-time map (240 min theory + 180 min lab) with formula checks
  01_Day01_Training_Presentation_with_Trainer_Notes.pptx  Same 65 slides as the student deck, with full speaker notes
  The student package also needs 06_customer_data_dirty.csv; copy it next to the solution notebook to re-run it.

NOTES
  - Exercise numbering: B4 = detect invalid/suspicious values; B8 = impute missing numbers (so that duplicates and
    impossible values are handled before any median is computed).
  - Counts differ between "raw" (460 rows) and "after exact dedup" (448 rows); see the manifest columns.
  - The student presentation has its lab-slide notes removed; all theory-slide notes and answers are kept.
  - Tested on pandas 3.0.2 and pandas 2.2.3 (scikit-learn 1.8 / 1.9).
