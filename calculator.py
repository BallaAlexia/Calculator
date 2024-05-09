def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def is_valid_operator(operator):
    valid_operator=("+", "-", "*", "/")
    return operator in valid_operator

def number_input():
    while True:
        number=input("Write a number: ")
        if is_number(number):
            return float(number)
        elif number == "quit":
            exit()
        else:
            print("Invalid input, try again.")

def operator_input():
    while True:
        operator=input("Choose an operator (+, -, *, /): ")
        if is_valid_operator(operator):
            return operator
        else:
            print("Invalid operation, choose a valid one.")

def calc(operator, a, b):
    result= None
    if operator == "+":
        result= a + b
    elif operator == "-":
        result= a - b
    elif operator == "*":
        result= a * b
    elif operator == "/":
        if b == 0:
            print("Nope.")
        else:
            result= a / b
    return result 

def simple_calculator():
    while True:
        a=number_input()
        operator=operator_input()
        b=number_input()
        result=calc(operator, a, b)
        print(f"The result is: {result}")

if __name__ == "__main__":
    simple_calculator()

