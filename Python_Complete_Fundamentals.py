"""
Python Complete Fundamentals Guide
==================================
A beginner-friendly reference covering the most important Python concepts
with explanations and practical examples.
"""

# ============================================================
# 1. PRINTING AND COMMENTS
# ============================================================
# A comment starts with # and is ignored by Python.
print("Hello, Python!")
print("Name:", "Samaher", "| Age:", 27)

# ============================================================
# 2. VARIABLES AND DATA TYPES
# ============================================================
# Python is dynamically typed, so you do not declare a variable type.
name = "Samaher"          # str
age = 27                  # int
height = 1.65             # float
is_learning = True        # bool
missing_value = None      # NoneType

print(name, age, height, is_learning, missing_value)
print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))
print(type(missing_value))

# Good variable names use snake_case and are descriptive.
student_score = 95
course_name = "Python Basics"

# ============================================================
# 3. TYPE CONVERSION
# ============================================================
number_text = "42"
number = int(number_text)
price = float("19.99")
year_text = str(2026)
boolean_value = bool(1)

print(number + 8)
print(price)
print(year_text)
print(boolean_value)

# ============================================================
# 4. ARITHMETIC OPERATORS
# ============================================================
a = 10
b = 3

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor division
print(a % b)    # Modulus / remainder
print(a ** b)   # Power

# Assignment operators
x = 5
x += 2
x *= 3
print(x)

# ============================================================
# 5. COMPARISON AND LOGICAL OPERATORS
# ============================================================
score = 85

print(score == 85)
print(score != 90)
print(score > 80)
print(score >= 60)
print(score < 100)
print(score <= 85)

# Logical operators: and, or, not
print(score >= 60 and score <= 100)
print(score < 60 or score > 80)
print(not score < 60)

# Membership operators
skills = ["Python", "SQL", "Pandas"]
print("Python" in skills)
print("R" not in skills)

# ============================================================
# 6. STRINGS
# ============================================================
text = "Python Programming"

print(text[0])          # First character
print(text[-1])         # Last character
print(text[:6])         # Slicing
print(text[7:])
print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("Programming", "Basics"))
print(text.startswith("Python"))
print(text.endswith("ing"))
print(len(text))

# Remove spaces from beginning/end
messy_text = "  hello  "
print(messy_text.strip())

# Split and join
sentence = "Python is easy to learn"
words = sentence.split()
print(words)
print("-".join(words))

# f-strings
print(f"My name is {name} and I am {age} years old.")

# ============================================================
# 7. LISTS
# ============================================================
# Lists are ordered, mutable, and allow duplicate values.
skills = ["Python", "SQL", "Machine Learning"]

print(skills)
print(skills[0])
print(skills[-1])
print(skills[1:])

skills.append("Pandas")
skills.insert(1, "NumPy")
skills.extend(["Matplotlib", "Git"])
print(skills)

skills.remove("Git")
removed_item = skills.pop()
print(removed_item)
print(skills)

numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Copy a list
numbers_copy = numbers.copy()

# ============================================================
# 8. TUPLES
# ============================================================
# Tuples are ordered and immutable.
coordinates = (10, 20, 30)
print(coordinates)
print(coordinates[0])

# Tuple unpacking
x_coord, y_coord, z_coord = coordinates
print(x_coord, y_coord, z_coord)

# ============================================================
# 9. SETS
# ============================================================
# Sets are unordered collections of unique values.
set_a = {1, 2, 3, 3}
set_b = {3, 4, 5}

print(set_a)
print(set_a | set_b)    # Union
print(set_a & set_b)    # Intersection
print(set_a - set_b)    # Difference
print(set_a ^ set_b)    # Symmetric difference

set_a.add(10)
set_a.discard(2)
print(set_a)

# ============================================================
# 10. DICTIONARIES
# ============================================================
# Dictionaries store key-value pairs.
student = {
    "name": "Samaher",
    "age": 27,
    "field": "Data Science"
}

print(student)
print(student["name"])
print(student.get("field"))

student["city"] = "Riyadh"
student["age"] = 27

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)

# ============================================================
# 11. CONDITIONAL STATEMENTS
# ============================================================
score = 92

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Needs Improvement"

print(grade)

# Nested condition
age = 27
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")

# Ternary / conditional expression
status = "Adult" if age >= 18 else "Minor"
print(status)

# ============================================================
# 12. FOR LOOPS
# ============================================================
for skill in skills:
    print(skill)

for number in range(1, 6):
    print(number)

# enumerate gives index + value
for index, skill in enumerate(skills, start=1):
    print(index, skill)

# Iterate over dictionary
for key, value in student.items():
    print(key, value)

# ============================================================
# 13. WHILE LOOPS
# ============================================================
count = 1

while count <= 5:
    print(count)
    count += 1

# ============================================================
# 14. BREAK, CONTINUE, PASS
# ============================================================
for number in range(1, 10):
    if number == 3:
        continue
    if number == 7:
        break
    print(number)

# pass is a placeholder
if True:
    pass

# ============================================================
# 15. FUNCTIONS
# ============================================================
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Samaher"))


def calculate_area(width, height):
    return width * height

print(calculate_area(5, 4))

# Default parameter
def introduce(name, field="Data Science"):
    return f"{name} studies {field}."

print(introduce("Samaher"))

# Keyword arguments
print(introduce(field="AI", name="Samaher"))

# *args allows multiple positional arguments
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4, 5))

# **kwargs allows multiple keyword arguments
def show_profile(**info):
    for key, value in info.items():
        print(key, value)

show_profile(name="Samaher", age=27, field="Data Science")

# ============================================================
# 16. LOCAL AND GLOBAL SCOPE
# ============================================================
global_value = 100


def scope_example():
    local_value = 50
    print(local_value)
    print(global_value)

scope_example()

# ============================================================
# 17. LAMBDA FUNCTIONS
# ============================================================
square = lambda number: number ** 2
print(square(6))

# ============================================================
# 18. MAP, FILTER, SORTED
# ============================================================
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda n: n ** 2, numbers))
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
descending = sorted(numbers, reverse=True)

print(squared)
print(even_numbers)
print(descending)

# ============================================================
# 19. LIST / SET / DICTIONARY COMPREHENSIONS
# ============================================================
squares = [n ** 2 for n in range(1, 6)]
evens = [n for n in range(10) if n % 2 == 0]
unique_squares = {n ** 2 for n in range(1, 6)}
square_lookup = {n: n ** 2 for n in range(1, 6)}

print(squares)
print(evens)
print(unique_squares)
print(square_lookup)

# ============================================================
# 20. ZIP
# ============================================================
names = ["Sara", "Nora", "Layan"]
scores = [90, 88, 95]

for student_name, student_score in zip(names, scores):
    print(student_name, student_score)

# ============================================================
# 21. EXCEPTION HANDLING
# ============================================================
try:
    value = int("25")
    result = 100 / value
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(result)
finally:
    print("Finished")

# Raise your own exception
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

print(set_age(27))

# ============================================================
# 22. FILE HANDLING
# ============================================================
# Common modes:
# r = read
# w = write / overwrite
# a = append
# x = create new file

with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Python is easy to read.\n")
    file.write("This is a second line.")

with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# ============================================================
# 23. JSON
# ============================================================
import json

profile = {
    "name": "Samaher",
    "age": 27,
    "field": "Data Science"
}

json_text = json.dumps(profile, indent=2)
print(json_text)

restored_profile = json.loads(json_text)
print(restored_profile["name"])

# ============================================================
# 24. MODULES AND IMPORTS
# ============================================================
import math
from statistics import mean

print(math.sqrt(81))
print(math.ceil(4.2))
print(math.floor(4.9))
print(mean([10, 20, 30]))

# ============================================================
# 25. USEFUL BUILT-IN FUNCTIONS
# ============================================================
values = [4, 8, 2, 10]

print(len(values))
print(sum(values))
print(min(values))
print(max(values))
print(round(3.14159, 2))
print(abs(-10))
print(any([False, True, False]))
print(all([True, True, True]))

# ============================================================
# 26. ITERATORS
# ============================================================
items = ["Python", "SQL", "Pandas"]
iterator = iter(items)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# ============================================================
# 27. GENERATORS
# ============================================================
def countdown(number):
    while number > 0:
        yield number
        number -= 1

for value in countdown(3):
    print(value)

# ============================================================
# 28. OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================
class Student:
    """Simple class representing a student."""

    def __init__(self, name, field):
        self.name = name
        self.field = field

    def introduce(self):
        return f"{self.name} studies {self.field}."

student_object = Student("Samaher", "Data Science")
print(student_object.name)
print(student_object.introduce())

# ============================================================
# 29. INHERITANCE
# ============================================================
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}."


class DataScientist(Person):
    def role(self):
        return "Builds data-driven solutions."


person = DataScientist("Samaher")
print(person.introduce())
print(person.role())

# ============================================================
# 30. DATACLASSES
# ============================================================
from dataclasses import dataclass


@dataclass
class Course:
    name: str
    hours: int


course = Course("Python", 20)
print(course)

# ============================================================
# 31. REGULAR EXPRESSIONS
# ============================================================
import re

contact_text = "Contact: student@example.com"
email_match = re.search(r"[\w.-]+@[\w.-]+", contact_text)

if email_match:
    print(email_match.group())

# ============================================================
# 32. DATE AND TIME
# ============================================================
from datetime import date, datetime, timedelta

sample_date = date(2026, 8, 30)
print(sample_date)
print(sample_date.year)

now = datetime.now()
print(now)
print(now + timedelta(days=7))

# ============================================================
# 33. RANDOM VALUES
# ============================================================
import random

random.seed(42)
print(random.randint(1, 10))
print(random.choice(["Python", "SQL", "R"]))

# ============================================================
# 34. NUMPY BASICS
# ============================================================
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)
print(array * 2)
print(array.mean())
print(array.sum())
print(array.min())
print(array.max())
print(array.shape)
print(array.dtype)

matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix)
print(matrix.shape)
print(matrix.reshape(2, 3))

# Boolean filtering
print(array[array > 2])

# ============================================================
# 35. PANDAS BASICS
# ============================================================
import pandas as pd

student_data = {
    "Name": ["Samaher", "Sara", "Nora", "Layan"],
    "Score": [95, 88, 91, 77],
    "Passed": [True, True, True, True]
}

df = pd.DataFrame(student_data)
print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())

# Select a column
print(df["Score"])

# Filter rows
print(df[df["Score"] >= 90])

# Sort values
print(df.sort_values("Score", ascending=False))

# Add a new column
df["Grade"] = ["A", "B", "A", "C"]
print(df)

# Grouping example
print(df.groupby("Grade")["Score"].mean())

# ============================================================
# 36. PYTHON STYLE AND BEST PRACTICES
# ============================================================
# Follow PEP 8 where practical:
# - Use meaningful variable/function names.
# - Use snake_case for variables and functions.
# - Use PascalCase for classes.
# - Use four spaces for indentation.
# - Keep functions focused on one responsibility.
# - Avoid duplicated code.
# - Add docstrings to important functions/classes.
# - Prefer readable code over clever code.


def calculate_average(values):
    """Return the arithmetic mean of a non-empty sequence."""
    return sum(values) / len(values)

print(calculate_average([90, 85, 95]))

# ============================================================
# 37. VIRTUAL ENVIRONMENTS AND PIP
# ============================================================
# These commands are normally run in the terminal, not inside Python:
#
# Create a virtual environment:
# python -m venv .venv
#
# Activate on macOS/Linux:
# source .venv/bin/activate
#
# Activate on Windows:
# .venv\Scripts\activate
#
# Install a package:
# pip install pandas
#
# Save dependencies:
# pip freeze > requirements.txt
#
# Install saved dependencies:
# pip install -r requirements.txt

# ============================================================
# 38. MINI PRACTICE PROJECT
# ============================================================
students = [
    {"name": "Sara", "score": 84},
    {"name": "Nora", "score": 56},
    {"name": "Layan", "score": 93}
]


def classify(score):
    return "Pass" if score >= 60 else "Fail"


for student_record in students:
    result = classify(student_record["score"])
    print(student_record["name"], student_record["score"], result)

average_score = sum(student_record["score"] for student_record in students) / len(students)
print("Average:", round(average_score, 2))

# ============================================================
# KEY TAKEAWAYS
# ============================================================
# 1. Start with variables, types, operators, strings, and collections.
# 2. Learn conditions and loops to control program flow.
# 3. Use functions to make code reusable and organized.
# 4. Handle errors and files safely.
# 5. Understand OOP, modules, generators, and standard-library tools.
# 6. NumPy and pandas are essential foundations for data analysis.
# 7. The best way to learn Python is by practicing small projects.
