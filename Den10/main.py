from art import logo
import os
clear = lambda: os.system('cls')



def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)


    should_continue = True
    while should_continue:
        num1 = float(input("What's your first number? "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue_input = input("Do you want to continue the calculation? Type yes or no: ")
        if should_continue_input == "no":
            should_continue = False
        clear()

calculator()

