# 2.3 Strings
# Chapter 02: Core Data Types
# Topics covered:
#   - String creation
#   - Indexing
#   - Slicing
#   - String immutability
#   - String Operations
#   - String methods
#   - String formatting
#   - Escape characters
#   - Unicode handling


# STRING CREATION
# A string is an ordered sequence of characters
# Strings are created with single quotes, double quotes, or triple quotes

s1 = 'hello'
s2 = "world"
s3 = '''This is a
multi-line string'''
s4 = """Also
multi-line"""

print(type(s1))    # <class 'str'>
print(s3)          # This is a
                   # multi-line string

# Single vs double quotes - no difference, pick one and stay consistent
# Use the other to avoid escaping
s5 = "it's easy"       # single quote inside double - no escape needed
s6 = 'say "hello"'     # double quote inside single - no escape needed

# Empty string
empty = ""
print(len(empty))  # 0

# str() converts other types to string
print(str(42))     # "42"
print(str(3.14))   # "3.14"
print(str(True))   # "True"


# INDEXING
# Access individual characters using their position (index)
# Python uses zero-based indexing

word = "python"
#        p  y  t  h  o  n
# index  0  1  2  3  4  5
# neg   -6 -5 -4 -3 -2 -1

print(word[0])     # p   - first character
print(word[1])     # y
print(word[-1])    # n   - last character (negative index counts from end)
print(word[-2])    # o

# IndexError if out of range
# print(word[10])  # IndexError: string index out of range

# len() returns number of characters
print(len(word))   # 6


# SLICING
# Extract a substring using [start:stop:step]
# start  - index to begin at (inclusive), default 0
# stop   - index to end at (exclusive), default len(s)
# step   - how many characters to skip, default 1

s = "abcdefgh"

print(s[2:5])      # cde   - index 2, 3, 4 (stop is exclusive)
print(s[:3])       # abc   - from start to index 2
print(s[3:])       # defgh - from index 3 to end
print(s[:])        # abcdefgh - full copy

# With step
print(s[::2])      # aceg  - every second character
print(s[1::2])     # bdfh  - every second, starting at index 1
print(s[::-1])     # hgfedcba - reversed (step of -1)

# Slicing with negative indices
print(s[-3:])      # fgh   - last 3 characters
print(s[:-2])      # abcdef - everything except last 2

# Out-of-range slices do NOT raise errors
print(s[2:100])    # cdefgh - just goes to end


# STRING IMMUTABILITY
# Strings cannot be changed after creation
# Any operation that "modifies" a string actually creates a NEW string

s = "hello"
# s[0] = "H"    - TypeError: 'str' object does not support item assignment

# To change a string, build a new one
s = "H" + s[1:]      # "Hello" - creates a new string object
print(s)

# This means strings are safe to share 
a = "hello"
b = a              # b points to same object
b = b + "!"        # b now points to a NEW string
print(a)           # hello   - a is unaffected
print(b)           # hello!


# STRING OPERATIONS
# Strings support two direct operators: + for joining and * for repeating

# CONCATENATION
# The + operator joins two or more strings into one new string

first = "hello"
last  = "world"

result = first + " " + last
print(result)              # hello world

# Concatenating multiple strings
full = "py" + "th" + "on"
print(full)                # python

# Concatenation always requires strings - mixing types causes TypeError
# print("Score: " + 99)   - TypeError: can only concatenate str (not "int") to str
# Fix: convert to str first
score = 99
print("Score: " + str(score))   # Score: 99

# += works too (creates a new string, reassigns the variable)
message = "hello"
message += " there"
message += "!"
print(message)             # hello there!

# MULTIPLICATION
# The * operator repeats a string a given number of times

line  = "-" * 30
print(line)                # ------------------------------ (30 dashes)

bang  = "ha" * 3
print(bang)                # hahaha

# Useful for formatting output
title = "REPORT"
print("=" * 20)
print(title.center(20))
print("=" * 20)
# ====================
#        REPORT
# ====================

# Multiply by zero or negative returns an empty string
print("abc" * 0)           # ""   - empty string
print("abc" * -5)          # ""   - empty string (no error)

# *= works too
border = "* "
border *= 5
print(border)              # * * * * *


# STRING METHODS
# Built-in methods for transforming and inspecting strings
# All return NEW strings (remember: strings are immutable)

s = "  Hello, World!  "

# Case methods
print(s.lower())         # "  hello, world!  "
print(s.upper())         # "  HELLO, WORLD!  "
print(s.title())         # "  Hello, World!  "
print(s.swapcase())      # "  hELLO, wORLD!  "

# Whitespace
print(s.strip())         # "Hello, World!"    - removes leading/trailing whitespace
print(s.lstrip())        # "Hello, World!  "  - left strip only
print(s.rstrip())        # "  Hello, World!"  - right strip only
print(s.strip("! "))     # "Hello, World"     - strip specific characters

# Search and check
t = "hello world"
print(t.find("world"))      # 6     - index of first occurrence (-1 if not found)
print(t.index("world"))     # 6     - same as find but raises ValueError if not found
print(t.count("l"))         # 3     - count occurrences
print(t.startswith("hel"))  # True
print(t.endswith("rld"))    # True
print("ello" in t)          # True  - membership test with 'in'

# Replace and split
print(t.replace("world", "Python"))  # "hello Python"
print(t.split())                     # ['hello', 'world'] - split on whitespace
print(t.split("o"))                  # ['hell', ' w', 'rld'] - split on char
print("a,b,c".split(","))            # ['a', 'b', 'c']

# Join - opposite of split
words = ["hello", "world"]
print(" ".join(words))               # "hello world"
print("-".join(words))               # "hello-world"
print("".join(words))                # "helloworld"

# Check content
print("hello123".isalpha())    # False - has digits
print("hello".isalpha())       # True  - all alphabetic
print("123".isdigit())         # True  - all digits
print("hello123".isalnum())    # True  - all alphanumeric
print("   ".isspace())         # True  - all whitespace

# Padding and alignment
print("hi".center(10))         # "    hi    "
print("hi".ljust(10, "-"))     # "hi--------"
print("hi".rjust(10, "-"))     # "--------hi"
print("42".zfill(5))           # "00042"  - zero-pad


# STRING FORMATTING
# Four ways to embed values inside strings

name  = "ashish"
score = 98.5
rank  = 1

# 1. % formatting (old style, avoid in new code)
print("Name: %s, Score: %.1f" % (name, score))   # Name: ashish, Score: 98.5

# 2. str.format() 
print("Name: {}, Score: {}".format(name, score))          # positional
print("Name: {0}, Rank: {1}".format(name, rank))          # indexed
print("Name: {n}, Score: {s}".format(n=name, s=score))    # named

# 3. f-strings 
print(f"Name: {name}, Score: {score}")           # basic
print(f"Score: {score:.2f}")                     # format spec: 2 decimal places
print(f"Rank: {rank:03d}")                       # zero-padded integer
print(f"Result: {10 * 5}")                       # expressions allowed
print(f"Upper: {name.upper()}")                  # method calls allowed
print(f"Name is {len(name)} chars long")

# f-string format specifiers
pi = 3.14159265
print(f"{pi:.3f}")      # 3.142   - 3 decimal places
print(f"{pi:10.3f}")    # "     3.142"  - width 10, 3 decimals
print(f"{1234567:,}")   # 1,234,567  - thousands separator
print(f"{0.85:.1%}")    # 85.0%   - percentage format

# 4. Template strings (useful for user-supplied input - avoids injection)
from string import Template
t = Template("Hello, $name! Score: $score")
print(t.substitute(name=name, score=score))  # Hello, ashish! Score: 98.5


# ESCAPE CHARACTERS
# Special characters that cannot be typed directly, represented with backslash

print("first line\nsecond line")    # \n - newline
print("col1\tcol2\tcol3")           # \t - tab
print("say \"hello\"")              # \" - literal double quote
print('it\'s fine')                 # \' - literal single quote
print("back\\slash")                # \\ - literal backslash
print("bell\a")                     # \a - bell (alert)
print("\r overwrite")               # \r - carriage return

# Raw strings - backslashes treated as literal characters
# Prefix r before the quote
path    = r"C:\Users\ashish\Documents"   # no need to escape backslashes
pattern = r"\d+\.\d+"                   # useful for regex patterns
print(path)    # C:\Users\ashish\Documents


# UNICODE HANDLING
# Python 3 strings are Unicode by default (UTF-8 internally)
# Every character has a Unicode code point

# Unicode characters work natively
greeting = "namaste"
symbol   = "rupee sign: \u20B9"    # unicode escape: \uXXXX
emoji    = "Python \U0001F40D"     # \UXXXXXXXX for code points > 0xFFFF

print(greeting)   # namaste
print(symbol)     # rupee sign: Rs
print(emoji)      # Python (snake emoji)

# ord() and chr()
print(ord("A"))       # 65   - Unicode code point of 'A'
print(ord("a"))       # 97
print(chr(65))        # A    - character from code point
print(chr(8364))      # euro sign

# Encoding and decoding
s = "hello"
encoded = s.encode("utf-8")       # str - bytes
print(encoded)                    # b'hello'
print(type(encoded))              # <class 'bytes'>

decoded = encoded.decode("utf-8") # bytes - str
print(decoded)                    # hello
print(type(decoded))              # <class 'str'>

# Different encodings
s = "cafe"
print(s.encode("utf-8"))          # b'cafe'   - standard, variable-width
print(s.encode("ascii"))          # b'cafe'   - only handles 0-127

# Characters outside ASCII need utf-8 or similar
hindi = "नमस्ते"
print(hindi.encode("utf-8"))      # bytes representation
print(len(hindi))                 # 6   - number of characters
print(len(hindi.encode("utf-8"))) # 18  - bytes (3 bytes per Hindi char in utf-8)
