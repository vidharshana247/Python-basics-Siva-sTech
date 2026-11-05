Operators in Python | Notes

Siva's Tech | Python Basics

Code for every example below is in index.py.

What are Operators?
An operator is a symbol that performs an operation.
The values it works on are called operands.
python
10 + 5      # + is the operator, 10 and 5 are operands, result is 15
Types of Operators (7)
#	Type	Operators	Video
1	Arithmetic	+  -  *  /  //  %  **	Part 1
2	Assignment	=  +=  -=  *=  /=	Part 1
3	Comparison	==  !=  >  <  >=  <=	Part 1
4	Logical	and  or  not	Part 1
5	Identity	is  is not	Part 2
6	Membership	in  not in	Part 2
7	Bitwise	&  |  ^  ~  <<  >>	Part 2
PART 1
1. Arithmetic Operators

Values: a = 10, b = 3

Operator	Name	Example	Result
+	Addition	a + b	13
-	Subtraction	a - b	7
*	Multiplication	a * b	30
/	Division	a / b	3.3333333333333335
//	Floor Division	a // b	3
%	Modulus (remainder)	a % b	1
**	Power	a ** b	1000
/ always gives a decimal (float) result.
// drops the decimal part.
% gives the remainder.
2. Assignment Operators

Value: x = 10 before each operation

Operator	Example	Same as	x becomes
=	x = 10	store 10 in x	10
+=	x += 3	x = x + 3	13
-=	x -= 3	x = x - 3	7
*=	x *= 3	x = x * 3	30
/=	x /= 2	x = x / 2	5.0
These are short forms that make code shorter.
/= gives a float, because / always gives a float.
3. Comparison Operators

Values: a = 10, b = 3. The result is always True or False.

Operator	Meaning	Example	Result
==	Equal to	a == b	False
!=	Not equal to	a != b	True
>	Greater than	a > b	True
<	Less than	a < b	False
>=	Greater than or equal	a >= 10	True
<=	Less than or equal	a <= b	False
4. Logical Operators
Operator	Meaning
and	True only if both are True
or	True if at least one is True
not	Reverses the result
python
age = 20
has_id = True
print(age >= 18 and has_id)   # True
print(age < 18 or has_id)     # True
print(not has_id)             # False
Common Mistakes (Part 1)
= stores a value, == compares. x = 5 is not the same as x == 5.
7 / 2 gives 3.5, but 7 // 2 gives 3.
input() always returns a string. Use int() before doing maths.
Interview Questions (Part 1)
Question	Answer
Output of 10 // 3	3
Output of 10 % 3	1
Output of 2 ** 3	8
Difference between = and ==	= assigns a value, == compares two values
PART 2
5. Identity Operators
Operator	Meaning
is	True if both are the same object
is not	True if they are different objects
python
a = [1, 2]
b = [1, 2]
c = a
print(a is c)       # True   (c points to the same list)
print(a is b)       # False  (two separate lists)
print(a == b)       # True   (values are the same)
print(a is not b)   # True
is checks the object, == checks the value.
6. Membership Operators
Operator	Meaning
in	True if the value is present
not in	True if the value is not present
python
fruits = ["apple", "mango"]
print("apple" in fruits)       # True
print("grape" in fruits)       # False
print("grape" not in fruits)   # True
print("py" in "python")        # True
Works on lists, strings, tuples and sets.
7. Bitwise Operators

Values: a = 5 (0101), b = 3 (0011)

Operator	Name	Example	Result
&	AND	a & b	1 (0001)
|	OR	a | b	7 (0111)
^	XOR	a ^ b	6 (0110)
~	NOT	~a	-6
<<	Left shift	a << 1	10 (1010)
>>	Right shift	a >> 1	2 (0010)
& gives 1 only if both bits are 1.
| gives 1 if at least one bit is 1.
^ gives 1 only if the bits are different.
~a = -(a + 1), so ~5 is -6.
a << 1 multiplies by 2, a >> 1 divides by 2.
Common Mistakes (Part 2)
a == b compares values, a is b compares objects. Two equal lists can still be different objects.
~5 is -6, not -5. Remember the formula -(a + 1).
in is case-sensitive. "a" in "cat" is True, "A" in "cat" is False.
Interview Questions (Part 2)
Question	Answer
Output of 5 & 3	1
Output of 3 not in [1, 2, 3]	False
Output of ~5	-6
Difference between is and ==	is checks the same object, == checks the same value
Summary
7 types of operators: Arithmetic, Assignment, Comparison, Logical, Identity, Membership, Bitwise.
/ gives a decimal, // drops it, % gives the remainder.
Comparison operators always give True or False.
is checks the object, == checks the value.
~a = -(a + 1).

Next video: Strings