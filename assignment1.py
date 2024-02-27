
import math

def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            return True
    return False

def are_relatively_prime(num1, num2):
    hcf = 1
    if is_prime(num1) and is_prime(num2):
        return True
    else:
        if num1 > num2:
            smaller = num2
        elif num1 < num2:
            smaller = num1
        else:
            smaller = num1
        for i in range(1, smaller + 1):
            if num1 % i == 0 and num2 % i == 0:
                hcf = i * hcf
        if hcf == 1:
            return True
        else:
            return False

def primes(num):
    lst = []
    for i in range(num + 1):
        if is_prime(i):
            lst.append(i)
    return lst

def prime_decomposition(num):
    lst = []
    for i in range(num + 1):
        if is_prime(i) == True:
            if num % i == 0:
                lst.append(i)
    lst2 = []
    while num > 1:
        for prime_num in lst:
                num = num // prime_num
                lst2.append(prime_num)
    return lst2

