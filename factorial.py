#!/usr/bin/env python3

# https://github.com/karan/Projects

from operator import mul
from functools import reduce
import timeit

def factorial_recursive(num):
    num = int(num)
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)

def factorial(num):
    return reduce(mul, list(range(1, num + 1))) if num != 0 else 1

if __name__ == "__main__":
    print('Factorial of 0 is {} using recursion'.format(factorial_recursive(0)))
    print('Factorial of 10 is {} using recursion'.format(factorial_recursive(10)))
    print('Factorial of 0 is {} using reduce'.format(factorial(0)))
    print('Factorial of 10 is {} using reduce'.format(factorial(10)))
    for num in range(0, 1000, 200):
        recursive_time = timeit.timeit("factorial_recursive({})".format(num),
                                    setup="from factorial import factorial_recursive",
                                    number=1)
        reduce_time = timeit.timeit("factorial({})".format(num),
                                    setup="from factorial import factorial",
                                    number=1)
        print("Recursive {:6.5f} s, reduce {:6.5f} s for num={}".format(recursive_time, reduce_time, num))

