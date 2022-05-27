#!/usr/bin/env python3
import numpy.fft as np


def main():
    """
    Using the FFT to multiply two binary numbers.  
    
    """
    # The binary numbers and their product
    a_bin = 0b110000001100
    b_bin = 0b100011110000
    c_bin = a_bin * b_bin
    print('The product of a and b is', c_bin)


    # (i) The coefficients of the polynomials A and B
    Acoeff = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    Bcoeff = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1]

    # (ii) the value representations of A and B
    Aval = np.fft(Acoeff, 32)
    Bval = np.fft(Bcoeff, 32)


    # (iii) The value representation of C
    Cval = []
    for i in range(len(Aval)):
        Cval.append(Aval[i] * Bval[i])


    # (iv) The coefficients of the polynomial C
    Ccoeff = np.ifft(Cval)
    # we'll get rid of the imaginary parts, which are just numerical errors
    for i, c in enumerate(Ccoeff):
        Ccoeff[i] = int(round(c.real))

    # (v) calculate the product by evaluating the polynomial at 2, i.e., C(2)
    # (You may need to take the real part at the end if there is a small imaginary component)
    prod = 0
    power = 1
    for i in range(len(Ccoeff)):
        prod += Ccoeff[i] * power
        power *= 2
    print('Using the FFT the product of a and b is', int(round(prod.real)))


    # (vi) write code to calculate the binary digits of c directly from the coefficients of C, Ccoeff.
    c = list(Ccoeff.real)
    for i in range(len(c)-1):
        (q, r) = divmod(c[i], 2)
        c[i+1] += q
        c[i] = r
    
    # now concatenate the nonzero elements as a string to see what the binary number is
    c_string = ""
    for c_bit in reversed(c):
        c_string += str(int(c_bit))
    # print the binary number
    print("the product of a and b in binary is", c_string)
    # finally, check that c_string is the correct binary number
    print("the conversion of this binary number to decimal is", int(c_string, 2))


if __name__ == '__main__':
    main()
