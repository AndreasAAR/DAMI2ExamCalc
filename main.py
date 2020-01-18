
import csv

import numpy
import numpy as np
import pandas as pd



path = 'ResamplesT.txt'

X = pd.read_csv(path, sep="\t")
print(X)