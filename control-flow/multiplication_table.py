#!/usr/bin/env python3

#prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))


print(f"Here if the multiplication table for {number}")

for i in range(1,11):
    product = i * number
    print(f"{number} * {i} = {product}")

