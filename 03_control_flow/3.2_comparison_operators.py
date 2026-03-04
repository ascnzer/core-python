# 3.2 Comparison Operators
# Chapter 03: Control Flow
# Topics covered:
#   - Equality vs identity
#   - Relational operators
#   - Chained comparisons
#   - Floating-point comparison pitfalls


# EQUALITY VS IDENTITY
# == checks if two values are EQUAL (same content)
# is checks if two variables point to the SAME object in memory

# Equality (==)
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)          # True   - same content
print(a != b)          # False  - not unequal

# Identity (is)
print(a is b)          # False  - different objects in memory
print(id(a))           # some memory address
print(id(b))           # different address

# When the same object is assigned to two variables
c = a                  # c points to the same object as a
print(a is c)          # True   - same object
print(a == c)          # True   - also equal (same object is always equal)

# The difference matters for mutable types
a.append(4)
print(c)               # [1, 2, 3, 4]  - c reflects the change (same object)
print(b)               # [1, 2, 3]     - b is unchanged (different object)

# Integers: Python caches small integers (-5 to 256)
x = 100
y = 100
print(x is y)          # True   - CPython reuses cached small int objects
print(x == y)          # True

x = 1000
y = 1000
print(x is y)          # False  - large integers are NOT cached
print(x == y)          # True   - still equal in value

# Strings: Python sometimes interns string literals
s1 = "hello"
s2 = "hello"
print(s1 is s2)        # True   - Python interns short, simple strings
print(s1 == s2)        # True

s1 = "hello world!"    # strings with spaces may not be interned
s2 = "hello world!"
print(s1 is s2)        # False  (implementation-dependent)
print(s1 == s2)        # True   - always reliable for value comparison

# None, True, False - always use 'is' for these singletons
val = None
print(val is None)     # True   - correct
print(val == None)     # True   - works but PEP 8 says use 'is'

flag = True
print(flag is True)    # True
print(flag is False)   # False

# Rule of thumb:
# Use == to compare values
# Use is only for None, True, False, or when you explicitly need identity


# RELATIONAL OPERATORS
# Compare values to determine ordering
# Work on numbers, strings (lexicographic), and any type that defines ordering

# Numeric comparisons
a = 10
b = 20

print(a < b)           # True   - less than
print(a > b)           # False  - greater than
print(a <= 10)         # True   - less than or equal
print(a >= 11)         # False  - greater than or equal
print(a == b)          # False  - equal to
print(a != b)          # True   - not equal to

# All comparison operators return a bool
result = a < b
print(type(result))    # <class 'bool'>
print(result)          # True

# String comparisons - lexicographic (dictionary order by Unicode code point)
print("apple" < "banana")    # True   - 'a' (97) < 'b' (98)
print("apple" < "Apple")     # False  - lowercase 'a' (97) > uppercase 'A' (65)
print("abc" == "abc")        # True
print("abc" < "abd")         # True   - same up to last char, 'c' < 'd'
print("abc" < "abcd")        # True   - shorter string is less if equal so far

# Comparing different numeric types is fine - Python promotes automatically
print(10 == 10.0)      # True   - int and float compared by value
print(10 < 10.5)       # True
print(1 == True)       # True   - True is 1 (bool is subclass of int)
print(0 == False)      # True

# Comparing incompatible types raises TypeError in Python 3
# print("hello" > 5)   # TypeError: '>' not supported between str and int
# print([1,2] < [1,3]) # works - lists compare element by element


# CHAINED COMPARISONS
# Python allows multiple comparisons in one expression
# More readable than the equivalent and-linked version

age = 25

# Standard way in most languages
print(age >= 18 and age <= 65)   # True

# Python chained comparison - reads like math notation
print(18 <= age <= 65)           # True  - equivalent, more readable
print(0 < age < 100)             # True
print(10 < age < 20)             # False - age is 25

# How chaining works internally:
# a < b < c  is evaluated as  (a < b) and (b < c)
# Each middle term is evaluated ONCE, not twice

x = 5
print(1 < x < 10)                # True  - x evaluated once
print(1 < x and x < 10)         # True  - equivalent but x appears twice

# Chaining with equality
print(1 == 1 == 1)               # True
print(1 == 1 == 2)               # False

# Chaining with different operators
score = 75
print(0 <= score <= 100)         # True  - valid score range check
print(60 <= score < 70)          # False - score is 75, not in 60-69

# Chaining three or more comparisons
a, b, c, d = 1, 2, 3, 4
print(a < b < c < d)             # True  - ascending order
print(a < b > c)                 # False - b > c is False (2 > 3 is False)

# Useful real-world example: validate a value is within bounds
def is_valid_percentage(p):
    return 0 <= p <= 100

print(is_valid_percentage(75))   # True
print(is_valid_percentage(105))  # False
print(is_valid_percentage(-5))   # False


# FLOATING-POINT COMPARISON PITFALLS
# Floats are stored in binary IEEE 754 format
# Some decimal values cannot be represented exactly, causing unexpected results

# The classic problem
print(0.1 + 0.2)           # 0.30000000000000004  - NOT 0.3
print(0.1 + 0.2 == 0.3)    # False  - dangerous!

# Another example
print(0.1 * 3)             # 0.30000000000000004
print(0.1 * 3 == 0.3)      # False

# Looks fine but fails
total = 0.0
for _ in range(10):
    total += 0.1
print(total)               # 0.9999999999999999  - not 1.0
print(total == 1.0)        # False

# Why this happens:
# 0.1 in binary = 0.0001100110011... (infinite repeating fraction)
# Gets rounded to fit in 64 bits - tiny error accumulates

# FIX 1: round() before comparing (for display / low precision needs)
a = 0.1 + 0.2
print(round(a, 10) == round(0.3, 10))   # True

# FIX 2: math.isclose() - the recommended way for most comparisons
import math

print(math.isclose(0.1 + 0.2, 0.3))                         # True
print(math.isclose(0.1 * 3, 0.3))                           # True

# isclose() parameters:
# rel_tol - relative tolerance (default 1e-9): relative to magnitude of the values
# abs_tol - absolute tolerance (default 0.0): fixed minimum gap
print(math.isclose(100.0, 100.0000001, rel_tol=1e-6))       # True
print(math.isclose(0.0, 0.0000001, abs_tol=1e-5))           # True

# When to use abs_tol vs rel_tol:
# abs_tol - use when comparing values near zero (rel_tol breaks down near 0)
# rel_tol - use for general magnitude-relative comparisons

# FIX 3: decimal module for exact decimal arithmetic
from decimal import Decimal

d1 = Decimal("0.1")
d2 = Decimal("0.2")
d3 = Decimal("0.3")

print(d1 + d2)             # 0.3  - exact
print(d1 + d2 == d3)       # True - exact comparison

# FIX 4: work in integers when possible (e.g., money in cents)
price_cents = 10 + 20      # 30 cents instead of 0.10 + 0.20 dollars
print(price_cents == 30)   # True - integers never have precision issues

# Summary of when to use each fix:
# round() before ==      - quick and dirty, low-precision use
# math.isclose()         - general float comparisons (recommended)
# decimal.Decimal        - financial / exact decimal arithmetic
# integer arithmetic     - money, counts, anything naturally discrete
