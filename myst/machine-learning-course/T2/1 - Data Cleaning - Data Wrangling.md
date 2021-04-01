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

# 1 - Data Cleaning - Data Wrangling

+++

## Data Wrangling

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
mainpath = '/workspaces/machine-learning-course/data/python-ml-course/datasets'
folder = '/customer-churn-model'

data = pd.read_csv(mainpath + folder + '/Customer Churn Model.txt')
```

```{code-cell} ipython3
data.head()
```

# Crear un subconjunto de datos

```{code-cell} ipython3
data["Account Length"]
```

```{code-cell} ipython3
data[["Account Length","Phone","Eve Charge","Day Calls"]]
```

```{code-cell} ipython3
desired_columns = ["Account Length","Phone","Eve Charge","Day Calls"]
all_columns_list = data.columns.values.tolist()
```

```{code-cell} ipython3
sublist = [x for x in all_columns_list if x not in desired_columns]
sublist
```

```{code-cell} ipython3
a = set(desired_columns)
b = set(all_columns_list)
sublist = b-a
sublist = list(sublist)
sublist
```

```{code-cell} ipython3
data[6:10]
```

## Filter

```{code-cell} ipython3
data[data["Day Mins"]>350]
```

```{code-cell} ipython3
data[data["State"] == 'NY'].head()
```

```{code-cell} ipython3
data[(data["Day Mins"]>300) & (data["State"] == 'NY')].head()
```

```{code-cell} ipython3
data[(data["Day Mins"]>300) & (data["State"] == 'NY')].head()
```

```{code-cell} ipython3
data[data["Day Calls"] < data["Night Calls"]].shape
```

```{code-cell} ipython3
data[data["Day Mins"] < data["Night Mins"]].shape
```

```{code-cell} ipython3
data[["Day Mins","Night Mins","Account Length"]][:49].head()
```

```{code-cell} ipython3
data.iloc[:3, 3:6]
```

```{code-cell} ipython3
data.iloc[:3, [2,5,6]]
```

```{code-cell} ipython3
data.loc[[1,4,8,36],["Day Mins","Night Mins","Account Length"]]
```

## New columns

```{code-cell} ipython3
data["Total Mins"] = data["Night Mins"] + data["Day Mins"] + data["Eve Mins"]
```

```{code-cell} ipython3
data[["Total Mins", "State", "Night Mins", "Day Mins", "Eve Mins"]].head()
```

## Generación de números aleatorios

```{code-cell} ipython3
import numpy as np
```

```{code-cell} ipython3
np.random.randint(1,100)
```

```{code-cell} ipython3
np.random.random()
```

```{code-cell} ipython3
def random_list(n,a,b):
    """Generta una lista de números aleatorios enteros entre a y b"""
    return [np.random.randint(a,b) for i in range(n)]
```

```{code-cell} ipython3
random_list(8,2,20)
```

```{code-cell} ipython3
import random
```

```{code-cell} ipython3
[random.randrange(0,100,7)/7 for i in range(10)]
```

## Shuffling

```{code-cell} ipython3
arr = np.arange(100)
```

```{code-cell} ipython3
np.random.shuffle(arr)
arr
```

```{code-cell} ipython3
np.random.choice(data.columns.values.tolist())
```

## Seed
