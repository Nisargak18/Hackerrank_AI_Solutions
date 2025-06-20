"""Fred is a very predictable man. For instance, when he uses his laptop, all he does is watch TV shows. He keeps on watching TV shows until his battery dies. Also, he is a very meticulous man, i.e. he pays great attention to minute details. He has been keeping logs of every time he charged his laptop, which includes how long he charged his laptop for and after that how long was he able to watch the TV. Now, Fred wants to use this log to predict how long will he be able to watch TV for when he starts so that he can plan his activities after watching his TV shows accordingly.

Challenge

You are given access to Fred’s laptop charging log by reading from the file “trainingdata.txt”. The training data file will consist of 100 lines, each with 2 comma-separated numbers.

The first number denotes the amount of time the laptop was charged.
The second number denotes the amount of time the battery lasted.
The training data file can be downloaded here (this will be the same training data used when your program is run). The input for each of the test cases will consist of exactly 1 number rounded to 2 decimal places. For each input, output 1 number: the amount of time you predict his battery will last.

Sample Input

1.50

Sample Output

3.00"""

SOLUTION:

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    timeCharged = float(input().strip())



    data = []
    with open("trainingdata.txt", "r") as file:
        for line in file:
            try:
                x_str, y_str = line.strip().split(',')
                x, y = float(x_str), float(y_str)
                # Only include data where y != 8.0 (battery maxed out)
                if x > 0 and y != 8.0:
                    data.append((x, y))
            except:
                continue

    X = [d[0] for d in data]
    Y = [d[1] for d in data]
    n = len(X)

    # Compute mean
    mean_x = sum(X) / n
    mean_y = sum(Y) / n

    # Compute slope (m) and intercept (c)
    numerator = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n))
    denominator = sum((X[i] - mean_x) ** 2 for i in range(n))

    m = numerator / denominator
    c = mean_y - m * mean_x

    # Predict
    prediction = m * timeCharged + c

    # Print result rounded to 2 decimal places
    print(f"{prediction:.2f}")