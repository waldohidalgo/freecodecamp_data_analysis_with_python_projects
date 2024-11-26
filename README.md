# Data Analysis with Python Projects

Repositorio con el código solución a los 5 proyectos requisitos obligatorios para obtener la [Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/)

Hasta la fecha llevo realizado: Proyecto 1. A medida que vaya realizando el resto de proyectos los iré subiendo a este repositorio.

## Listado de Proyectos

### 1- Mean-Variance-Standard Deviation Calculator

#### 1.1- Proyecto Aprobado

![Primer Proyecto Aprobado](./Proyecto1_Mean-Variance-StandardDeviationCalculator/passed.webp)

#### 1.2- Todos los tests superados

![All tests passed](./Proyecto1_Mean-Variance-StandardDeviationCalculator/all_tests_passed.webp)

#### 1.3- Código Creado

```py
import numpy as np

def calculate(list):
    n=len(list)
    if n<9:
        raise ValueError("List must contain nine numbers.")

    orig=np.array(list)
    reorg=orig.reshape(3,3)
    mean=[np.mean(reorg,axis=0).tolist(),np.mean(reorg,axis=1).tolist(),np.mean(reorg)]
    variance=[np.var(reorg,axis=0).tolist(),np.var(reorg,axis=1).tolist(),np.var(reorg)]
    std=[np.std(reorg,axis=0).tolist(),np.std(reorg,axis=1).tolist(),np.std(reorg)]
    maxv=[np.max(reorg,axis=0).tolist(),np.max(reorg,axis=1).tolist(),np.max(reorg)]
    minv=[np.min(reorg,axis=0).tolist(),np.min(reorg,axis=1).tolist(),np.min(reorg)]
    sumv=[np.sum(reorg,axis=0).tolist(),np.sum(reorg,axis=1).tolist(),np.sum(reorg)]

    calculations={
        'mean':mean,
        'variance':variance,
        'standard deviation':std,
        'max':maxv,
        'min':minv,
        'sum':sumv
    }

    return calculations
```
