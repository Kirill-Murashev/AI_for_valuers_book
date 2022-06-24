# -*- coding: utf-8 -*-
# Spyder Editor

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# set significance level
alpha = 0.05

# import dataset
df = pd.read_csv('spba-flats-210928.csv')
print(df)
type(df['price_m'])

# get only prices and counties, release RAM
df1 = df[['price_m', 'county']]
del [[df]]

# add boolean var for region
df1['r'] = df1['county'].str.startswith('s')
# tranform into integer
df1['r'] *= 1

# create separate dataframes for city and suburbs
dfs = df1[df1['county'].str.startswith('s')]
dfl = df1[df1['county'].str.startswith('l')]

# get probability scores
# create dataframes containing only prices
Xs = dfs[['price_m', 'r']]
Xl = dfl[['price_m', 'r']]

# create random equal samples for each dataframe
#Xs = dfs.sample(n=2000)
#Xl = dfl.sample(n=2000)

# remove column names
#Xs = Xs[:].values
#Xl = Xl[:].values

# concatenate two dataframes into one
#X = pd.concat([Xs, Xl], axis=0)

# check if value in 's' greater than in 'l'
#X['r'] = X['s']



# sum of 'favourable'
#fav = pd.DataFrame.sum(X['r'])

# fit logit model to data
#logit = LogisticRegression()
#logit.fit(X[['s', 'l']], X['r'])
#print(logit.coef_)

# calculate logit score
#logit_score = logit.predict_proba(X[['s', 'l']])[:, 1]

# calculate AUC
#print(roc_auc_score(X['r'], logit_score))
