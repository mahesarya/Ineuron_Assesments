'''Q.1. Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''
for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(5,0,-1):
    for j in range(i-1):
        print("* ",end="")
    print()



'''Q.2. Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: ineuron
Output: norueni
'''
word="ineuron"
new_word=word[::-1]
print(new_word)