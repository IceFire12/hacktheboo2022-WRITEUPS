from Crypto.Util.number import *

def divideresidues(dividend, divisor, modulus):
    r, newr = modulus, divisor
    t, newt = 0, 1
    while newr != 0:
        quotient, remainder = divmod(r, newr)
        r, newr = newr, remainder
        t, newt = newt, t - quotient * newt
    if t < 0:
        t = t + modulus
    quotient, remainder = divmod(dividend, r)
    return t * quotient % modulus

def main():
    y = divideresidues(c1, g, p)
    s = pow(h, y, p)
    print(long_to_bytes(divideresidues(c2, s, p)))
