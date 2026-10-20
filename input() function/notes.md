# 🐍 Python Basics – EP 03: input() Function

**Channel:** Siva's Tech – Learn • Code • Grow
**Next episode:** Variables

## About This Episode

Ever wondered how a Python program actually "listens" to you? That's exactly what this episode is about: the `input()` function!

We break it down piece by piece:

- What exactly `input()` does
- Why every interactive program needs it
- The basic syntax (super simple!)
- Taking text vs. number inputs
- Live examples with real outputs
- The `int()` + `input()` combo every beginner should know

No jargon, no rush. Just clear, beginner-friendly explanations you can follow along and practice with immediately.

---

## 1. What is input()?

The `input()` function is used to get information or a value from the user.

## 2. Why do we use input()?

We use `input()` to make our programs interactive by allowing the user to enter their own values.

## 3. Basic Syntax

```python
input()
```

---

## Examples

### 4. Getting Text from the User
```python
name = input("Enter your name: ")
print(name)
```
**Output:**
```
Enter your name: Dharshu
Dharshu
```
The program asks the user to enter their name and then displays the entered name.

### 5. input() with a Message
```python
name = input("What is your name? ")
print("Hello", name)
```
**Output:**
```
What is your name? Dharshu
Hello Dharshu
```
We can give a message inside `input()` to tell the user what to enter.

### 6. Taking a Number as Input
```python
age = int(input("Enter your age: "))
print(age)
```
**Output:**
```
Enter your age: 20
20
```
By default, `input()` returns the value as a **string**. If we want to use the input as an integer, we can use `int()`.

### 7. Simple Calculation
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```
**Output:**
```
Enter first number: 10
Enter second number: 20
30
```
The user enters two numbers, and the program adds them.

### 8. One More Example: Name & Age
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
```
**Output:**
```
Enter your name: Dharshu
Enter your age: 20
Name: Dharshu
Age: 20
```
Here, we get both text and numerical information from the user.

---

## ⭐ Important Point

`input()` always returns the user's input as a **string**.

---

**Tags:** `#Python` `#PythonBasics` `#InputFunction` `#LearnPython` `#PythonForBeginners` `#CodingJourney` `#SivasTech` `#PythonTutorial`