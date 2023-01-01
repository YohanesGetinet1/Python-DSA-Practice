#!/usr/bin/python3
num1 = int(input("Insert the first number\n"))
num2 = int(input("Insert the second number\n"))
print(f"The list of Prime numbers between {num1} and {num2} are:")
for number in range(num1, num2+1):
	if number > 1:
		for x in range(2,number):
			if (number % x) == 0:
				break
		else:
			""" The else keyword in a for loop specifies a block of code to be executed when the loop is finished """
			print(number)
