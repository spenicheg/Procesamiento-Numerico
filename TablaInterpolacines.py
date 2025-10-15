import pandas as pd
import numpy as np

def lagrange_interpolation(x_points, y_points, x_eval):
    total = 0
    n = len(x_points)
    for i in range(n):
        xi, yi = x_points[i], y_points[i]
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x_eval - x_points[j]) / (x_points[i] - x_points[j])
        total += yi * Li
    return total


df = pd.read_excel("Proyecto procesamiento.xlsx", sheet_name="Datos")
df.columns = df.columns.str.strip().str.replace('\n', '', regex=True)
df['x'] = pd.to_numeric(df['x'], errors='coerce')
df['y'] = pd.to_numeric(df['y'], errors='coerce')

n = len(df)

for grado in range(1, 5):
    df[f'Interpolación grado {grado}'] = np.nan


for i in range(n):
    xi = df.loc[i, 'x']

    if 0 < i < n - 1:
        x_pts = [df.loc[i - 1, 'x'], df.loc[i + 1, 'x']]
        y_pts = [df.loc[i - 1, 'y'], df.loc[i + 1, 'y']]
        df.loc[i, 'Interpolación grado 1'] = lagrange_interpolation(x_pts, y_pts, xi)

    if i > 1 and i < n - 1:
        x_pts = [df.loc[i - 2, 'x'], df.loc[i - 1, 'x'], df.loc[i + 1, 'x']]
        y_pts = [df.loc[i - 2, 'y'], df.loc[i - 1, 'y'], df.loc[i + 1, 'y']]
        df.loc[i, 'Interpolación grado 2'] = lagrange_interpolation(x_pts, y_pts, xi)

    if i > 2 and i < n - 1:
        x_pts = [df.loc[i - 3, 'x'], df.loc[i - 2, 'x'], df.loc[i - 1, 'x'], df.loc[i + 1, 'x']]
        y_pts = [df.loc[i - 3, 'y'], df.loc[i - 2, 'y'], df.loc[i - 1, 'y'], df.loc[i + 1, 'y']]
        df.loc[i, 'Interpolación grado 3'] = lagrange_interpolation(x_pts, y_pts, xi)

    if i > 2 and i < n - 2:
        x_pts = [df.loc[i - 3, 'x'], df.loc[i - 2, 'x'], df.loc[i - 1, 'x'],
                 df.loc[i + 1, 'x'], df.loc[i + 2, 'x']]
        y_pts = [df.loc[i - 3, 'y'], df.loc[i - 2, 'y'], df.loc[i - 1, 'y'],
                 df.loc[i + 1, 'y'], df.loc[i + 2, 'y']]
        df.loc[i, 'Interpolación grado 4'] = lagrange_interpolation(x_pts, y_pts, xi)


df.to_excel("tabla_lagrange_final.xlsx", index=False)
print("Archivo guardado como 'tabla_lagrange_final.xlsx'")
