#!/usr/bin/env python3

import random
import math

def modexp(x, y, N):
    """
    This function compute x^y mod N
    Hint:  modulo in python is  the "%" operator.
    You can check that your code is correct by comparing to pow(x,y,N), which is python's implementation
    """
    if y == 0:
        return 1
    z = modexp(x, math.floor(y/2), N)
    if y % 2 == 0:
        return (z * z) % N
    else:
        return (x * z * z) % N


def primality(N):
    """
    Test if a number N is prime using Fermat's little Theorem with 10 random values of a.
    That is, if a^(N-1) mod N = 1 then return true, and otherwise return false.
    """
    for iteration in range(10):
        a = random.randint(1, N-1)

        if modexp(a, N-1, N) != 1:
            return False

    return True


def prime_generator(N):
    """
    This function generates a prime number <= N
    Hint:  you can generate a random integer between a and b using random.randint(a,b)
    """
    tries = 0
    while tries < 100:
        # generate a random integer
        p = random.randint(1, N)
        if primality(p):
            return p
        else:
            tries += 1

    return False


def extended_Euclid(a, b):
    """
    This function computes (x,y,d) where d = gcd(a,b) and x and y are integers such that ax + by = d
    """
    if b == 0:
        return 1, 0, a
    (x1, y1, d) = extended_Euclid(b, a % b)

    return y1, x1 - math.floor(a/b) * y1, d


def main():
    """
    Test file for the two parts of the question
    """
    ## generate a 7 digit prime
    print("my prime number is", prime_generator(10000000))

    ## RSA
    ##################
    e = 5
    gcd = 2
    while gcd != 1:
        p = prime_generator(10000000)
        q = prime_generator(10000000)
        p1q1 = (p-1)*(q-1)
        # determine if (p-1)(q-1) and e are relatively prime
        (x, y, gcd) = extended_Euclid(p1q1, e)

    print("p and q are", p, " and ", q)
    N = p * q
    print("N is", p*q)
    print("(p-1)(q-1) is", p1q1)
    print("gcd of e and (p-1)(q-1) is", gcd)

    # Find the decoding exponent d
    (x, y, gcd) = extended_Euclid(p1q1, e)
    d = y % p1q1
    print("the decoding exponent is", d)

    # encrypted version of x
    x = 2148321
    encrypted = modexp(x, e, N)
    print("the encrypted message is", encrypted)

    # decrypted message
    decrypted = modexp(encrypted, d, N)
    print("the decrypted message is", decrypted)

if __name__ == '__main__':
    main()
