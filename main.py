def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("Sum:", add(num1, num2))
print("Difference:", subtract(num1, num2))
print("Quotient:", divide(num1, num2))