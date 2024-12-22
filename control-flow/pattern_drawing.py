#!/usr/bin/env python3

#prompt the user to enter a number
size = int(input("Enter the size of the pattern: "))

#nested loop
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  
    print()  
    row += 1