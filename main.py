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

path = 'ResamplesT.txt'
data = pd.read_csv(path, sep="\t")
data_top = data.head()
print(data_top)

hive = data['HIVE-COTE']
BOSS = data['BOSS']

results = stats.ttest_rel(hive,BOSS)
print(results)