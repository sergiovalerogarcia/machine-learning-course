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

# 2 - Pre Analisys

```{code-cell} ipython3
import pandas as pd
import os
mainpath = '/workspaces/machine-learning-course/data/python-ml-course/datasets'
folder = '/titanic'
```

```{code-cell} ipython3
data = pd.read_csv(mainpath + folder + '/titanic3.csv')
```

## Resumen de los datos

```{code-cell} ipython3
data.head()
```

```{code-cell} ipython3
data.shape
```

```{code-cell} ipython3
data.tail()
```

```{code-cell} ipython3
data.columns.values
```

**Resumen de estadísticos básicos**

```{code-cell} ipython3
data.describe()
```

```{code-cell} ipython3
data.dtypes
```

## Missing values

```{code-cell} ipython3
pd.isnull(data['body']).values.ravel().sum()
```

```{code-cell} ipython3
pd.notnull(data['body']).values.ravel().sum()
```

**Los valores que faltan en un dataset pueden venir por dos razones:**
* Por la extracción de los datos
* Por la recoleción de los datos

+++

### Borrado de valores que faltan

```{code-cell} ipython3
len(data)
```

```{code-cell} ipython3
data_drop = data.dropna(axis=0,how="any")
len(data_copy)
```

### Cómputo de los calores faltantes

```{code-cell} ipython3
data_fill = data.fillna(0)
data_fill.head()
```

```{code-cell} ipython3
data_fill = data.fillna("desconocido")
data_fill.head()
```

```{code-cell} ipython3
data_fill = data.copy()
data_fill["body"] = data["body"].fillna(0)
data_fill.head()
```

```{code-cell} ipython3
data_fill = data.copy()
data_fill["home.dest"] = data["home.dest"].fillna("Desconocido")
data_fill.head()
```

```{code-cell} ipython3
pd.isnull(data["age"]).values.ravel().sum()
```

```{code-cell} ipython3
data_fill = data.copy()
data_fill["age"] = data["age"].fillna(data["age"].mean())
data_fill.head(20)
```

```{code-cell} ipython3
data["age"][15]
```

```{code-cell} ipython3
data_fill = data.copy()
data_fill["age"] = data["age"].fillna(method="backfill")
data_fill["age"][15]
```

```{code-cell} ipython3
data_fill = data.copy()
data_fill["age"] = data["age"].fillna(method="ffill")
data_fill["age"][15]
```

### Variables dummy

```{code-cell} ipython3
pd.DataFrame(
    data["sex"].unique(), 
    columns=["sex"]
)
```

```{code-cell} ipython3
dummy_sex = pd.get_dummies(data["sex"], prefix="sex")
```

```{code-cell} ipython3
dummy_sex.head()
```

```{code-cell} ipython3
column_name = data.columns.values.tolist()
column_name
```

```{code-cell} ipython3
data_with_dummy = data.copy()
data_with_dummy.drop(["sex"], axis = 1)
data_with_dummy = pd.concat([data_with_dummy, dummy_sex], axis = 1)
data_with_dummy
```

```{code-cell} ipython3
def createDummies(df, var_name):
    dummy_var = pd.get_dummies(data[var_name], prefix=var_name)
    data_with_dummy = df.copy()
    data_with_dummy = data_with_dummy.drop([var_name], axis = 1)
    data_with_dummy = pd.concat([data_with_dummy, dummy_var], axis = 1)
    return data_with_dummy
```

```{code-cell} ipython3
data_with_dummy_using_function = createDummies(data, "sex")
data_with_dummy_using_function
```
