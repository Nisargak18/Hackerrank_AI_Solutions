"""You are given an array of N integers separated by spaces, all in one line.

Display the following:

Mean (m): The average of all the integers.

Median of this array: In case, the number of integers is odd, the middle element; else, the average of the middle two elements.

Mode: The element(s) which occurs most frequently. If multiple elements satisfy this criteria, display the numerically smallest one.

Standard Deviation (SD).

SD = (((x1-m)2+(x2-m)2+(x3-m)2+(x4-m)2+...(xN-m)2))/N)0.5

where xi is the ith element of the array

Lower and Upper Boundary of the 95% Confidence Interval for the mean, separated by a space. This might be a new term to some. However, it is an important concept with a simple, formulaic solution. Look it up!

Other than the modal values (which should all be integers) the answers should be in decimal form till one place of decimal (0.0 format). An error margin of +/- 0.1 will be tolerated for the standard deviation and the confidence interval boundaries. The mean, mode and median values should match the expected answers exactly."""

SOLUTION:

import math
from collections import Counter

# Input
n = int(input())
data = list(map(int, input().split()))

# Mean
mean = sum(data) / n

# Median
sorted_data = sorted(data)
if n % 2 == 0:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
else:
    median = sorted_data[n // 2]

# Mode
frequency = Counter(data)
max_freq = max(frequency.values())
modes = [k for k, v in frequency.items() if v == max_freq]
mode = min(modes)

# Standard Deviation
squared_diff = [(x - mean) ** 2 for x in data]
std_dev = math.sqrt(sum(squared_diff) / n)

# Confidence Interval (95%)
margin = 1.96 * (std_dev / math.sqrt(n))
ci_lower = mean - margin
ci_upper = mean + margin

# Output
print(f"{mean:.1f}")
print(f"{median:.1f}")
print(f"{mode}")
print(f"{std_dev:.1f}")
print(f"{ci_lower:.1f} {ci_upper:.1f}")
