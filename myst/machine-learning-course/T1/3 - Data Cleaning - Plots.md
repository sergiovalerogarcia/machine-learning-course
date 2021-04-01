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

# 3 - Data Cleaning - Plots

```{code-cell} ipython3
import pandas as pd
import math
import os
import matplotlib.pyplot as plt

mainpath = '/workspaces/machine-learning-course/data/python-ml-course/datasets'
folder = '/customer-churn-model'

data = pd.read_csv(mainpath + folder + '/Customer Churn Model.txt')
```

```{code-cell} ipython3
data.head()
```

```{code-cell} ipython3
%matplotlib inline
```

```{code-cell} ipython3
#savefig("/workspaces/machine-learning-course/data/figs")
```

## Scatter Plot

```{code-cell} ipython3
data.plot(kind="scatter", x="Day Mins", y="Day Charge")
```

```{code-cell} ipython3
data.plot(kind="scatter", x="Night Mins", y="Night Charge")
```

```{code-cell} ipython3
figure, axs = plt.subplots(2,2, sharey=True, sharex=True)
data.plot(kind="scatter", x="Day Mins", y="Day Charge", ax=axs[0][0])
data.plot(kind="scatter", x="Day Calls", y="Day Charge", ax=axs[0][1])
data.plot(kind="scatter", x="Night Mins", y="Night Charge", ax=axs[1][0])
data.plot(kind="scatter", x="Night Calls", y="Night Charge", ax=axs[1][1])
```

## Histogramas de frecuencia

```{code-cell} ipython3
sturges_rule_bins = 1 + math.log(len(data), 2)
sturges_rule_bins = round(sturges_rule_bins)
sturges_rule_bins
```

```{code-cell} ipython3
plt.hist(data["Day Calls"], bins = sturges_rule_bins)
plt.xlabel("Número de llamadas al día")
plt.ylabel("Frecuencia")
plt.title("Hisograma de número de llamadas al día")
```

## Boxplot, diagrama de caja y bigotes

```{code-cell} ipython3
plt.boxplot(data["Day Calls"])
plt.ylabel("Número de llamadas al día")
plt.title("Boxplot de las llamadas diarias")
```

```{code-cell} ipython3
data["Day Calls"].mode()
```

```{code-cell} ipython3
data["Day Calls"].mean()
```

```{code-cell} ipython3
data["Day Calls"].median()
```

```{code-cell} ipython3
data["Day Calls"].describe()
```

### Bigotes

```{code-cell} ipython3
IQR=data["Day Calls"].quantile(0.75)-data["Day Calls"].quantile(0.25)
IQR
```

```{code-cell} ipython3
data["Day Calls"].quantile(0.25) - 1.5*IQR
```

```{code-cell} ipython3
data["Day Calls"].quantile(0.75) + 1.5*IQR
```

```{code-cell} ipython3
plt.boxplot(data[["Day Calls", "Night Calls"]])
```
