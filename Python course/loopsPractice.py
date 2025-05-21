# Write a program that checks if a number entered by the user is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Ask the user to input a number and check if it’s positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# Input an age and categorize:
# 0-12: Child, 13-19: Teenager, 20-64: Adult, 65+: Senior
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age.")
elif age <= 12:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teenager.")
elif age <= 64:
    print("You are an Adult.")
else:
    print("You are a Senior.")