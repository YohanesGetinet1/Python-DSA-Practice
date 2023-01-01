#!/usr/bin/python3
num1 = int(input("Insert the first number\n\t"))
num2 = int(input("Insert the second number\n\t"))
num3 = int(input("Insert the third number\n\t"))

if num1 > num2 and num1 > num3:
	print(f"{num1} is the largest number")
elif num2 > num1 and num2 > num3:
	print(f"{num2} is largest number")
else:
	print(f"{num3} is largest number")
