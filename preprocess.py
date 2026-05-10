import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(filepath='aquamarine_dataset.xlsx'):
    df = pd.read_excel(filepath)
    feature_cols = ['Cs_ppm', 'Li_ppm', 'Sc_ppm', 'Ga_ppm', 'Fe_ppm', 'Mg_ppm', 'Na_ppm']
    X = df[feature_cols].copy()
    y = df['Deposit']
    X_log = np.log(X)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_log)
    return X_scaled, y, scaler, df
