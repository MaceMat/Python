"""
Python Fundamentals Demonstration

This script covers basic concepts:
- Variables and data types
- Basic arithmetic
- Control structures (if/else, loops)
- Functions
- Data structures (list, tuple, dictionary)
- File operations (simple example)
"""

# 1. Variables and Data Types
name = "Alice"
age = 30
height = 5.6
is_student = False

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 2. Basic Arithmetic
a = 10
b = 3
sum_ab = a + b
diff_ab = a - b
prod_ab = a * b
div_ab = a / b

print("\nArithmetic Operations:")
print("Sum:", sum_ab)
print("Difference:", diff_ab)
print("Product:", prod_ab)
print("Division:", div_ab)

# 3. Control Structures
# If/Else
if age < 18:
    print("\nYou are a minor.")
else:
    print("\nYou are an adult.")

# For Loop example
print("\nFor Loop:")
for i in range(5):
    print("Iteration", i)

# While Loop example
print("\nWhile Loop:")
count = 0
while count < 5:
    print("Count is", count)
    count += 1

# 4. Functions
def greet(person):
    """Return a greeting message."""
    return f"Hello, {person}!"

print("\nFunction Call:")
print(greet(name))

# 5. Data Structures
# List
fruits = ["apple", "banana", "cherry"]
print("\nList of Fruits:", fruits)
fruits.append("date")
print("Updated List:", fruits)

# Tuple
coordinates = (10, 20, 30)
print("\nCoordinates Tuple:", coordinates)

# Dictionary
student = {
    "name": "Bob",
    "age": 22,
    "major": "Computer Science"
}
print("\nStudent Dictionary:", student)
print("Student's Major:", student["major"])

# 6. File Operations (write and read a file)
print("\nFile Operations:")
filename = "sample.txt"
# Write to a file
with open(filename, "w") as file:
    file.write("This is a sample text file.\nLearning Python is fun!")

# Read from the file
with open(filename, "r") as file:
    content = file.read()
    print("Content of", filename, ":\n", content)

# 7. Object-Oriented Programming Basics
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Inheritance example: Student inherits from Person
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def greet(self):
        return super().greet() + f" I'm majoring in {self.major}."


# Create instances and demonstrate OOP concepts
person_obj = Person("Charlie", 40)
student_obj = Student("Diana", 21, "Computer Science")

print("\nObject-Oriented Programming Basics:")
print(person_obj.greet())
print(student_obj.greet())

print("\nEnd of Python Fundamentals Demonstration.")