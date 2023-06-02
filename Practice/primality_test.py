###
# Primality Test
# Author: Nam Jun Lee
# Date: Sept 9th, 2021
###

import math


# A function that determines whether the input value is decimal
def is_prime(n):
    # Check all the numbers from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # Not prime number
    return True  # Prime number


# A function of sum of all prime number
def sum_prime(m):
    total = 0
    # Determine the sum of all the few from 2 to m
    for i in range(2, m + 1):
        if is_prime(i):
            total += i
    return total


num = int(input('Please enter an integer >= 2: '))

if num >= 2:
    # Prime
    if is_prime(num):
        print(f'{num} is prime!')
    # Not Prime
    else:
        print(f'{num} is not prime!')
    print(f'Sum of primes from 2 to {num} is {sum_prime(num)}!')
# less than 2
else:
    print('Invalid input')
