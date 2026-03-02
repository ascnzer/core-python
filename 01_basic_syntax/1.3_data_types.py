# 1.3 Data Types Overview
# Chapter 01: Basic Syntax
# Topics covered:
#   - Primitive vs non-primitive types
#   - Mutable vs immutable
#   - Type checking
#   - Type casting
#   - Memory & reference behavior


# PRIMITIVE vs NON-PRIMITIVE
# Primitive (simple, single values):
# int, float, complex, bool, str, NoneType

# Non-primitive (containers - hold multiple values):
# list, tuple, set, dict

# Primitives
age       = 30           # int
price     = 9.99         # float
score     = 4 + 2j       # complex
passed    = True         # bool
username  = "ashish"     # str
nothing   = None         # NoneType

print(type(age))         # <class 'int'>
print(type(price))       # <class 'float'>
print(type(score))       # <class 'complex'>
print(type(passed))      # <class 'bool'>
print(type(username))    # <class 'str'>
print(type(nothing))     # <class 'NoneType'>

# Non-primitives
my_list   = [1, 2, 3]          # list
my_tuple  = (1, 2, 3)          # tuple
my_set    = {1, 2, 3}          # set
my_dict   = {"a": 1, "b": 2}   # dict

print(type(my_list))     # <class 'list'>
print(type(my_tuple))    # <class 'tuple'>
print(type(my_set))      # <class 'set'>
print(type(my_dict))     # <class 'dict'>


# MUTABLE vs IMMUTABLE
# Immutable: value cannot be changed after creation
# Mutable: value can be changed in place

# Immutable types: int, float, bool, str, tuple
s = "hello"
# s[0] = "H"     TypeError: strings don't support item assignment
s = "Hello"    # this is fine - we're creating a NEW string, not changing the old one

t = (1, 2, 3)
# t[0] = 99    - TypeError: tuples don't support item assignment

# Mutable types: list, set, dict
nums = [1, 2, 3]
nums[0] = 99           # lists are mutable
nums.append(4)         # modifies in place
print(nums)            # [99, 2, 3, 4]

d = {"x": 10}
d["x"] = 20            # dicts are mutable
d["y"] = 30            # add new key
print(d)               # {'x': 20, 'y': 30}


# TYPE CHECKING
# Two ways to check type:

x = 42

# 1. type() - tells exactly what type it is
print(type(x))            # <class 'int'>
print(type(x) == int)     # True

# 2. isinstance() - preferred, also handles inheritance
print(isinstance(x, int))         # True
print(isinstance(x, (int, float))) # True - checks against multiple types at once
print(isinstance(x, str))         # False

# Why isinstance() is better:
# It returns True for subclasses too
# Example: bool is a subclass of int
flag = True
print(type(flag) == int)        # False  - misses it
print(isinstance(flag, int))    # True   - catches it correctly


# TYPE CASTING
# Convert a value from one type to another using built-in functions

# int()
print(int("42"))        # 42    str to int
print(int(3.9))         # 3     float to int
print(int(True))        # 1     bool to int
print(int(False))       # 0

# float()
print(float("3.14"))    # 3.14  str to float
print(float(10))        # 10.0  int to float

# str()
print(str(100))         # "100"
print(str(3.14))        # "3.14"
print(str(True))        # "True"

# bool()
print(bool(0))          # False  - zero is falsy
print(bool(1))          # True
print(bool(""))         # False  - empty string is falsy
print(bool("hi"))       # True
print(bool([]))         # False  - empty list is falsy
print(bool([1, 2]))     # True

# list() / tuple() / set()
print(list("abc"))      # ['a', 'b', 'c']
print(tuple([1, 2, 3])) # (1, 2, 3)
print(set([1, 1, 2, 3]))# {1, 2, 3}  - duplicates removed

# Casting that fails (ValueError)
# int("hello")   - ValueError: invalid literal
# float("abc")   - ValueError


# MEMORY & REFERENCE BEHAVIOR
# Variables don't store values - they store references (pointers) to objects in memory
# id() gives the memory address of an object.

a = [1, 2, 3]
b = a              # b points to the SAME list in memory
b.append(4)
print(a)           # [1, 2, 3, 4]  - a is affected 
print(id(a) == id(b))  # True - same object


# Immutables behave differently - Python can reuse small objects
x = 10
y = 10
print(id(x) == id(y))  # True - Python caches small integers (-5 to 256)

x = 1000
y = 1000
print(id(x) == id(y))  # False - large integers are NOT cached

# None is always the same object
a = None
b = None
print(a is b)      # True 
