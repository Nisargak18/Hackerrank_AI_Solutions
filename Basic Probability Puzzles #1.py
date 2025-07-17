'''Objective
In this challenge, we practice calculating probability.

Task
In a single toss of  fair (evenly-weighted) -sided dice, find the probability of that their sum will be at most .

Output Format

In the editor below, submit your answer as Plain Text in the form of an irreducible fraction , where  and  are both integers.

Your answer should resemble something like:

3/4'''

SOLUTION:

from math import gcd

def calulate_probability(max_sum,side=6): 
    total_outcome= side * side 
    favourable = 0

    for i in range(1,side+1):
        for j in range(1,side+1):
            if i+j<= max_sum:
                favourable +=1

    divisor = gcd(favourable,total_outcome)
    numerator= favourable//divisor
    denominator = total_outcome//divisor

    return f"{numerator}//{denominator}"
x=int(input())
print("total_outcome:",calulate_probability(x))
 