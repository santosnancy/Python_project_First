# X^2 + 5x + 23
#if X = 4
from math import pow
print('\033[1;33mFind the value of  X\033[m')
num = float(input('Enter the value of X:...'))
a = pow(num, 2)
b = 5 * num
c = 23
exp = pow(num, 2) + 5*num + 23
print('This is the function X^2 + 5x + 23')
print(f'sum is {a} + {b} + {c}')
print(f'The Value of  X is {exp}')

