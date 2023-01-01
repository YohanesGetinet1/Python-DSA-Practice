#!/usr/bin/python3
subject = ["Python","Virtualization","Web","ios","Android","System software"]
n = len(subject)
k = input("Enter the Subject you want to access ").lower()

def LinearSearch(subject, n ,k):
    
    print(f"Length of the data strcture{type(subject)} is",n)
    
    for i in range(0,n):
        if subject[i].lower() == k:
            return i
    return -1
        
checker = LinearSearch(subject,n,k)

if checker == -1:
    print("Subject not found")
else:
    print("Subject found at index",checker)



