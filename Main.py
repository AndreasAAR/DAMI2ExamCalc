'''
Auth: Andreas Ährlund-Richter
Course: Data Mining 2 "Research Topics In Data Science"
T-test question in Hand-In Exam.
'''

import csv
import numpy as np
import pandas as pd
import scipy
from scipy.stats import stats

#equations from
#https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/t-test/

path = 'ResamplesT.txt'
data = pd.read_csv(path, sep="\t")
data_top = data.head()
print(data_top)

hive = data['HIVE-COTE']
boss = data['BOSS']

#T-test paired
results = stats.ttest_rel(hive,boss)
print(results)

###"Manual" step-wise procedure

#Getting squared and summed differences
sumSquared = sum((hive**2) -(boss**2))
sumDiff = sum(hive-boss)
sumDiffSquared = sumSquared**2
#Number of samples
numSamp = len(hive)

print("sumDiff")
print(sumDiff)
print("sumSquared")
print(sumSquared)
print("sumDiffSquared")
print(sumDiffSquared)
print("numSamp")
print(numSamp)


