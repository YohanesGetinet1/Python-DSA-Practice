#!/usr/bin/python3

def fibonacci(n):
	if n < 0:
		print("Invalid Input")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Insert the number"))
result = fibonacci(number)
print(f"The fibonacci series of {number} is {result}")
