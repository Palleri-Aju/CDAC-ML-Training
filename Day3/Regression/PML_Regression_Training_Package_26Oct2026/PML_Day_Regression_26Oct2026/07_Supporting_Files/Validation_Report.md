# Validation Report — PML Regression package (validated 25 Oct 2026)

| Area | Check | Result |
|---|---|---|
| Mathematics | Every worked example recomputed in Python (OLS 2.1/8.4, SSE 3.6, R² 0.98, adj. R² 0.9733; GD iterations 7.5 → 1.5098 → 0.3217; metrics on outlier example; Ridge/Lasso candidate tables; concept-check numericals B1–B5; challenge manual answers 54.81 and 2.5/7.5/2.739) | Pass |
| Mathematics | GD stability claim (α < 2/λmax ≈ 0.361) checked by eigenvalues and by running α = 0.3 (converges) and 0.37 (diverges) | Pass |
| Trainer notebook | Executed top-to-bottom with nbconvert inside the package layout (finds ../04_Datasets) | Pass — 0 errors, figures rendered |
| Student notebook | Generated from the same source as the solutions (each TODO block is the solution block in the trainer file); executed with `--allow-errors` | Only expected TODO errors (NameError/TypeError); 0 syntax errors; no answers leaked (checked programmatically) |
| Notebook ↔ docs | Figures quoted in the handbook, trainer key and deck taken from the executed notebook | Pass |
| Reproducibility | Fixed seeds: data 2610 / 42 / 7; splits random_state = 42 | Pass |
| Leakage | Scalers and polynomial expansion inside Pipelines; tuning via CV on training data; test set used once per final model | Pass (by design and review) |
| Trainer deck | OOXML validation; rendered all 69 slides via LibreOffice and visually inspected; overflow, code wrapping, title alignment fixed | Pass |
| Student deck | OOXML validation; rendered (69 slides); no answers present (0 "ANSWER" strings); 58 revision notes | Pass — spot-checked visually, not every slide re-inspected after final build |
| Word documents (5) | OOXML validation; handbook, concept checks and trainer key rendered and inspected | Pass — lab guide and challenge validated but only partially inspected visually |
| Session_Plan.xlsx | LibreOffice recalculation: 85 formulas, 0 errors; 420 instructional min = 7 h; contiguous 09:00–17:15 | Pass |
| Package | All files present; relative path ../04_Datasets verified by notebook execution | Pass |

## Known limitations
- Rendering checks used LibreOffice; fonts (Cambria/Calibri) are substituted there, so minor layout differences in PowerPoint/Word are possible.
- Handbook table of contents is a Word field: right-click → *Update field* on first open.
- The trainer deck is 69 slides (5 dividers + 6 discussion slides included), above the 45–60 guideline.
- Ridge/Lasso are introductory only; full derivations deferred to the next session as agreed.
