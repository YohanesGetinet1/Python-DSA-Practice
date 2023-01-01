#!/usr/bin/python3

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    return n1 / n2


def mul(n1, n2):
    return n1 * n2


def modulo(n1, n2):
    return n1 % n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": modulo
}


def calculator():
    num1 = float(input("Insert the first number\n"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operator = input("select operation")
        num2 = float(input("Insert the next number\n"))
        calculation = operations[operator]
        answer = calculation(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")


calculator()
