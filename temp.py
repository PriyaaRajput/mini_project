# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# factorial_calculator.py

def factorial(n):
    """Recursive function to calculate factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main block
if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Please enter a valid integer.")

