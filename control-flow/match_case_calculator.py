#!/usr/bin/env python3

# Prompt the user for input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()

# Match-case for operations
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("You cannot divide a number by 0.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid input. Please choose a valid operation (+, -, *, /).")
