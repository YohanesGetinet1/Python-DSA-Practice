#!/usr/bin/python3

num1 = int(input("Insert the first number\n\t"))
num2 = int(input("Insert the second number\n\t"))

gcd = None

for i in range(1, num1 + 1):
    if i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
print(f"The GCD of {num1} and {num2} is {gcd}")

