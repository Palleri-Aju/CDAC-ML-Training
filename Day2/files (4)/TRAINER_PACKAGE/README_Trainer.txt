TRAINER PACKAGE - DAY 02 (do not distribute to students)

FILES
  01_Day02_Training_Presentation_with_Trainer_Notes.pptx  Same 60 slides as the student deck + detailed speaker notes
  03_Trainer_Exercise_Key.docx    Sections A-H: objectives and slide map, dataset and defects, every solution, exact TODO table,
                                  quiz answers with slide numbers, troubleshooting, rubric/model answers, delivery notes
  05_Day02_Trainer_Solution.ipynb Fully solved notebook, executed from a fresh kernel (outputs saved); each exercise explains
                                  syntax, purpose and interpretation
  06_titanic_data_dirty.csv       Classroom dataset (keep it next to the solution notebook to re-run it)
  07_Data_Dictionary.xlsx         Same dictionary students receive
  Trainer_Data_Quality_Manifest.csv  Every injected/natural issue with counts computed from the CSV (raw and after exact dedup)
  Trainer_Session_Timing.xlsx     Slide-to-time map, hour plan and formula checks (420 min = 180 theory + 120 lab + 120 self-learning)
  Titanic_Original_Source.csv     The authentic public Titanic table (891 rows), preserved unchanged
  requirements.txt                Python libraries

DATASET
  06_titanic_data_dirty.csv = seeded sample (seed 20261024) of 600 authentic rows + 10 exact duplicates + 6 conflicting repeated-ID
  rows, with injected defects. Every manifest count was computed from the CSV and cross-checked against the generator's log.

VERIFICATION (what was run)
  - Solution notebook executed end to end on pandas 3.0.2 / scikit-learn 1.8.0 and on pandas 2.2.3 / scikit-learn 1.9.1.
  - Each blank filled with its answer reproduces the solution code; the student notebook fails at the first blank as designed.
  - Both decks have identical slides; the student deck has no speaker notes.

DELIVERY
  Hour 1-3: slides 1-39 (checks at 13, 23, 38; predict-then-reveal at 5-6, 25-26, 30-31). Hour 4: slides 40-43.
  Hour 5: slides 44-49. Hour 6: slides 50-54. Hour 7: slides 55-60. See the timing workbook for minutes per slide.
  Do not show the Trainer Key or the solution notebook to students before they attempt the exercises.
