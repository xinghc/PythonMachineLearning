import numpy
from sklearn import datasets, linear_model
from math import sqrt
import matplotlib.pyplot as plt
try:
	import urllib.request as urllib2
except ImportError:
	import urllib2

def xattrSelect(x, idxSet):
	#takes X matrix as list of list and returns subset containing
	#columns in idxSet
	xOut = []
	for row in x:
		xOut.append([row[i] for i in idxSet])
	return(xOut)

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv")
data = urllib2.urlopen(target_url).readlines()
xList = []
labels = []
names = []
firstLine = True
for line in data:
	if firstLine:
		names = line.strip().decode('utf-8').split( ";" )
		firstLine = False
	else:
		row = line.strip().decode('utf-8').split( ";" )
		# quality is what we want to predict, put it into label
		labels.append(float(row[-1]))
		row.pop()
		floatRow = [float(num) for num in row]
		xList.append(floatRow)

indices = range(len(xList))
# One of three parts of data to be tested
xListTest = [xList[i] for i in indices if i%3 == 0 ]
labelsTest = [labels[i] for i in indices if i%3 == 0]
# Two of threee parts of data to be trained
xListTrain = [xList[i] for i in indices if i%3 != 0 ]
labelsTrain = [labels[i] for i in indices if i%3 != 0]

attributeList = []
index = range(len(xList[0]))
indexSet = set(index)
indexSeq = []
oosError = []
for i in index:
	attSet = set(attributeList)
	# remove the attribute that we have put into the attSet already
	attTrySet = indexSet - attSet
	attTry = [ii for ii in attTrySet]
	errorList = []
	attTemp = []
	# Try a new attribute with existing selected set (i.e., attributeList)
	for iTry in attTry:
		# Evaluate new candidates with existing attribites 
		attTemp = [] + attributeList
		attTemp.append(iTry)
		xTrainTemp = xattrSelect(xListTrain, attTemp)
		xTestTemp = xattrSelect(xListTest, attTemp)
		xTrain = numpy.array(xTrainTemp)
		yTrain = numpy.array(labelsTrain)
		xTest = numpy.array(xTestTemp)
		yTest = numpy.array(labelsTest)
		wineQModel = linear_model.LinearRegression()
		wineQModel.fit(xTrain,yTrain)
		rmsError = \
		  numpy.linalg.norm((yTest-wineQModel.predict(xTest)),2)/sqrt(len(yTest))
		errorList.append(rmsError)
		attTemp = []

	print("Time " + str(i) + " : " + str(errorList))
	iBest = numpy.argmin(errorList)
	attributeList.append(attTry[iBest])
	oosError.append(errorList[iBest])

print("Out of sample error versus attribute set size" )
print(oosError)
print("\n" + "Best attribute indices")
print(attributeList)
namesList = [names[i] for i in attributeList]
print("\n" + "Best attribute names")
print(namesList)

# Plot error versus number of attributes
x = range(len(oosError))
plt.plot(x, oosError, 'k')
plt.xlabel('Number of Attributes')
plt.ylabel('Error (RMS)')
plt.show()

# Use only two attribute to predict the test group
indexBest = oosError.index(min(oosError))
attributesBest = attributeList[1:(indexBest+1)]
xTrainTemp = xattrSelect(xListTrain, attributesBest)
xTestTemp = xattrSelect(xListTest, attributesBest)
xTrain = numpy.array(xTrainTemp); 
xTest = numpy.array(xTestTemp)

# train and plot error histogram
wineQModel = linear_model.LinearRegression()
wineQModel.fit(xTrain,yTrain)
errorVector = yTest-wineQModel.predict(xTest)
plt.hist(errorVector)
plt.xlabel("Bin Boundaries")
plt.ylabel("Counts")
plt.show()

# scatter plot of actual versus predicted
plt.scatter(wineQModel.predict(xTest), yTest, s=100, alpha=0.10)
plt.xlabel('Predicted Taste Score')
plt.ylabel('Actual Taste Score')
plt.show()

