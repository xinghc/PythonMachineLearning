__author__ = 'mike_bowles'
import urllib2
import sys

target_url = ( "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data" )

data = urllib2.urlopen(target_url)

print "Fetching data to local memory ......"
xList = []
labels = []

for line in data:
	row = line.strip().split( "," )
	xList.append(row)

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])) + '\n')


