---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 2 - Funciones de distribución de probabilidades

```{code-cell} ipython3
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
```

## Distribución uniforme

```{code-cell} ipython3
a=1
b=100
n=200000
data_uniform = np.random.uniform(a,b,n)
```

```{code-cell} ipython3
%matplotlib inline
```

```{code-cell} ipython3
plot = plt.hist(data_uniform, bins=200)
```

## Distribución normal

```{code-cell} ipython3
data_normal = np.random.randn(1000000)
```

```{code-cell} ipython3
plt.plot(data_normal)
```

```{code-cell} ipython3
plt.hist(data_normal, bins=30)
```

```{code-cell} ipython3
plt.plot(x,sorted(data_normal))
```

```{code-cell} ipython3
mu = 5.5
sd = 2.5
z_10000 = np.random.randn(10000)
data_normal_with_mu_sd =  mu + sd * z_10000
```

```{code-cell} ipython3
plt.hist(data_normal_with_mu_sd, bins=30)
```

```{code-cell} ipython3
np.random.randn(2,4)
```

## La simulación de Monte Carlo

+++

1. Generamos 2 números aleatorios uniforme entre 0 y 1 en total 1000 veces
2. Calcularemos x^2 + y^2
    * Si el valor es inferior a 1 estamos dentro del círculo
    * Si el calor es superior a 1 estamos fuera del círculo
3. Calculamos el número total de veces que están dentro del círculo y lo dividimos entre el número total de intentos para obtener una aproximación de la probabilidad de caer dentro del círculo
4. Usamos dicha probabilidad para aproximar el valor de pi
5. Repetimos el experimento un número suficiente de veces para obtener (100) diferentes aproximaciones de pi
6. Calculamos el promedio de los 1000 experimentos anterior para dar un valor final de pi

```{code-cell} ipython3
def pi_montecarlo(n, n_exp):
    pi_avg = 0
    pi_value_list = []
    for i in range(n_exp):
        value = 0
        x = np.random.uniform(0,1,n).tolist()
        y = np.random.uniform(0,1,n).tolist()
        for j in range(n):
            z = np.sqrt(x[j] * x[j] + y[j] * y[j])
            if z<=1:
                value += 1
        float_value = float(value)
        pi_value = float_value * 4 / n
        pi_value_list.append(pi_value)
        pi_avg += pi_value

    pi = pi_avg/n_exp

    print(pi)
    fig = plt.plot(pi_value_list)
    return (pi, fig)
```

```{code-cell} ipython3
pi_montecarlo(10000, 200)
```

## Dummy Data Sets

```{code-cell} ipython3
n = 100000
data = pd.DataFrame({
    'A': np.random.randn(n),
    'B': 1.5 + 2.5 * np.random.randn(n),
    'C': np.random.uniform(5,32,n)
})
```

```{code-cell} ipython3
data.head()
```

```{code-cell} ipython3
data.describe()
```

```{code-cell} ipython3
plt.hist(data['A'])
```
