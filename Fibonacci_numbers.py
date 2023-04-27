# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:58:28 2023

@author: aarsh
"""

# Function to generate Fibonacci numbers
def fibonacci(n):
    # First two terms of Fibonacci series
    a, b = 0, 1
    # List to store the Fibonacci series
    fib_series = []
    # Loop to generate the series
    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Taking input from user
n = int(input("Enter the number of terms: "))

# Calling the fibonacci function
fib_series = fibonacci(n)

# Printing the generated series
print("Fibonacci Series:")
for i in fib_series:
    print(i, end=" ")
