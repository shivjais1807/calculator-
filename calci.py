def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Example usage
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (add, subtract, multiply, divide): ")
    print("Result:", calculator(a, b, op))
except ValueError:
      print("Please enter valid numbers.")  