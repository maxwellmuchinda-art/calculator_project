# lab1_calculator.py
# ICT111 - Lab 1 Python Calculator
# GROUP 9
# lab1_calculator.py
history = []
operations_count = 0
memory = 0.0
last_result = None
def format_number(x):
    if x is None:
        return "Error"
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)
def add(a, b):
    return a + b
def sub(a, b):
    return a - b 
def multiply(a, b):
    return a * b 
def divide(a, b):
if b ==0:
    print("Error: Division by zero.")
    return None
return a/ b
def modulus(a, b):
    if b == 0:
        print("Error: Modulus by zero.")
        return None
    return a % b
def get_number_input(prompt):
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print("Invalid input. Please enter a number.")
def update_history(num1, op, num2, result):
    global history, operations_count
    entry = f"{format_number(num1)} {op} {format_number(num2)} = {format_number(result)}"
    history.append(entry)
    if result is not None:
        operations_count += 1
def display_history():
    if not history:
        print("No calculations yet.")
        return
    print("\nCalculation history:")
    for i, e in enumerate(history, 1):
        print(f"{i}. {e}")
    print()

