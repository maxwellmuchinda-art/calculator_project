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
def clear_history():
    global history, operations_count
    history = []
    operations_count = 0
    print("History cleared.")
def memory_add(value):
    global memory
    memory += (value or 0.0)    
    print("Added to memory.")
def memory_subtract(value):
    global memory
    memory -= (value or 0.0)
    print("Subtracted from memory.")
def memory_recall():
    print(f"Memory = {format_number(memory)}")
    return memory
def memory_clear():
    global memory
    memory = 0.0
    print("Memory cleared.")
def main():
    global last_result
    ops = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus)
    while True:
        print("\nSimple calculator Menu: ")
        print("1) Add")
        print("2) Subtract")
        print("3) Multiply")
        print("4) Divide")
        print("5) Modulus")
        print("6) Show history")
        print("7) Clear History")
        print("8) Memory: M+")
        print("9) Memory: M-")
        print("10) Memory: MR (recall)")
        print("11) Memory: MC (clear)")
        print("12) Show operations count")
        print("0) Exit")
 choice = input("Select option: ").strip()
        if choice == "0":
            print("Goodbye.")
            break
 if choice in ops:
            op_symbol, func = ops[choice]
            n1 = get_number_input("Enter first number: ")
            n2 = get_number_input("Enter second number: ")
            result = func(n1, n2)
 if result is not None:
                last_result = result
                print(f"Result: {format_number(result)}")
            update_history(n1, op_symbol, n2, result)
