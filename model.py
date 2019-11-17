# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:34:10 2019

@author: Vivek Nikam
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_train = pd.read_csv('../train.csv')
#Find useless columns --- if Non-null>1200 keep else delete column
#find categorical features and non-cat features
# delete categorical features whode unique values>8
#fillna non-cat columns using mean/mode/median
#fillna cat columns using mode/median
#create dummy columns from cat-columns
#create final dataframe for train
#create model-Random forest/xgboost
#create dataframe as per submission file and submit to kaggle
#post your score to CodeNautics DSML group.