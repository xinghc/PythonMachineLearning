__author__ = 'mike-bowles'
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import numpy
import random
from sklearn import datasets, linear_model
from sklearn.metrics import roc_curve, auc
import pylab as pl

def confusionMatrix(predicted, actual, threshold):
	if len(predicted) != len(actual): return -1
	tp = 0.0
	fp = 0.0
	tn = 0.0
	fn = 0.0
	for i, actual_val in enumerate(actual):
		if actual_val == 1.0: #labels that are 1.0 (positive examples)
			if predicted[i] > threshold:
				tp += 1.0 #correctly predicted positive
			else:
				fn += 1.0 #incorrectly predicted negative
		else: #labels that are 0.0 (negative examples)
			if predicted[i] < threshold:
				tn += 1.0 #correctly predicted negative
			else:
				fp += 1.0 #incorrectly predicted positive
		rtn = [tp, fn, fp, tn]
	return rtn

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib2.urlopen(target_url)

xList = []
labels = []
for line in data:
	row = line.strip().decode().split(",")
	if(row[-1] == 'M'):
		labels.append(1.0)
	else:
		labels.append(0.0)
	row.pop()	# Remove the label in the row
	floatRow = [float(num) for num in row]
	xList.append(floatRow)

# 2/3 data for training, 1/3 data for testing
indices = range(len(xList))
xListTrain = [xList[i] for i in indices if i%3 != 0 ]
labelsTrain = [labels[i] for i in indices if i%3 != 0]
xListTest = [xList[i] for i in indices if i%3 == 0 ]
labelsTest = [labels[i] for i in indices if i%3 == 0]

# make them into numpy array
xTrain = numpy.array(xListTrain)
yTrain = numpy.array(labelsTrain)
xTest = numpy.array(xListTest)
yTest = numpy.array(labelsTest)
if xTrain.shape[0] != yTrain.shape[0]:
	print("Matrix size mismatch")
	print("Shape of xTrain array", xTrain.shape)
	print("Shape of yTrain array", yTrain.shape)
	exit()
elif xTest.shape[0] != yTest.shape[0]:
	print("Matrix size mismatch")
	print("Shape of xTest array", xTest.shape)
	print("Shape of yTest array", yTest.shape)
	exit()

# train linear regression model
rocksVMinesModel = linear_model.LinearRegression()
rocksVMinesModel.fit(xTrain,yTrain)

# in-sample error examination
trainingPredictions = rocksVMinesModel.predict(xTrain)
print("Some values predicted by model", trainingPredictions[0:5], trainingPredictions[-6:-1])
# generate confusion matrix for predictions on training set (in-sample error)
confusionMatTrain = confusionMatrix(trainingPredictions, yTrain, 0.5)
# pick threshold value and generate confusion matrix entries
tp = confusionMatTrain[0]
fn = confusionMatTrain[1]
fp = confusionMatTrain[2]
tn = confusionMatTrain[3]
print("tp = " + str(tp) + "\tfn = " + str(fn) + "\n" + "fp = " + str(fp) + "\ttn = " + str(tn) + '\n')

# out-of-sample data examination
testPredictions = rocksVMinesModel.predict(xTest)
# generate confusion matrix from predictions on out-of-sample data
conMatTest = confusionMatrix(testPredictions, yTest, 0.5)
# pick threshold value and generate confusion matrix entries
tp = conMatTest[0]
fn = conMatTest[1]
fp = conMatTest[2]
tn = conMatTest[3]
print("tp = " + str(tp) + "\tfn = " + str(fn) + "\n" + "fp = " + str(fp) + "\ttn = " + str(tn) + '\n')

# generate ROC curve for in-sample data
fpr, tpr, thresholds = roc_curve(yTrain,trainingPredictions)
roc_auc = auc(fpr, tpr)
print( 'AUC for in-sample ROC curve: %f' % roc_auc)
# Plot ROC curve
pl.clf()
pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
pl.plot([0, 1], linestyle='--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('In sample ROC rocks versus mines')
pl.legend(loc="lower right")
pl.show()

# generate ROC curve for out-of-sample data
fpr, tpr, thresholds = roc_curve(yTest,testPredictions)
roc_auc = auc(fpr, tpr)
print( 'AUC for out-of-sample ROC curve: %f' % roc_auc)
# Plot ROC curve
pl.clf()
pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
pl.plot([0, 1], linestyle='--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Out-of-sample ROC rocks versus mines')
pl.legend(loc="lower right")
pl.show()
