__author__ = 'mike_bowles'
import numpy as np
import pylab
import scipy.stats as stats
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import sys

target_url = ( "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data" )
data = urllib2.urlopen(target_url).readlines()
xList = []
labels = []

for line in data:
        row = line.strip().decode().split( "," )
        xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type_data = [0]*3
colCounts = []

col = 3
colData = []
for row in xList:
        colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colStd = np.std(colData)

sys.stdout.write("Mean = " + str(colMean) + "\tStandard Deviation = " + str(colStd) + "\n")

stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()
