# -*- coding: utf-8 -*-
# Spyder Editor

# import libraries
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.stats as stats

# import dataset
df = pd.read_csv("spba-flats-210928.csv")
print(df)
type(df["price_m"])

# get only prices and counties, release RAM
df1 = df[["price_m", "county"]]
del [[df]]

# calculate the number of observations on data frame
spbaLenR = round(math.sqrt(len(df1.index)))

# fit a normal distribution to the data: mean and standard deviation
mu, std = norm.fit(df1["price_m"])

# plot the histogram
plt.hist(df1["price_m"], bins=spbaLenR, density=True)

# plot the PDF
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Fit Values: {:.2f} and {:.2f}".format(mu, std)
plt.title(title)

plt.savefig('spba-price-histogram-py.pdf')

# create separate data frames for city and suburbs
#dfs = df1[df1["county"].str.startswith('s')]
#dfl = df1[df1["county"].str.startswith('l')]

# Saint-Petersburg

# calculate the number of observations on data frame
#spbLen = len(dfs.index)
#spbLenR = round(math.sqrt(spbLen))

# fit a normal distribution to the data: mean and standard deviation
#muS, stdS = norm.fit(dfs["price_m"])

# plot the histogram
#plt.hist(dfs["price_m"], bins=spbLenR, density=True)

# plot the PDF
#xmin, xmax = plt.xlim()
#x = np.linspace(xmin, xmax, 100)
#ps = norm.pdf(x, muS, stdS)

#plt.plot(x, ps, 'k', linewidth=2)
#title = "Fit Values: {:.2f} and {:.2f}".format(muS, stdS)
#plt.title(title)

# LO
# calculate the number of observations on data frame
#loLen = len(dfl.index)
#loLenR = round(math.sqrt(loLen))

# fit a normal distribution to the data: mean and standard deviation
#muL, stdL = norm.fit(dfl["price_m"])

# plot the histogram
#plt.hist(dfl["price_m"], bins=loLenR, density=True)

# plot the PDF
#xmin, xmax = plt.xlim()
#x = np.linspace(xmin, xmax, 100)
#pl = norm.pdf(x, muL, stdL)

#plt.plot(x, ps, 'k', linewidth=2)
#title = "Fit Values: {:.2f} and {:.2f}".format(muS, stdS)
#plt.title(title)

# add labels to data
#dfs["region"] = "SPb"
#dfl["region"] = "LO"

# plot boxplot
#prices = [dfs, dfl]
#allPrices = pd.concat(prices)
#plt.figure()
#allPrices.boxplot(by="region")

# normality tests
#shapiroWSpb, shapiroPvalueSpb = stats.shapiro(dfs['price_m'])
#shapiroWLO, shapiroPvalueLO = stats.shapiro(dfl['price_m'])

# Mann-Whitney test
#U = stats.mannwhitneyu(x=dfs['price_m'], y=dfl['price_m'],
#                       alternative='two-sided')
