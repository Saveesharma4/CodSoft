num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

result = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2 if num2 != 0 else "undefined"
}.get(op, "Invalid operation")

print("Result:", result)
