import os
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    I1 = float(input("Enter your First Number: "))
    op = input("Enter any Operation (+, -, /, *): ")
    I2 = float(input("Enter your Second Number: "))

    if op == "+":
        output = add(I1, I2)
    elif op == "-":
        output = sub(I1, I2)
    elif op == "*":
        output = mul(I1, I2)
    elif op == "/":
        output = div(I1, I2)
    else:
        os.system('cls')
        print("Invalid Choice! Please enter again.")
        return calculator()  # Restart the function if input is invalid

    print(f"{I1} {op} {I2} = {output}")

calculator()
