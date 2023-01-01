#!/usr/bin/python3

def BinarySearch(List,search,low,high):
	while low <= high:
		mid = low + (high - low) // 2
		if List[mid].lower() == search:
			return mid
		elif List[mid] < search:
			low = mid + 1
		else:
			high = mid -1
	return -1


search = input("Enter the Name you want to search").lower()
Name = ["Yohanes","John","Simon","Obama","Rockefeller","Napoleon"]
print(search)
n = len(Name)
high = (n-1)
print(n,high)

result = BinarySearch(Name,search,0,high)

if result != -1:
	print(f"Element {search.capitaliza()} found at index of {mid}")
else:
	print("Element is not found")
