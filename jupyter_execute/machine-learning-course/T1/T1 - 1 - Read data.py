# T1 - 0 - Read data

import pandas as pd
import os
mainpath = '/workspaces/machine-learning-course/data/python-ml-course/datasets'
folder = '/titanic'

os.listdir(mainpath + folder)

## Read csv

data = pd.read_csv(mainpath + folder + '/titanic3.csv')

data.head()

## Change column names based on file

data2 = pd.read_csv(mainpath + '/customer-churn-model' + '/Customer Churn Model.txt')

data2.columns.values

data_cols = pd.read_csv(mainpath + '/customer-churn-model' + '/Customer Churn Columns.csv')
data_col_list = data_cols["Column_Names"].tolist()
data_col_list
data2 = pd.read_csv(mainpath + '/customer-churn-model' + '/Customer Churn Model.txt', skiprows=1,
                    header = None, names = data_col_list)
data2

## From url

medals_url = 'http://winterolympicsmedals.com/medals.csv'

medals_data = pd.read_csv(medals_url)

medals_data.head()

import csv
import urllib3

http = urllib3.PoolManager()
r = http.request('GET', medals_url)

cr = csv.reader(r.data)

## From xlsx

pd.read_excel(mainpath + '/titanic/titanic3.xls', 'titanic3')