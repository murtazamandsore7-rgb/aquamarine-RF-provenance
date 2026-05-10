# Aquamarine provenance classification using Random Forest

This repository contains the code and data for the paper:

**Random Forest approach to geochemical exploration and deposit‑specific fingerprinting of aquamarine: A case study of Pakistan, Brazil, Nigeria, and Afghanistan**  
*Murtaza Aqeel, Applied Geochemistry (2026)*

## Contents
- `aquamarine_dataset.xlsx` – Complete LA‑ICP‑MS/EPMA dataset (1,287 specimens, 13 deposits)
- `preprocess.py` – Data loading, log‑ratio transform, autoscaling
- `rf_model.py` – Random Forest training, cross‑validation, feature importance
- `confusion_matrix.py` – Generate confusion matrix from cross‑validation
- `figure_s1_pca.py` – PCA plot coloured by laboratory (Supplementary Fig. S1)
- `figure_s2_learning_curve.py` – Learning curve (Supplementary Fig. S2)
- `figure_s3_shap.py` – SHAP summary plot (Supplementary Fig. S3)
- `requirements.txt` – Python dependencies

## Requirements
```bash
pip install -r requirements.txt

## Usage
python rf_model.py
python figure_s1_pca.py

## Results
- Deposit‑level accuracy: 82.8% (±2.3%) from 10‑fold cross‑validation
- Robust provenance indicators: Cs, Sc, Ga (heat‑resistant)
- Decision tree thresholds...
