# Proyecto de Procesamiento Numérico: Estudio de la Dispersión de Ácido Acético

## Visión General del Proyecto

Este proyecto fue desarrollado para el curso de Procesamiento Numérico de la **Universidad Tecnológica de Bolívar** (NRC: 2312). El objetivo principal es aplicar métodos de integración numérica (Trapecio y Simpson) para calcular la **Masa Total Dispersada** de vapor de ácido acético en un ambiente controlado, analizando el impacto de la reducción de datos y la malla no uniforme en la precisión de los resultados.


## Objetivos de la Sección de Integración

1.  **Cálculo de Referencia:** Determinar el valor de la integral del conjunto original de **31 datos** Referencia approx 67.97$).
2.  **Reducción de Datos:** Eliminar **6 datos** distribuidos homogéneamente del conjunto original (31 to 25), generando una **malla no uniforme** (paso h variable entre 0.2m  y 0.4m).
3.  **Análisis de Sensibilidad:** Comparar los resultados de la integral del conjunto reducido (N=25) contra la referencia (N=31) para determinar la afectación de la reducción y la no uniformidad.


## Metodología Numérica y Hallazgos Clave

El análisis se centró en la adaptación de los métodos de integración a una malla no uniforme.

### 1. El Dilema de la Malla No Uniforme

La eliminación de 6 datos rompió la uniformidad de la malla. Las funciones clásicas de Simpson requieren que el paso $h$ sea constante.

| Método          | Referencia (31 Pts) | Reducido (25 Pts) | Error Relativo | Conclusión                 |
| **Trapecio**    | 67.968650           | 67.968630         | **$0.00003%**  | **Funciona perfectamente** |
| **Simpson 1/3** | 67.964273           | 56.678580         | **$16.60%**    | **Fallo Metodológico**     |
| **Simpson 3/8** | 67.9284675          | 56.396543         | **$16.98%**    | **Fallo Metodológico**     |

### 2. Conclusiones del Análisis

El resultado demuestra que la elección del método es más crítica que la reducción de datos:

* **Éxito del Trapecio:** El método del Trapecio compuesto, implementado para calcular el área por segmento (h variable), se adaptó correctamente a la malla no uniforme. La afectación fue nula.
* **Fallo de Simpson:** La implementación de las reglas clásicas de Simpson (asumiendo h constante) en una malla no uniforme genera un **error de truncamiento del 17%**, demostrando que el algoritmo es incompatible con este tipo de datos.


## 📝 Respuestas a Preguntas de Análisis

### A. ¿Qué tanto se afectaron los resultados de las integrales?

La afectación fue dual. El método **Trapecio** demostró una afectación **nula** ( 0.001%), confirmando que la función es extremadamente suave y que los 6 datos eran redundantes. Sin embargo, los métodos de **Simpson** mostraron una afectación **severa** (aprox. 17%), debido a un error metodológico al aplicarlos a una malla con paso h variable.

### B. ¿Cree usted que estos resultados se pueden generalizar para todas las integrales numéricas?

**No.** Estos resultados no son generalizables. La razón por la que el Trapecio funcionó tan bien es la **suavidad extrema** de la curva de concentración de ácido acético. Si los datos provinieran de un proceso volátil (ej. señales con ruido o picos), el aumento de h (de 0.2m a 0.4m) habría amplificado el error del Trapecio, y el fallo de Simpson sería aún más catastrófico.

### C. ¿Qué determina el porcentaje de afectación de los resultados de las integrales?

El factor determinante fue la **compatibilidad del algoritmo con la malla**:

1.  **Compatibilidad Metodológica:** El método de integración (Trapecio vs. Simpson clásico) fue el factor principal. Un algoritmo que se adapta a h variable (Trapecio) es robusto; uno que requiere h constante (Simpson clásico) fallará en la reducción de datos con remoción no uniforme.
2.  **Suavidad de la Curva:** La baja curvatura de f(x) mantuvo el error del Trapecio casi a cero, a pesar de la duplicación del paso h en algunas zonas.
