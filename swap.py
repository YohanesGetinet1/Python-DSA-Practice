#!/usr/bin/python3

def swap():
   num1 = input("Insert the first value\n")
   num2 = input("Insert the second value\n")
   print(f"Before swap first value is { num1 } and \nsecond value is {num2}")
   temp = None
   temp = num1
   num1 = num2
   num2 = temp
   print(f"After swap first value is { num1 } and \nsecond value is {num2}")

swap()
