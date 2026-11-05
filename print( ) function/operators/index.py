# Operators in Python | Siva's Tech
# Part 1: Arithmetic, Assignment, Comparison, Logical
# Part 2: Identity, Membership, Bitwise
#
# Run:  python index.py
# The practice programs at the bottom use input(), so they are
# functions. Uncomment a call at the end of the file to try one.
 
 
# ======================================================
# PART 1
# ======================================================
print("===== PART 1 =====")
 
# ---------- 1. Arithmetic Operators ----------
print("\n--- Arithmetic Operators ---")
a = 10
b = 3
print("Add:", a + b)             # 13
print("Sub:", a - b)             # 7
print("Mul:", a * b)             # 30
print("Div:", a / b)             # 3.3333333333333335
print("Floor Div:", a // b)      # 3
print("Modulus:", a % b)         # 1
print("Power:", a ** b)          # 1000
 
# ---------- 2. Assignment Operators ----------
print("\n--- Assignment Operators ---")
x = 10
print("x =", x)                  # 10
x += 3
print("x += 3 ->", x)            # 13
x -= 6
print("x -= 6 ->", x)            # 7
x *= 4
print("x *= 4 ->", x)            # 28
x /= 4
print("x /= 4 ->", x)            # 7.0
 
# ---------- 3. Comparison Operators ----------
print("\n--- Comparison Operators ---")
a = 10
b = 3
print("a == b:", a == b)         # False
print("a != b:", a != b)         # True
print("a > b:", a > b)           # True
print("a < b:", a < b)           # False
print("a >= 10:", a >= 10)       # True
print("a <= b:", a <= b)         # False
 
# ---------- 4. Logical Operators ----------
print("\n--- Logical Operators ---")
age = 20
has_id = True
print(age >= 18 and has_id)      # True
print(age < 18 or has_id)        # True
print(not has_id)                # False
 
# ---------- Common Mistakes (Part 1) ----------
print("\n--- Common Mistakes (Part 1) ---")
y = 5
print(y == 5)                    # True  (== compares, = assigns)
print(7 / 2)                     # 3.5   (/ gives a decimal)
print(7 // 2)                    # 3     (// drops the decimal)
 
# ---------- Interview Questions (Part 1) ----------
print("\n--- Interview Questions (Part 1) ---")
print(10 // 3)                   # 3
print(10 % 3)                    # 1
print(2 ** 3)                    # 8
 
 
# ======================================================
# PART 2
# ======================================================
print("\n===== PART 2 =====")
 
# ---------- 5. Identity Operators ----------
print("\n--- Identity Operators ---")
a = [1, 2]
b = [1, 2]
c = a
print(a is c)                    # True  (same object)
print(a is b)                    # False (different objects)
print(a == b)                    # True  (same values)
print(a is not b)                # True
 
# ---------- 6. Membership Operators ----------
print("\n--- Membership Operators ---")
fruits = ["apple", "mango"]
print("apple" in fruits)         # True
print("grape" in fruits)         # False
print("grape" not in fruits)     # True
print("py" in "python")          # True
 
# ---------- 7. Bitwise Operators ----------
print("\n--- Bitwise Operators ---")
a = 5                            # 0101
b = 3                            # 0011
print(a & b)                     # 1   (0001)
print(a | b)                     # 7   (0111)
print(a ^ b)                     # 6   (0110)
print(~a)                        # -6  (formula: -(a + 1))
print(a << 1)                    # 10  (1010)
print(a >> 1)                    # 2   (0010)
 
# ---------- Common Mistakes (Part 2) ----------
print("\n--- Common Mistakes (Part 2) ---")
print(~5)                        # -6
print(-(5 + 1))                  # -6
print("a" in "cat")              # True
print("A" in "cat")              # False (case-sensitive)
 
# ---------- Interview Questions (Part 2) ----------
print("\n--- Interview Questions (Part 2) ---")
print(5 & 3)                     # 1
print(3 not in [1, 2, 3])        # False
print(~5)                        # -6
 
 
# ======================================================
# PRACTICE PROGRAMS (use input, so they are functions)
# ======================================================
 
def part1_even_or_odd():
    n = int(input("Enter a number: "))
    print("Is even?", n % 2 == 0)
 
 
def part1_login_check():
    username = input("Username: ")
    password = input("Password: ")
    print("Login success:", username == "siva" and password == "1234")
 
 
def part1_vote_eligibility():
    age = int(input("Enter your age: "))
    print("Can vote:", age >= 18)
 
 
def part2_item_in_list():
    items = ["pen", "book", "bag"]
    item = input("Enter item: ")
    print("Available:", item in items)
 
 
def part2_even_or_odd_bitwise():
    n = int(input("Enter a number: "))
    print("Last bit (0 = even, 1 = odd):", n & 1)
 
 
def part2_double_and_half():
    n = int(input("Enter a number: "))
    print("Double:", n << 1)
    print("Half:", n >> 1)
 
 
# Uncomment one line to try a practice program:
# part1_even_or_odd()
# part1_login_check()
# part1_vote_eligibility()
# part2_item_in_list()
# part2_even_or_odd_bitwise()
# part2_double_and_half()
 
