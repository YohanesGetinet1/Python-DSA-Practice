#!/usr/bin/python3

n = int(input("Insert the number"))
factorial = 1

if n < 0:
	print("No factorial for negative number")
elif n == 0:
	print(f"Factorial of {n} is 1")
else:
	for i in range(1, n+1,1):
		factorial = factorial * i
	print(f"the factorial of {n} is {factorial}")

