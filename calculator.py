import math

operation = ["+", "-", ":", "/", "*"]

number1 = int(input("First number : "))
operation_options = input(f"Choose your operation : {operation}")
number2 = int(input("Second number : "))

if operation_options== "+":
    addition = number1 + number2
    print(addition)

elif operation_options == "-":
    substraction = number1 - number2
    print(substraction)

elif operation_options == "*":
    multiplication = number1 * number2
    print(multiplication)                                                                                                                                                                           

elif operation_options == "/" or ":":
    division = number1/number2
    print(division)

else:
    print(f"Operation not valid {operation}")