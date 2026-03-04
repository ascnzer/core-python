# 3.1 Conditional Statements
# Chapter 03: Control Flow
# Topics covered:
#   - if statement
#   - if-else
#   - if-elif-else
#   - Nested conditionals
#   - Logical combinations


# IF STATEMENT
# Executes a block only if the condition is True
# Condition can be any expression that evaluates to truthy or falsy

age = 20

if age >= 18:
    print("You are an adult")      # runs - condition is True

score = 45
if score < 50:
    print("Below passing")         # runs
    print("Please study more")     # still inside the if block (same indentation)

# If condition is False, the block is skipped entirely
temperature = 30
if temperature < 0:
    print("It is freezing")        # skipped - condition is False

# Any truthy/falsy value works as a condition
name = "ashish"
if name:                           # truthy - non-empty string
    print("Name is set")           # runs

items = []
if items:                          # falsy - empty list
    print("Has items")             # skipped


# IF-ELSE
# Provides an alternative block when the condition is False
# Exactly one of the two blocks always runs

age = 16

if age >= 18:
    print("Can vote")
else:
    print("Cannot vote yet")       # runs - age is 16

# if-else as a decision - one path always taken
balance = 1000
withdrawal = 500

if withdrawal <= balance:
    balance -= withdrawal
    print("Withdrawal successful")
else:
    print("Insufficient funds")

print(f"Balance: {balance}")       # Balance: 500

# Ternary (one-line) if-else
# value_if_true if condition else value_if_false
status = "adult" if age >= 18 else "minor"
print(status)                      # minor

# Ternary for assignments
x = 10
y = 20
maximum = x if x > y else y
print(maximum)                     # 20


# IF-ELIF-ELSE
# Chain multiple conditions - only the FIRST matching branch runs
# elif is short for "else if"
# The final else is optional - catches everything not matched above

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)                       # C - matches the third condition

# Order matters - first match wins
x = 15
if x > 10:
    print("greater than 10")       # runs - matched here first
elif x > 5:
    print("greater than 5")        # skipped - never reached
elif x > 0:
    print("positive")              # skipped - never reached

# Without else, nothing prints if no condition matches
day = "Saturday"

if day == "Monday":
    print("Start of work week")
elif day == "Friday":
    print("End of work week")
elif day == "Saturday" or day == "Sunday":
    print("Weekend!")              # runs
# no else - that's fine


# NESTED CONDITIONALS
# if statements inside other if statements
# Use sparingly - deep nesting hurts readability

age    = 25
income = 50000
credit = 720

# Nested approach
if age >= 18:
    if income >= 30000:
        if credit >= 700:
            print("Loan approved")     # runs
        else:
            print("Credit score too low")
    else:
        print("Income too low")
else:
    print("Must be 18 or older")

# Flatter alternative using logical operators (usually preferred)
if age >= 18 and income >= 30000 and credit >= 700:
    print("Loan approved")             # runs
else:
    print("Loan denied")

# Sometimes nesting makes logical sense
user_role = "admin"
is_active = True
action    = "delete"

if user_role == "admin":
    if is_active:
        if action == "delete":
            print("Admin deleted the record")   # runs
        else:
            print("Admin performed:", action)
    else:
        print("Account is inactive")
else:
    print("Permission denied")


# LOGICAL COMBINATIONS
# Combine conditions using and, or, not
# Allows complex decisions without deep nesting

age    = 22
member = True
points = 150

# and - all conditions must be True
if age >= 18 and member:
    print("Eligible for member discount")     # runs

# or - at least one condition must be True
has_coupon = False
if member or has_coupon:
    print("Discount applies")                 # runs - member is True

# not - inverts the condition
banned = False
if not banned:
    print("Access granted")                   # runs

# Combining and / or / not
# and binds tighter than or - use parentheses to be explicit
if (age >= 18 and member) or has_coupon:
    print("Checkout eligible")                # runs

# Real-world example: form validation
username = "ashish"
password = "secure123"
email    = "ashish@example.com"

if not username:
    print("Username required")
elif not password or len(password) < 8:
    print("Password must be at least 8 characters")
elif "@" not in email:
    print("Invalid email address")
else:
    print("Registration successful")          # runs - all checks passed

# in / not in operators with conditionals
allowed_roles = ["admin", "editor", "viewer"]
user_role     = "editor"

if user_role in allowed_roles:
    print(f"{user_role} has access")          # runs

blocked_ips = ["192.168.1.5", "10.0.0.3"]
client_ip   = "192.168.1.1"

if client_ip not in blocked_ips:
    print("Connection allowed")               # runs
