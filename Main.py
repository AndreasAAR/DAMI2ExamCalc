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
import math

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
#sumsquaresΣD
Σ2 = sum(((hive) - (boss)) ** 2)
Σ = sum(hive - boss)
Σ2_2 = Σ ** 2
#Number of samples
n = len(hive)

print("sumDiff")
print(Σ)
print("sumSquared")
print(Σ2)
print("sumDiffSquared")
print(Σ2_2)
print("numSamp")
print(n)

#Manual calculation from results
result = ((Σ) / n)\
         / math.sqrt((Σ2 - (Σ2_2 / n))
                     / ((n - 1) * (n)))
print(result)


'''
ΣD:  Sum of the differences (Sum of X-Y from Step 2)
Σ2DSum of the squared differences (from Step 4)
(ΣD)2:  Sum of the differences (from Step 2), squared.
N: Number of samples in each population.
From Python https://github.com/AndreasAAR/DAMI2ExamCalc these will be:
ΣD:  9.697089319
Σ2D:  14.334104893544094
(ΣD)2:  205.46656309912473
N: 85
Formula used:
https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/t-test/
'''



