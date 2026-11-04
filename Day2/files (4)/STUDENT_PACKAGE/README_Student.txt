PRACTICAL MACHINE LEARNING - DAY 02 (CDAC Mumbai, PGCP-AI) - Saturday 24 October 2026
Data Preprocessing, Cleaning, Transformation and Pipelines

FILES
  01_Day02_Training_Presentation.pptx  Slides used in class (60 slides)
  02_Student_Exercise_Guide.docx       Guide to every exercise (no answers)
  04_Day02_Student_Exercise.ipynb      The notebook you complete (fill in the ____ blanks)
  06_titanic_data_dirty.csv            Classroom dataset. NEVER edit or overwrite it.
  07_Data_Dictionary.xlsx              Columns, valid ranges, business rules, category aliases
  requirements.txt                     Python libraries

INSTALL AND RUN
  Jupyter: pip install -r requirements.txt, then run "jupyter notebook" in this folder and open the notebook.
  Colab:   upload the notebook, then upload the CSV (the A1 cell can do it). Libraries are preinstalled.
  Keep the CSV in the same folder as the notebook. Run cells top to bottom (Shift+Enter).
  A cell containing ____ fails on purpose until you complete it. If something looks strange: Kernel > Restart and Run All.

HOW THE DAY WORKS (7 hours)
  Hours 1-3 theory | Hour 4 guided self-learning (SL1-SL3) | Hours 5-6 lab (A, B, C exercises)
  Hour 7 guided self-learning (C6, D1-D3, MC1-MC3, C7). Exercise IDs match the slides and the guide.

RAW DATA RULES
  Never change the raw CSV. Work on copies in the notebook. Do only rule-based fixes before the split;
  anything that learns a number from the data (median, scaler, categories) is fitted on training data only.

SUBMIT
  The completed notebook with all outputs visible (Restart and Run All), your decision log and reflection (C7).
  No model is trained today. Feature engineering, selection, PCA and t-SNE are Day 3.
