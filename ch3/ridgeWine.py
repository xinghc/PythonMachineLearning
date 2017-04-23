__author__ = 'mike-bowles'
import numpy 
from sklearn import datasets, linear_model 
from math import sqrt 
import matplotlib.pyplot as plt
try:
        import urllib.request as urllib2
except ImportError:
        import urllib2

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
		labels.append(float(row[-1]))
		row.pop()
		floatRow = [float(num) for num in row]
		xList.append(floatRow)

indices = range(len(xList))
xListTest = [xList[i] for i in indices if i%3 == 0 ]
xListTrain = [xList[i] for i in indices if i%3 != 0 ]
labelsTest = [labels[i] for i in indices if i%3 == 0]
labelsTrain = [labels[i] for i in indices if i%3 != 0]
xTrain = numpy.array(xListTrain); 
yTrain = numpy.array(labelsTrain)
xTest = numpy.array(xListTest); 
yTest = numpy.array(labelsTest)
alphaList = [0.1**i for i in [0, 1, 2, 3, 4, 5, 6]]

rmsError = []
for alph in alphaList:
	wineRidgeModel = linear_model.Ridge(alpha=alph)
	wineRidgeModel.fit(xTrain, yTrain)
	rmsError.append(numpy.linalg.norm((yTest-wineRidgeModel.predict(xTest)), 2)/sqrt(len(yTest)))

print("RMS Error alpha")

for i in range(len(rmsError)):
	print(rmsError[i], alphaList[i])

#plot curve of out-of-sample error versus alpha
x = range(len(rmsError))
plt.plot(x, rmsError, 'k')
plt.xlabel('-log(alpha)')
plt.ylabel('Error (RMS)')
plt.show()

#Plot errors (aka residuals)
indexBest = rmsError.index(min(rmsError))
alph = alphaList[indexBest]
wineRidgeModel = linear_model.Ridge(alpha=alph)
wineRidgeModel.fit(xTrain, yTrain)
errorVector = yTest-wineRidgeModel.predict(xTest)

plt.hist(errorVector)
plt.xlabel("Bin Boundaries")
plt.ylabel("Counts")
plt.show()
plt.scatter(wineRidgeModel.predict(xTest), yTest, s=100, alpha=0.10)
plt.xlabel('Predicted Taste Score')
plt.ylabel('Actual Taste Score')
plt.show()

