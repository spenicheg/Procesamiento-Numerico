import numpy as np
import pandas as pd

data = {
    'Toma': range(1, 26),
    'Distancia_m': [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 
                    2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8],
    'Concentracion_mg_m3': [0, 0.0012, 0.0025, 0.0037, 0.0049, 0.0062, 0.0076, 
                            0.0089, 0.0101, 0.0113, 0.4571, 1.8868, 2.8246, 
                            3.7623, 4.7001, 5.6378, 6.5756, 7.5133, 8.4511, 
                            9.3888, 10.963, 13.4525, 15.4842, 17.5162, 19.5479]
}

df = pd.DataFrame(data)


x = df['Distancia_m'].values
y = df['Concentracion_mg_m3'].values
n_datos = len(x)
n_segmentos = n_datos - 1


h = x[1] - x[0] 

print(f"Análisis de Integración Numérica")
print(f"Cantidad de datos: {n_datos}")
print(f"Segmentos (intervalos): {n_segmentos}")
print(f"Paso (h): {h:.2f} m")
print("-" * 40)

suma_trapecio = y[0] + y[-1] + 2 * np.sum(y[1:-1])
integral_trapecio = (h / 2) * suma_trapecio

if n_segmentos % 2 == 0:
    suma_s13 = y[0] + y[-1]
    suma_s13 += 4 * np.sum(y[1:-1:2]) 
    suma_s13 += 2 * np.sum(y[2:-1:2])
    integral_s13 = (h / 3) * suma_s13
else:
    integral_s13 = None
    print("Simpson 1/3 no aplicable (segmentos impares).")

if n_segmentos % 3 == 0:
    suma_s38 = y[0] + y[-1]
    for i in range(1, n_segmentos):
        if i % 3 == 0:
            suma_s38 += 2 * y[i] 
        else:
            suma_s38 += 3 * y[i] 
    integral_s38 = (3 * h / 8) * suma_s38
else:
    integral_s38 = None
    print("Simpson 3/8 no aplicable (segmentos no múltiplos de 3).")

print(f"RESULTADOS DE LA INTEGRAL (Masa acumulada o Exposición Espacial):")
print(f"a. Trapecio:    {integral_trapecio:.6f}")
if integral_s13 is not None:
    print(f"b. Simpson 1/3: {integral_s13:.6f}")
if integral_s38 is not None:
    print(f"c. Simpson 3/8: {integral_s38:.6f}")

print("-" * 40)
print("Diferencia relativa entre Trapecio y Simpson 1/3:")
diff = abs((integral_trapecio - integral_s13)/integral_s13)*100
print(f"Diferencia: {diff:.4f}%")