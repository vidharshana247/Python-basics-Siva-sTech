# 🐍 Python Basics – EP 04: Variables

**Channel:** Siva's Tech – Learn • Code • Grow
**Topic:** Variables – Storing data
**Next episode:** Data Types

## Today We Learn

- What is a Variable?
- Why do we use it?
- Syntax
- Create a Variable
- Print / Access
- Different Values
- Change a Value
- Multiple Variables
- Naming Rules

## Timestamps

| Time  | Topic                  |
|-------|------------------------|
| 00:00 | Introduction           |
| 00:33 | What is a Variable?    |
| 00:55 | Creating a Variable    |
| 02:05 | Variable Naming Rules  |
| 02:34 | Changing the Value     |
| 03:22 | Multiple Variables     |
| 05:04 | Variables + print()    |
| 06:13 | Variables + input()    |
| 07:32 | Quick Recap            |

---

## 1. What is a Variable?

A variable is a **named container that stores a value**. Python uses the name to find the value later.

```
name  →  "Siva"
```

---

## 2. Creating a Variable

`=` means **assign**, not "equals".

```python
name = "Siva"
age = 25
print(name)
print(age)
```
**Output:**
```
Siva
25
```

---

## 3. Naming Rules

**Allowed**
- ✓ Start with a letter or `_`
- ✓ Letters, digits, underscores only

**Not allowed**
- ✗ Cannot start with a number
- ✗ No spaces or symbols (`@` `#` `-`)
- ✗ Cannot be a keyword (`if`, `for`)

**Case sensitive:** `age` ≠ `Age`

---

## 4. Changing the Value

A variable can change anytime.

```python
x = 5
x = 10
print(x)
```
**Output:**
```
10
```

---

## 5. Multiple Variables

Assign many at once.

```python
a, b, c = 1, 2, 3
x = y = 0
print(a, b, c, x, y)
```
**Output:**
```
1 2 3 0 0
```

---

## 6. Variables + print()

Mix text and variables with a comma.

```python
name = "Siva"
age = 25
print("Hello", name)
print("Age:", age)
```
**Output:**
```
Hello Siva
Age: 25
```

---

## 7. Variables + input()

`input()` always returns a string.

```python
name = input("Enter your name: ")
print("Welcome", name)
```
**Output:**
```
Enter your name: Siva
Welcome Siva
```

---

## 8. Practice Program

Add two numbers.

```python
a = 10
b = 20
print("Sum =", a + b)
```
**Output:**
```
Sum = 30
```

---

## 9. Common Mistakes

| Wrong | Why |
|-------|-----|
| `1name = "Siva"` | Starts with a number |
| `my name = "Siva"` | Has a space |
| `Name` ≠ `name` | Different variables |

---

## 10. Recap

- ✓ Variable = named container
- ✓ Use `=` to assign a value
- ✓ Follow naming rules

**Try:** store your name and age, then print them.

**Next video:** Data Types →

---

## 11. Quick Quiz

**1. Which is a valid variable name?**
- A) `1name`
- B) `my name`
- C) `my_name`

**2. `x = 5`, then `x = 10`. What does `print(x)` show?**
- A) 5
- B) 10
- C) 15

**3. Are `age` and `Age` the same variable?**
- A) Yes
- B) No

<details>
<summary>Quiz Answers</summary>

1. **C**
2. **B**
3. **B**

</details>

---

*Learn • Code • Grow*