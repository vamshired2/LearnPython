def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Division by 0 is not allowed, please enter a valid number"
    return num1 / num2

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter the operation you want to perform (add, sub, mul, div): ").strip().lower()

# Performing the selected operation
if operation == "add":
    result = add(num1, num2)
elif operation == "sub":
    result = sub(num1, num2)
elif operation == "mul":
    result = mul(num1, num2)
elif operation == "div":
    result = div(num1, num2)
else:
    result = "Invalid operation! Please enter add, sub, mul, or div."

print("Result:", result)
