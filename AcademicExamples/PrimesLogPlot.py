import numpy as np
import matplotlib.pyplot as plt
import math

def is_prime(primeNumberCandidate):
    if primeNumberCandidate == 2:
        return True
    if primeNumberCandidate == 1 or primeNumberCandidate % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(primeNumberCandidate)) + 1, 2):
        if primeNumberCandidate % i == 0:
            return False
    return True

def count_primes(n):
    count = 0
    for i in range(1, n):
        if is_prime(i):
            count += 1
    return count

numberRange = [10, 100, 1000, 10000, 100000, 1000000]
primes = [count_primes(i) for i in numberRange]

plt.plot(numberRange, primes, 'o-')
plt.yscale('log')
plt.xlabel('Range of Numbers')
plt.ylabel('Number of primes less than n')
plt.title('Number of primes less than n')
plt.show()
