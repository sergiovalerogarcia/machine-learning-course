# T1 - 3 - Data Cleaning - Plots

import pandas as pd
import math
import os
import matplotlib.pyplot as plt

mainpath = '/workspaces/machine-learning-course/data/python-ml-course/datasets'
folder = '/customer-churn-model'

data = pd.read_csv(mainpath + folder + '/Customer Churn Model.txt')

data.head()

%matplotlib inline

#savefig("/workspaces/machine-learning-course/data/figs")

## Scatter Plot

data.plot(kind="scatter", x="Day Mins", y="Day Charge")

data.plot(kind="scatter", x="Night Mins", y="Night Charge")

figure, axs = plt.subplots(2,2, sharey=True, sharex=True)
data.plot(kind="scatter", x="Day Mins", y="Day Charge", ax=axs[0][0])
data.plot(kind="scatter", x="Day Calls", y="Day Charge", ax=axs[0][1])
data.plot(kind="scatter", x="Night Mins", y="Night Charge", ax=axs[1][0])
data.plot(kind="scatter", x="Night Calls", y="Night Charge", ax=axs[1][1])

## Histogramas de frecuencia

sturges_rule_bins = 1 + math.log(len(data), 2)
sturges_rule_bins = round(sturges_rule_bins)
sturges_rule_bins

plt.hist(data["Day Calls"], bins = sturges_rule_bins)
plt.xlabel("Número de llamadas al día")
plt.ylabel("Frecuencia")
plt.title("Hisograma de número de llamadas al día")

## Boxplot, diagrama de caja y bigotes

plt.boxplot(data["Day Calls"])
plt.ylabel("Número de llamadas al día")
plt.title("Boxplot de las llamadas diarias")

data["Day Calls"].mode()

data["Day Calls"].mean()

data["Day Calls"].median()

data["Day Calls"].describe()

### Bigotes

IQR=data["Day Calls"].quantile(0.75)-data["Day Calls"].quantile(0.25)
IQR

data["Day Calls"].quantile(0.25) - 1.5*IQR

data["Day Calls"].quantile(0.75) + 1.5*IQR

plt.boxplot(data[["Day Calls", "Night Calls"]])