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
