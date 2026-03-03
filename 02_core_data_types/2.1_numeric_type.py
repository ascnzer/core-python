# 2.1 Numeric Types
# Chapter 02: Core Data Types
# Topics covered:
#   - Integers
#   - Floating-point numbers
#   - Complex numbers
#   - Precision issues
#   - Arithmetic operators


# INTEGERS
# Whole numbers, positive or negative, with no decimal point
# Python integers have unlimited precision - they can be arbitrarily large

age         = 25
temperature = -10
big_num     = 1_000_000      # underscores allowed for readability 
zero        = 0

print(type(age))             # <class 'int'>
print(big_num)               # 1000000

# Integer literals in different bases
binary  = 0b1010             # base 2  - prefix 0b
octal   = 0o17               # base 8  - prefix 0o
hexa    = 0xFF               # base 16 - prefix 0x

print(binary)                # 10
print(octal)                 # 15
print(hexa)                  # 255

# Convert to different base representations
print(bin(10))               # '0b1010'
print(oct(15))               # '0o17'
print(hex(255))              # '0xff'

# Python integers have no size limit
huge = 10 ** 100             # googol - works fine in Python
print(huge)


# FLOATING-POINT NUMBERS
# Numbers with a decimal point
# Stored using IEEE 754 double-precision (64-bit)

pi      = 3.14159
gravity = 9.81
tiny    = -0.001
sci     = 1.5e10             # scientific notation: 1.5 x 10^10
small   = 2.7e-4             # 2.7 x 10^-4

print(type(pi))              # <class 'float'>
print(sci)                   # 15000000000.0
print(small)                 # 0.00027

# Special float values
import math

pos_inf = float("inf")       # positive infinity
neg_inf = float("-inf")      # negative infinity
nan     = float("nan")       # not a number

print(pos_inf)               # inf
print(neg_inf)               # -inf
print(nan)                   # nan

print(math.isinf(pos_inf))   # True
print(math.isnan(nan))       # True


# COMPLEX NUMBERS
# Numbers with a real and imaginary part
# Written as: real + imagj  (j is the imaginary unit in Python)

c1 = 3 + 4j
c2 = 1 - 2j
c3 = complex(2, 5)           # complex(real, imag)

print(type(c1))              # <class 'complex'>
print(c1)                    # (3+4j)
print(c3)                    # (2+5j)

# Access parts separately
print(c1.real)               # 3.0
print(c1.imag)               # 4.0
print(c1.conjugate())        # (3-4j)

# Arithmetic with complex numbers
print(c1 + c2)               # (4+2j)
print(c1 * c2)               # (11-2j)  -  (3+4j)(1-2j) = 3-6j+4j-8j^2 = 11-2j

# Magnitude (absolute value)
print(abs(c1))               # 5.0  -  sqrt(3^2 + 4^2) = 5


# PRECISION ISSUES
# Floats are stored in binary - some decimals cannot be represented exactly
# This is a fundamental limitation of IEEE 754, not a Python bug

print(0.1 + 0.2)             # 0.30000000000000004  (not exactly 0.3!)
print(0.1 + 0.2 == 0.3)      # False

# Why this happens:
# 0.1 in binary is 0.0001100110011... (repeating) - gets rounded during storage

# Fix 1: round() for display purposes
result = 0.1 + 0.2
print(round(result, 2))      # 0.3

# Fix 2: math.isclose() for comparisons (recommended)
print(math.isclose(0.1 + 0.2, 0.3))                # True
print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9))  # True

# Fix 3: decimal module for exact decimal arithmetic
from decimal import Decimal

d1 = Decimal("0.1")
d2 = Decimal("0.2")
print(d1 + d2)               # 0.3  - exact!
print(d1 + d2 == Decimal("0.3"))  # True


# ARITHMETIC OPERATORS
# Standard math operations on numeric types

a = 17
b = 5

print(a + b)    # 22      - addition
print(a - b)    # 12      - subtraction
print(a * b)    # 85      - multiplication
print(a / b)    # 3.4     - true division (always returns float)
print(a // b)   # 3       - floor division (rounds DOWN toward negative infinity)
print(a % b)    # 2       - modulo (remainder after division)
print(a ** b)   # 1419857 - exponentiation (17 to the power of 5)

# Floor division vs true division
print(7 / 2)    # 3.5
print(7 // 2)   # 3    - truncates toward negative infinity
print(-7 // 2)  # -4   - NOT -3! floors toward negative infinity

# Modulo with negatives
print(10 % 3)   # 1
print(-10 % 3)  # 2    - result has same sign as the divisor in Python

# Operator precedence (PEMDAS / BODMAS)
# ** > (unary -) > * / // % > + -
print(2 + 3 * 4)     # 14  - multiplication first
print((2 + 3) * 4)   # 20  - parentheses override
print(2 ** 3 ** 2)   # 512 - exponentiation is right-associative: 2**(3**2) = 2**9

# Augmented assignment operators
x = 10
x += 5      # x = 15
x -= 3      # x = 12
x *= 2      # x = 24
x //= 5     # x = 4
x **= 3     # x = 64
x %= 10     # x = 4
print(x)    # 4

# Built-in numeric functions
print(abs(-42))          # 42     - absolute value
print(pow(2, 10))        # 1024   - same as 2 ** 10
print(pow(2, 10, 1000))  # 24     - modular exponentiation: (2**10) % 1000
print(divmod(17, 5))     # (3, 2) - returns (quotient, remainder) as a tuple
print(round(3.14159, 2)) # 3.14   - round to 2 decimal places
print(round(2.5))        # 2      - banker's rounding (rounds to nearest even)
print(round(3.5))        # 4      - banker's rounding
