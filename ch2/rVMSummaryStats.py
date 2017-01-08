__author__ = 'mike_bowles'
import urllib2
import sys
import numpy as np

target_url = ( "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data" )
data = urllib2.urlopen(target_url)

xList = []
labels = []

for line in data:
	row = line.strip().split( "," )
	xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type_data = [0]*3
colCounts = []

col = 3
colData = []
for row in xList:
	colData.append(float(row[col]))

# Calculate mean and SD for the data
colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)
sys.stdout.write( 	"Mean =" + '\t' + str(colMean) + '\t\t' +
			"Standard Deviation = " + '\t' + str(colsd) + '\n' )
percentBdry = []
#ntiles = 4
#for i in range(ntiles+1):
#	percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
percentBdry = (np.percentile(colArray, np.arange(0, 100+1, 25))) # +1 to print the P100
sys.stdout.write( "\nBoundaries for 4 Equal Percentiles \n" )
print(percentBdry)
sys.stdout.write( "\n" )

percentBdry = []
#ntiles = 10
#for i in range(ntiles+1):
#	percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
percentBdry = (np.percentile(colArray, np.arange(0, 100+1, 10)))  # +1 to print the P100
sys.stdout.write( "\nBoundaries for 10 Equal Percentiles \n" )
print(percentBdry)
sys.stdout.write( "\n" )

col = 60
colData = []
for row in xList:
	colData.append(row[col])

unique = set(colData)
sys.stdout.write( "Unique Label Values \n" )
print(unique)

catDict = dict(zip(list(unique), range(len(unique))))

catCount = [0]*2

for elt in colData:
	catCount[catDict[elt]] +=1

sys.stdout.write( "\nCounts for Each Value of Categorical Label\n" )
print(list(unique))
print(catCount)
