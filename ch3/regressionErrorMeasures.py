__author__ = 'mike-bowles'
from math import sqrt

#here are some made-up numbers to start with
target = [1.5, 2.1, 3.3, -4.7, -2.3, 0.75]
prediction = [0.5, 1.5, 2.1, -2.2, 0.1, -0.5]

error = []
for i in range(len(target)):
	error.append(target[i] - prediction[i])

print("Errors ",)
print(error)
print()

#calculate the squared errors and absolute value of errors
squaredError = []
absError = []
for val in error:
	squaredError.append(val*val)
	absError.append(abs(val))

#print squared errors and absolute value of errors
print("Squared Error")
print(squaredError)
print("Absolute Value of Error")
print(absError)
print()

print("MSE = ", sum(squaredError)/len(squaredError))
print("RMSE = ", sqrt(sum(squaredError)/len(squaredError)))
print("MAE = ", sum(absError)/len(absError))
print()

#compare MSE to target variance
targetDeviation = []
targetMean = sum(target)/len(target)
for val in target:
	targetDeviation.append((val - targetMean)*(val - targetMean))

print("Target Variance = ", sum(targetDeviation)/len(targetDeviation))
print("Target Standard Deviation = ", sqrt(sum(targetDeviation)/len(targetDeviation)))
print()
