#!/usr/bin/python3

n = int(input("Insert the number\n"))

add = 0
avg = 0

for numbers in range(0,n+1,1):
	add = add + numbers
avg = add / numbers

choice = input("to get sum press 's' to get average press 'a' ").lower()
if choice == 's':
	print(f"The sum of numbers in range of 0 and {n} is {add}")
elif choice == 'a':
	print(f"The averge of numbers in rang of 0 and {n} is {avg}")

