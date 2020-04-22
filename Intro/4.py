import sys
import math

'''
По данному натуральном n вычислите сумму . 
В решении этой задачи можно использовать только один цикл.
'''

def count_factorial(n):
    r = 0
    for i in range(1, n+1):
        r += math.factorial(i)
    print(r)

n = int(input())
count_factorial(n)