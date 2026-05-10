import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from preprocess import load_and_preprocess

X, y, scaler, df = load_and_preprocess()

rf = RandomForestClassifier(n_estimators=500, max_features=3, min_samples_leaf=5, random_state=42, n_jobs=-1)

cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_val_score(rf, X, y, cv=cv, scoring='accuracy')
print(f'10‑fold CV accuracy: {scores.mean():.3f} ± {scores.std():.3f}')

rf.fit(X, y)
importances = rf.feature_importances_
feature_names = ['Cs', 'Li', 'Sc', 'Ga', 'Fe', 'Mg', 'Na']
importance_df = pd.DataFrame({'feature': feature_names, 'importance': importances})
print(importance_df.sort_values('importance', ascending=False))
