'''Q.1 Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5,between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line.'''
for i in range(2000,3200+1):
    if (i%7==0) and (i%5!=0):
        print(i,end=",")


'''Q.2 Write a Python program to accept the user's first and last name and then getting them 
printed in the the reverse order with a space between first name and last name.'''
first_name=input("plese enter your first name: ")
last_name =input("please enter your last name: ")
rev_fname=""
rev_lname=""
for char in first_name:
    rev_fname=char+rev_fname

for char in last_name:
    rev_lname=char+rev_lname
print("Reversed first name is: ",rev_fname)
print("Reversed Last name is: ",rev_lname)


'''Q.3 Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r3'''
import math
r=int(input("enter the value for side of Sphere: "))
v=4/3*math.pi*r**3
print(f"volume of sphere is {v}")


