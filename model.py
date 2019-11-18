# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:34:10 2019

@author: Vivek Nikam
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_train = pd.read_csv('../train.csv')
#Threshold for useless columns due to na values=300
ser = df_train.isna().sum()
useless_columns = list(ser[ser>300].index)
selected_columns = list(df_train.columns)
for col in useless_columns:
    selected_columns.remove(col)
selected_cat = []
selected_non_cat = []
for col in selected_columns:
    if df_train[col].dtype =='O':
        selected_cat.append(col)
    else:
        selected_non_cat.append(col)
y = 'SalePrice'
selected_columns.remove(y)
selected_non_cat.remove(y)