import pandas as pd
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from preprocess import load_and_preprocess

X, y, _, _ = load_and_preprocess()
rf = RandomForestClassifier(n_estimators=500, max_features=3, min_samples_leaf=5, random_state=42)
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
y_pred = cross_val_predict(rf, X, y, cv=cv)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y, y_pred, labels=rf.classes_)
cm_df = pd.DataFrame(cm, index=rf.classes_, columns=rf.classes_)
cm_df.to_csv('confusion_matrix.csv')
print("Confusion matrix saved to confusion_matrix.csv")
