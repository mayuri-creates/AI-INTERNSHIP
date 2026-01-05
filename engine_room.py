
# DATA TYPES & STRINGS

# String example
message = "Python Programming"
print(message)
print(type(message))
# Output:
# Python Programming
# <class 'str'>

# Integer example
age = 21
print(age)
print(type(age))
# Output:
# 21
# <class 'int'>

# Float example
percentage = 82.5
print(percentage)
print(type(percentage))
# Output:
# 82.5
# <class 'float'>

# Boolean example
is_passed = True
print(is_passed)
print(type(is_passed))
# Output:
# True
# <class 'bool'>

# String functions
text = "learning python is easy"
print(text.upper())
print(text.title())
print(text.count('i'))
print(len(text))
# Output:
# LEARNING PYTHON IS EASY
# Learning Python Is Easy
# 2
# 24



# OPERATORS & IF-ELSE


a = 8
b = 3

# Arithmetic operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Comparison operators
print(a > b)
print(a == b)

# Assignment operators
x = 10
x += 5
print(x)

# Logical operators
p = True
q = False
print(p and q)
print(p or q)
print(not p)

# If-else example
marks = 65
if marks >= 40:
    print("Pass")
else:
    print("Fail")



# LIST


subjects = ['Maths', 'Science', 'English']
print(subjects)
print(type(subjects))

print(subjects[0])
print(subjects[-1])

subjects.append('History')
subjects.insert(1, 'Geography')
subjects.remove('Science')
subjects.pop()
print(subjects)

numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)

for sub in subjects:
    print(sub)

data = [[1, 2], [3, 4]]
print(data[1][0])



# TUPLE


colors = ('red', 'green', 'blue')
print(colors)
print(type(colors))

print(colors[1])

nums = (1, 2, 3, 2, 2)
print(nums.count(2))
print(nums.index(3))

for n in nums:
    print(n)

single = (10,)
print(type(single))

t1 = ('A', 'B')
t2 = (1, 2)
print(t1 + t2)

fruits = ('apple', 'banana')
print('apple' in fruits)
print('mango' in fruits)

lst = [10, 20, 30]
tpl = tuple(lst)
print(tpl)



# DICTIONARY


student = {
    "name": "Aarav",
    "roll_no": 101,
    "course": "MCA",
    "year": 2024
}

print(student)
print(type(student))
print(student["name"])
print(len(student))

student["year"] = 2025
print(student)

print(student.get("course"))
print(student.get("address"))

print(student.keys())
print(student.values())

student["college"] = "MET BKC"
student.pop("roll_no")
del student["college"]
print(student)

company = dict(name="Infosys", founded=1981, country="India")
print(company)

for key in company:
    print(key, company[key])

for k, v in company.items():
    print(k, v)

for value in company.values():
    print(value)

for key in sorted(company):
    print(key)



# NESTED DICTIONARY

employee = {
    "emp_id": 501,
    "emp_name": "Neha",
    "skills": {
        "primary": "Python",
        "secondary": "SQL"
    }
}

print(employee)
print(employee["skills"])
print(employee["skills"]["primary"])
print(type(employee["skills"]))



# FUNCTIONS


def greet():
    print("Welcome to Python")

greet()
greet()

def greet_user(name):
    print("Hello", name)

greet_user("Mayuri")
greet_user("Students")

def square(num):
    return num * num

print(square(5))

def add_numbers(a, b):
    return a + b

print(add_numbers(10, 20))

def calculate_distance(speed, time):
    return speed * time

print(calculate_distance(speed=60, time=2))
print(calculate_distance(time=3, speed=40))



# IF STATEMENTS

x = 15
if x > 10:
    print("x is greater than 10")

age = 19
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

num = 7
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

a = 10
b = 25
c = 18

if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")

marks = 72
if marks > 85:
    print("Grade A")
elif marks > 60:
    print("Grade B")
elif marks > 40:
    print("Grade C")
else:
    print("Fail")

y = 45
if y > 30:
    print("Above 30")
    if y > 40:
        print("Above 40")

p = 5
q = 10
print("p is greater") if p > q else print("q is greater")


# LOOPS, CLASSES & MODULES


subjects = ['math', 'physics', 'chemistry', 'biology']
for sub in subjects:
    print(sub)

colors = ('red', 'blue', 'green')
for color in colors:
    print(color)

student = {'name': 'Riya', 'age': 21, 'course': 'MCA'}
for key in student:
    print(key, student[key])

word = "Python"
for ch in word:
    print(ch)

for i in range(5):
    print(i)

languages = ['C', 'C++', 'Python', 'Java']
for index, lang in enumerate(languages):
    print(index, lang)

nums = [2, 4, 6, 8]
def cube(n):
    return n ** 3

for n in nums:
    print(n, cube(n))

class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def info(self):
        print("Name:", self.name)
        print("City:", self.city)

p1 = Person("Amit", "Pune")
p1.info()

import math
print(math.sqrt(16))
print(math.pi)
print(math.log10(100))
