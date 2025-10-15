import pandas as pd
import numpy as np

def lagrange_interpolation(x_points, y_points, x_eval):
    n = len(x_points)
    total = 0
    for i in range(n):
        xi, yi = x_points[i], y_points[i]
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x_eval - x_points[j]) / (x_points[i] - x_points[j])
        total += yi * Li
    return total

df = pd.read_excel("Proyecto procesamiento.xlsx", sheet_name="Datos")
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace('\n', '', regex=True)

x_col = 'Esfuerzo (MPa)'
y_col = 'Deformación (%)'

df[x_col] = pd.to_numeric(df[x_col], errors='coerce')
df[y_col] = pd.to_numeric(df[y_col], errors='coerce')

df["Interpolación grado 4"] = np.nan
df["Error verdadero"] = np.nan
df["Error relativo (%)"] = np.nan

n = len(df)

for i in range(n):
    if i > 1 and i < n - 2:
        indices = [i-2, i-1, i+1, i+2]
        if all(0 <= idx < n for idx in indices):
            x_pts = [df.loc[idx, x_col] for idx in indices]
            y_pts = [df.loc[idx, y_col] for idx in indices]
            xi = df.loc[i, x_col]

            y_inter = lagrange_interpolation(x_pts, y_pts, xi)
            df.loc[i, "Interpolación grado 4"] = y_inter

            y_real = df.loc[i, y_col]
            et = y_real - y_inter
            et_rel = abs(100 * et / y_real)
            df.loc[i, "Error verdadero"] = et
            df.loc[i, "Error relativo (%)"] = et_rel


error_promedio = df["Error relativo (%)"].mean(skipna=True)

fila_prom = pd.DataFrame({
    x_col: ["—"],
    y_col: ["—"],
    "Interpolación grado 4": ["—"],
    "Error verdadero": ["—"],
    "Error relativo (%)": [error_promedio]
})
df_final = pd.concat([df, fila_prom], ignore_index=True)

df_final.to_excel("tabla_interpolacion_grado4_con_errores.xlsx", index=False)
print("Archivo generado: tabla_interpolacion_grado4_con_errores.xlsx")
print(f"Error relativo promedio: {error_promedio:.4f}%")

"""Tabla interpolaciones"""

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

x_col = 'Esfuerzo (MPa)'
y_col = 'Deformación (%)'

df[x_col] = pd.to_numeric(df[x_col], errors='coerce')
df[y_col] = pd.to_numeric(df[y_col], errors='coerce')

n = len(df)

for grado in range(1, 5):
    df[f'Interpolación grado {grado}'] = np.nan


for i in range(n):
    xi = df.loc[i, x_col]

    if 0 < i < n - 1:
        x_pts = [df.loc[i - 1, x_col], df.loc[i + 1, x_col]]
        y_pts = [df.loc[i - 1, y_col], df.loc[i + 1, y_col]]
        df.loc[i, 'Interpolación grado 1'] = lagrange_interpolation(x_pts, y_pts, xi)

    if i > 1 and i < n - 1:
        x_pts = [df.loc[i - 2, x_col], df.loc[i - 1, x_col], df.loc[i + 1, x_col]]
        y_pts = [df.loc[i - 2, y_col], df.loc[i - 1, y_col], df.loc[i + 1, y_col]]
        df.loc[i, 'Interpolación grado 2'] = lagrange_interpolation(x_pts, y_pts, xi)

    if i > 2 and i < n - 1:
        x_pts = [df.loc[i - 3, x_col], df.loc[i - 2, x_col], df.loc[i - 1, x_col], df.loc[i + 1, x_col]]
        y_pts = [df.loc[i - 3, y_col], df.loc[i - 2, y_col], df.loc[i - 1, y_col], df.loc[i + 1, y_col]]
        df.loc[i, 'Interpolación grado 3'] = lagrange_interpolation(x_pts, y_pts, xi)

    if i > 2 and i < n - 2:
        x_pts = [df.loc[i - 3, x_col], df.loc[i - 2, x_col], df.loc[i - 1, x_col],
                 df.loc[i + 1, x_col], df.loc[i + 2, x_col]]
        y_pts = [df.loc[i - 3, y_col], df.loc[i - 2, y_col], df.loc[i - 1, y_col],
                 df.loc[i + 1, y_col], df.loc[i + 2, y_col]]
        df.loc[i, 'Interpolación grado 4'] = lagrange_interpolation(x_pts, y_pts, xi)


df.to_excel("tabla_lagrange_final.xlsx", index=False)
print("Archivo guardado como 'tabla_lagrange_final.xlsx'")