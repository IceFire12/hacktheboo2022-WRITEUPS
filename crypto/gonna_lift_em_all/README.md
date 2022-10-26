# Gonna-Lift-Em-All

![crypto](https://img.shields.io/badge/category-crypto-brightgreen) <br>
![difficulty](https://img.shields.io/badge/difficulty-easy-green) <br>
![solvetime](https://img.shields.io/badge/solved-durring%20event-green)

## Description

> Quick, there's a new custom Pokemon in the bush called "The Custom Pokemon". Can you find out what its weakness is and capture it?

Provided files are:
- [chall.py](chall.py)
- [data.txt](data.txt)

## Solving process

We get a python program and it’s output, includind the values of p, g, h and the value of two ciphertexts that correspond to the equations `g * y mod p` and `m * s mod p`. By using the following divideresidues function, I found online, we can extract y out of the equation `g*y mod p = c1`. Using y we can get the value of `s = pow(h, y, p)`. And then we use the divideresidues function again to get m out of the equation `m*s mod p = c2`. You can see the whole code [here](solution.py).

```python
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
```
```python
from Crypto.Util.number import *

def main():
    y = divideresidues(c1, g, p)
    s = pow(h, y, p)
    print(long_to_bytes(divideresidues(c2, s, p)))
```

**Flag:** *HTB{b3_c4r3ful_wh3n_1mpl3m3n71n6_cryp705y573m5_1n_7h3_mul71pl1c471v3_6r0up}*