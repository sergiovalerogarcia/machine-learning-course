# T1 - 2 - Pre Analisys

import pandas as pd
import os
mainpath = '/workspaces/machine-learning-course/data/python-ml-course/datasets'
folder = '/titanic'

data = pd.read_csv(mainpath + folder + '/titanic3.csv')

## Resumen de los datos

data.head()

data.shape

data.tail()

data.columns.values

**Resumen de estadísticos básicos**

data.describe()

data.dtypes

## Missing values

pd.isnull(data['body']).values.ravel().sum()

pd.notnull(data['body']).values.ravel().sum()

**Los valores que faltan en un dataset pueden venir por dos razones:**
* Por la extracción de los datos
* Por la recoleción de los datos

### Borrado de valores que faltan

len(data)

data_drop = data.dropna(axis=0,how="any")
len(data_copy)

### Cómputo de los calores faltantes

data_fill = data.fillna(0)
data_fill.head()

data_fill = data.fillna("desconocido")
data_fill.head()

data_fill = data.copy()
data_fill["body"] = data["body"].fillna(0)
data_fill.head()

data_fill = data.copy()
data_fill["home.dest"] = data["home.dest"].fillna("Desconocido")
data_fill.head()

pd.isnull(data["age"]).values.ravel().sum()

data_fill = data.copy()
data_fill["age"] = data["age"].fillna(data["age"].mean())
data_fill.head(20)

data["age"][15]

data_fill = data.copy()
data_fill["age"] = data["age"].fillna(method="backfill")
data_fill["age"][15]

data_fill = data.copy()
data_fill["age"] = data["age"].fillna(method="ffill")
data_fill["age"][15]

### Variables dummy

pd.DataFrame(
    data["sex"].unique(), 
    columns=["sex"]
)

dummy_sex = pd.get_dummies(data["sex"], prefix="sex")

dummy_sex.head()

column_name = data.columns.values.tolist()
column_name

data_with_dummy = data.copy()
data_with_dummy.drop(["sex"], axis = 1)
data_with_dummy = pd.concat([data_with_dummy, dummy_sex], axis = 1)
data_with_dummy

def createDummies(df, var_name):
    dummy_var = pd.get_dummies(data[var_name], prefix=var_name)
    data_with_dummy = df.copy()
    data_with_dummy = data_with_dummy.drop([var_name], axis = 1)
    data_with_dummy = pd.concat([data_with_dummy, dummy_var], axis = 1)
    return data_with_dummy

data_with_dummy_using_function = createDummies(data, "sex")
data_with_dummy_using_function