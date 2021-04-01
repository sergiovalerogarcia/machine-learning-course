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

# T1 - 0 - Read data

```{code-cell} ipython3
import pandas as pd
import os
mainpath = '/workspaces/machine-learning-course/data/python-ml-course/datasets'
folder = '/titanic'
```

```{code-cell} ipython3
os.listdir(mainpath + folder)
```

## Read csv

```{code-cell} ipython3
data = pd.read_csv(mainpath + folder + '/titanic3.csv')
```

```{code-cell} ipython3
data.head()
```

## Change column names based on file

```{code-cell} ipython3
data2 = pd.read_csv(mainpath + '/customer-churn-model' + '/Customer Churn Model.txt')
```

```{code-cell} ipython3
data2.columns.values
```

```{code-cell} ipython3
data_cols = pd.read_csv(mainpath + '/customer-churn-model' + '/Customer Churn Columns.csv')
data_col_list = data_cols["Column_Names"].tolist()
data_col_list
data2 = pd.read_csv(mainpath + '/customer-churn-model' + '/Customer Churn Model.txt', skiprows=1,
                    header = None, names = data_col_list)
data2
```

## From url

```{code-cell} ipython3
medals_url = 'http://winterolympicsmedals.com/medals.csv'
```

```{code-cell} ipython3
medals_data = pd.read_csv(medals_url)
```

```{code-cell} ipython3
medals_data.head()
```

```{code-cell} ipython3
import csv
import urllib3
```

```{code-cell} ipython3
http = urllib3.PoolManager()
r = http.request('GET', medals_url)
```

```{code-cell} ipython3
cr = csv.reader(r.data)
```

## From xlsx

```{code-cell} ipython3
pd.read_excel(mainpath + '/titanic/titanic3.xls', 'titanic3')
```
