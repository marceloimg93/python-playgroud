num1 = input("Enter first number: ")
op = input("Enter operator: ")
num2 = input("Enter second number: ")

num1 = float(num1)
num2 = float(num2)

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "Invalid operator"

print(result)