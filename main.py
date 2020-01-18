
import csv
import numpy
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

print(hive)

