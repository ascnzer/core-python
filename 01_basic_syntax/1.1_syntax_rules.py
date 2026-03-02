# 1.1 Syntax Rules
# Chapter 01: Basic Syntax
# Topics covered:
#   - Comments
#   - Indentation
#   - Code blocks
#   - Statements vs expressions
#   - Keywords


# COMMENTS
# Single-line comment 
# Python ignores everything after #
x = 5  # this is an inline comment

# Multi-line: just stack single-line comments
# Line one of explanation
# Line two of explanation


# INDENTATION
# Python uses indentation (4 spaces) instead of curly braces
# Wrong indentation = IndentationError

if True:
    print("This is indented correctly")   # 4 spaces in
    print("Still inside the if block")


# CODE BLOCKS
# A block is a group of statements at the same indentation level
# Blocks start after a colon (:) used with if, for, while, def, class, etc

for i in range(3):
    print(i)
    if i == 1:
        print("one")
print("Loop done")


# STATEMENTS vs EXPRESSIONS
# Expression: produces a value
# Statement: performs an action (does NOT return a value)

# Expressions
2 + 3           # 5
"hello"         # "hello"

# Statements
x = 10          # assignment statement
print(x)        # function call statement
if x > 5:       # compound statement
    pass


# KEYWORDS
# Reserved words for Python 
# We can't use them as variable names

# Full list (as of Python 3.11):
# False, None, True, and, as, assert, async, await,
# break, class, continue, def, del, elif, else, except,
# finally, for, from, global, if, import, in, is,
# lambda, nonlocal, not, or, pass, raise, return,
# try, while, with, yield

import keyword
print(keyword.kwlist)        # prints all keywords
print(len(keyword.kwlist))   # 35 keywords in Python 3.11

# This would cause a SyntaxError:
# for = 10 'for' is a keyword


# Docstrings (triple quotes) used for functions/classes, not really comments
def greet():
    """This is a docstring. It documents what the function does."""
    pass

print(greet.__doc__)  # "This is a docstring..."
