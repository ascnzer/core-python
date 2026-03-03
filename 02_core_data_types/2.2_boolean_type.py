# 2.2 Boolean Type
# Chapter 02: Core Data Types
# Topics covered:
#   - True and False
#   - Boolean expressions
#   - Truthy and falsy values
#   - Boolean operators
#   - Short-circuit evaluation


# TRUE AND FALSE
# bool is a subclass of int in Python
# True == 1 and False == 0 under the hood

is_active  = True
is_deleted = False

print(type(is_active))       # <class 'bool'>
print(isinstance(True, int)) # True  - bool IS an int subclass

# Because bool is a subclass of int, arithmetic works
print(True + True)           # 2
print(True + False)          # 1
print(True * 5)              # 5
print(False * 100)           # 0

# Useful trick: count True values in a list
results = [True, False, True, True, False]
print(sum(results))          # 3  - counts the Trues


# BOOLEAN EXPRESSIONS
# Any expression that evaluates to True or False
# Comparison operators return bools

x = 10
y = 20

print(x == y)    # False  - equal to
print(x != y)    # True   - not equal to
print(x < y)     # True   - less than
print(x > y)     # False  - greater than
print(x <= 10)   # True   - less than or equal to
print(x >= 11)   # False  - greater than or equal to

# Chained comparisons (Python allows this, unlike most languages)
age = 25
print(18 <= age <= 65)   # True   - readable range check
print(0 < x < 100)       # True   - same as (0 < x) and (x < 100)

# Identity vs equality
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True   - same values
print(a is b)    # False  - different objects in memory
print(a is c)    # True   - c points to the same object as a

# None comparisons - always use 'is', never ==
value = None
print(value is None)     # True   - correct way
print(value == None)     # True   - works but not recommended (PEP 8)


# TRUTHY AND FALSY VALUES
# Every value in Python has an implicit boolean interpretation
# Used in if statements, while loops, boolean operators

# Falsy values - these all evaluate to False in a boolean context:
print(bool(False))    # False
print(bool(0))        # False  - zero integer
print(bool(0.0))      # False  - zero float
print(bool(0j))       # False  - zero complex
print(bool(""))       # False  - empty string
print(bool([]))       # False  - empty list
print(bool(()))       # False  - empty tuple
print(bool(set()))    # False  - empty set
print(bool({}))       # False  - empty dict
print(bool(None))     # False  - None

# Truthy values - everything else evaluates to True:
print(bool(1))        # True
print(bool(-1))       # True   - any non-zero number
print(bool("hi"))     # True
print(bool([0]))      # True   - list with one item (even if item is falsy)
print(bool(" "))      # True   - space is NOT empty

# Practical use: check if a container is non-empty
name = "ashish"
items = [1, 2, 3]

if name:             # same as: if name != ""
    print("Name is set")

if items:            # same as: if len(items) > 0
    print("List has items")


# BOOLEAN OPERATORS
# and, or, not - combine or invert boolean expressions

# not: inverts the truth value
print(not True)      # False
print(not False)     # True
print(not 0)         # True
print(not "hello")   # False

# and: True only if BOTH sides are true
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# or: True if AT LEAST ONE side is true
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# Operator precedence: not > and > or
print(True or False and False)       # True  - and binds tighter: True or (False and False)
print((True or False) and False)     # False - parentheses override
print(not True or True)              # True  - (not True) or True = False or True

# and / or return the actual operand, not just True/False (see short-circuit below)
print(0 and "hello")    # 0      - returns first falsy value
print(1 and "hello")    # hello  - returns last value (both truthy)
print(0 or "hello")     # hello  - returns first truthy value
print("" or 0)          # 0      - returns last value (both falsy)


# SHORT-CIRCUIT EVALUATION
# Python stops evaluating as soon as the result is determined
# and: stops at first False
# or:  stops at first True

# and short-circuits on first falsy value
def check_a():
    print("check_a ran")
    return False

def check_b():
    print("check_b ran")
    return True

result = check_a() and check_b()   # check_b never runs
# output: check_a ran
print(result)                      # False

# or short-circuits on first truthy value
result = check_b() or check_a()    # check_a never runs
# output: check_b ran
print(result)                      # True
