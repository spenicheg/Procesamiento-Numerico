import numpy as np

# 1) Datos (25 puntos)
x = [0,0.2,0.4,0.6,1.0,1.2,1.4,1.6,2.0,2.2,2.4,2.6,3.0,3.2,3.4,3.6,4.0,4.2,4.4,4.6,5.0,5.2,5.4,5.6,6.0]
C = [35.8026,33.7706,31.7389,29.707,25.6435,23.6116,21.5799,19.5479,15.4842,13.4525,10.963,9.3888,7.5133,6.5756,5.6378,4.7001,2.8246,1.8868,0.4571,0.0113,0.0089,0.0076,0.0062,0.0049,0.0025]

h_nominal = 0.2

# 2) Trapecio
def trapecio(x, y):
    total = 0
    for i in range(len(x)-1):
        h = x[i+1] - x[i]
        total += h * (y[i] + y[i+1]) / 2
    return total

# 3) Simpson 1/3
def simpson_1_3_corregido(y, h):
    n = len(y) - 1
    if n % 2 != 0:
        raise ValueError("Simpson 1/3 requiere número de intervalos par")

    suma4 = sum(y[i] for i in range(1, n, 2))
    suma2 = sum(y[i] for i in range(2, n, 2))
    
    return (h/3) * (y[0] + y[-1] + 4*suma4 + 2*suma2)

# 4) Simpson 3/8
def simpson_3_8_corregido(y, h):
    n = len(y) - 1
    if n % 3 != 0:
        raise ValueError("Simpson 3/8 requiere múltiplo de 3")

    suma3 = 0
    suma2 = 0
    for i in range(1, n):
        if i % 3 == 0:
            suma2 += y[i]
        else:
            suma3 += y[i]

    return (3*h/8) * (y[0] + y[-1] + 3*suma3 + 2*suma2)

I_trap = trapecio(x, C)
I_s13  = simpson_1_3_corregido(C, h_nominal)
I_s38  = simpson_3_8_corregido(C, h_nominal)

print("\nRESULTADOS:")
print(f"Trapecio (h variable):   {I_trap:.6f}")
print(f"Simpson 1/3 (h=0.2):     {I_s13:.6f}")
print(f"Simpson 3/8 (h=0.2):     {I_s38:.6f}")
