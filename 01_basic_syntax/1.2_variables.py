# 1.2 Variables
# Chapter 01: Basic Syntax
# Topics covered:
#   - What is a variable
#   - Variable assignment
#   - Dynamic typing
#   - Naming conventions
#   - Multiple assignment


# WHAT IS A VARIABLE
# A variable is a name that points to a value stored in memory
# Think of it as a label on a box. The box holds the value

age = 25
name = "ashish"
is_student = True

print(age)        # 25
print(name)       # ashish
print(is_student) # True


# VARIABLE ASSIGNMENT
# Use = to assign. The value on the right is stored, the name on the left points to it

x = 10          # x points to integer 10
x = 20          # x now points to 20 (old value is discarded)
print(x)        # 20

# We can assign the result of an expression
result = 5 * 4 + 2
print(result)   # 22

# Augmented assignment (shorthand)
count = 0
count += 1      # same as: count = count + 1
count -= 1      # same as: count = count - 1
count *= 3      # same as: count = count * 3
print(count)    # 0


# DYNAMIC TYPING
# Python figures out the type at runtime 
# The same variable can hold different types at different times

value = 42
print(type(value))   # <class 'int'>

value = "hello"
print(type(value))   # <class 'str'>

value = 3.14
print(type(value))   # <class 'float'>

value = [1, 2, 3]
print(type(value))   # <class 'list'>

# type() always tells what the variable is holding right now


# NAMING CONVENTIONS
# Rules:
#   - Can contain letters, digits, underscores
#   - Must start with a letter or underscore (NOT a digit)
#   - Case-sensitive: name ≠ Name ≠ NAME
#   - Cannot be a keyword

# valid names
user_name = "ashish"
_private = "hidden"
value1 = 100
MAX_SIZE = 500       # convention for constants

# invalid names
# 1value = 10        - starts with digit
# my-var = 10        - hyphens not allowed
# class = "Math"     - keyword

# Conventions (PEP 8 style guide):
# snake_case         - variables and functions:  user_age, get_name()
# UPPER_SNAKE_CASE   - constants:                MAX_RETRIES = 3
# PascalCase         - classes:                  class BankAccount
# _single_leading    - internal/private use
# __double_leading   - name mangling in classes

first_name = "ashish"
last_name  = "saini"
GRAVITY    = 9.81

print(first_name, last_name)
print(GRAVITY)


# MULTIPLE ASSIGNMENT
# Assign multiple variables on one line

a, b, c = 1, 2, 3
print(a, b, c)      # 1 2 3

# Swap values without a temp variable
a, b = b, a
print(a, b)         # 2 1

# Assign the same value to many variables at once
x = y = z = 0
print(x, y, z)      # 0 0 0
