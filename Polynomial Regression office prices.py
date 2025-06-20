"""The Problem
Charlie wants to buy office space and has conducted a survey of the area. He has quantified and normalized various office space features, and mapped them to values between 0 and 1. Each row in Charlie's data table contains these feature values followed by the price per square foot. However, some prices are missing. Charlie needs your help to predict the missing prices.

The prices per square foot are approximately a polynomial function of the features, and you are tasked with using this relationship to predict the missing prices for some offices.

The prices per square foot, are approximately a polynomial function of the features in the observation table. This polynomial always has an order less than 4
Input Format

The first line contains two space separated integers, F and N. Over here, F is the number of observed features. N is the number of rows for which features as well as price per square-foot have been noted.
This is followed by a table with F+1 columns and N rows with each row in a new line and each column separated by a single space. The last column is the price per square foot.

The table is immediately followed by integer T followed by T rows containing F space-separated columns.

Constraints

1 <= F <= 5
5 <= N <= 100
1 <= T <= 100
0 <= Price Per Square Foot <= 10^6 0 <= Factor Values <= 1

Output Format

T lines. Each line 'i' contains the predicted price for the 'i'th test case."""

SOLUTION:


import numpy as np 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#step1:Read input
F, N = map(int, input().split())

#Read training data
data = [list(map(float, input().split())) for i in range(N)]
data = np.array(data)
X_train, y_train = data[:, :-1], data[:, -1]

#step2:Read test data
T = int(input())
X_test = [list(map(float, input().split())) for i in range(T)]
X_test = np.array(X_test)

#step3: Polynomial transformation (degree 3 as in problem)
degree = 3
poly = PolynomialFeatures(degree)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)


#step4:Train the regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)


#step5:Predict and print result
predictions = model.predict(X_test_poly)

#output predictions rounded to 2 decimal places
for p in predictions:
    print(round(p, 2))