__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
import numpy

target_url = ( "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data" )

rocksVMines = pd.read_csv(target_url, header=None, prefix="V")
print(rocksVMines)

corMat = DataFrame(rocksVMines.corr())
print(corMat)

plot.pcolor(corMat)
plot.show()
