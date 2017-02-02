__author__ = 'mike_bowles'
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import sys

target_url = ( "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data" )

data = urllib2.urlopen(target_url).readlines()

print( "Fetching data to local memory ......" )
xList = []
labels = []

for line in data:
	row = line.strip().decode().split( "," )
	xList.append(row)

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])) + '\n')

nrow = len(xList)
ncol = len(xList[1])  # We assumed that all row has same number of elements

type_data = [0]*3
colCounts = []

# Mark number of type of attribute in the original data
for col in range(ncol):
	for row in xList:
		try:
			a = float(row[col])
			if isinstance(a, float):
				type_data[0] += 1
		except ValueError:
			if len(row[col]) > 0:
				type_data[1] += 1
			else:
				type_data[2] += 1
	colCounts.append(type_data)
	type_data = [0]*3

sys.stdout.write( 	"Col#" + '\t' + "Number" + '\t' +
			"Strings" + '\t' + "Other\n" )

iCol = 0 
for types in colCounts:
	sys.stdout.write( 	str(iCol) + '\t' + str(types[0]) + '\t' +
			 	str(types[1]) + '\t' + str(types[2]) + '\n' )
	iCol += 1


