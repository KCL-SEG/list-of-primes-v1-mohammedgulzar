"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    num = 2
    while len(list) < number_of_primes:
        primeFlag = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                primeFlag = False
        if primeFlag:
            list.append(num)
        num += 1
    return list


print(primes(10))
