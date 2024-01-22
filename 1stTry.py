"""Write a Python program that takes user input for the length and width of a rectangle and calculates its area."""

length=input("Enter the Length :")
width=input("Enter the width :")

area=int(length)*int(width)
print("Area is :",area)


"""Write a function that checks if a given number is prime. Allow the user to input a 
number and provide feedback on whether it's a prime number or not."""

num=int(input("Enter the number"))
flag=0
if num <= 1 :
    print(num,"is not a  prime number")
else:
    for i in range(2,num):
        if num%i==0:
            flag=1
            break  
        else:
            flag=0
if flag==0:
    print("It is a prime number")
else:
    print("Not a prime number")

"""List Manipulation:Create a list of numbers, and write a program to:
#Print the elements in reverse order.
#Calculate the sum of all the numbers.
#Find the maximum and minimum values."""
listed=[1,2,5,8,9,6,4,7,2,6,4,6,11]
#To reverse
print(listed[::-1])
#To find sum
result=sum(listed)
print("sum is :",result)
#max and min
k=max(listed)
y=min(listed)
print("max value is :",k," min value is :",y)


"""String Manipulation:Take a user input string and perform the following operations:
#Display the length of the string.
#Print the string in uppercase.
#Check if the string is a palindrome."""

userword=str(input("Enter your word"))
#to find length
length=len(userword)
print(length)
#to covrt to uppercase
upp=userword.upper()
print(upp)
#to check palindrome
rev_word=userword[::-1]
if rev_word==userword:
    print("It is palindrome")
else:
    print("It is not palindrome")


"""Simple Calculator:
Implement a basic calculator that performs addition, subtraction, multiplication, and division.
Allow the user to input two numbers and select the operation to perform."""
def addition(a , b):
    print("Answer is :",sum(a+b))

def subtraction(a, b):
    print("Answer is :",(a-b))

def multiplication(a, b):
    print("Answer is :",(a*b))

def division(a, b):
    if b!=0:
        print("Answer is :",(a/b))
    else:
        print("Can't divide with zero")

def user_input_here():
     user=int(input("Enter your 1st Number :  "))
     return user


first_input_number = user_input_here()
second_input_number = user_input_here()

print("Choose Your Arithamatic operation\n")

choice=str(input("A-Addition ,S-Subtraction,M-Multiplication,D-Division  :  "))
match choice:
    case 'A':
        print("Chose Addition")
        addition(first_input_number,second_input_number)\
        
    case 'S':
        print("Chose Subtraction")
        subtraction(first_input_number,second_input_number)

    case 'M':
        print("Chose Multiplication")
        multiplication(first_input_number,second_input_number)

    case 'D':
        print("Chose Division")
        division(first_input_number,second_input_number)
    case _:
        print("Invalid attempt -Use only A/S/M/D")


####
"""Question 1: Find the Sum of Array Elements
Write a Python function that takes an array of integers as input and returns the sum of its elements."""

size=int(input("Enter size of array :"))
print("Enter the Array elements")
output_array=[ ]
result=0
for i in range (size):
    temp_input=int(input())
    output_array.append(temp_input)

for i in output_array:
    result+=i

print(result)


"""Question 2: Rotate an Array
Implement a function that rotates the elements of an array to the right by a given number of positions.
For example, if the array is [1, 2, 3, 4, 5] and the rotation is 2, the result should be [4, 5, 1, 2, 3]."""

def rotate_list(lst, n):
    # Loop through the range of n positions to rotate
    for i in range(n):
        # Remove the last element of the list and insert it at the beginning
        lst.insert(0, lst.pop())
    # Return the rotated list
    return lst
 

##user Input
input_array=[]
array_size=int(input("Array size :"))
for i in range(array_size):
    temp=input()
    input_array.append(temp)
##user array before rotation
print(input_array)


# Rotation
rotation_position=int(input("Enter position to be rotated"))
rotated_list = rotate_list(input_array, rotation_position)
print(rotated_list)


"""Question 3: Merge Sorted Arrays
Implement a function that takes two sorted arrays as input and merges them into a single sorted array.
The merged array should contain all elements from both arrays in ascending order."""


def sorter_method(incoming):
    final_array = incoming.copy()
    final_array.sort()
    return final_array

# User input
array_size = int(input("Enter array size: "))

# First user input
print("Enter 1st array elements")
array_one = [int(input()) for _ in range(array_size)]

# Second user input
print("Enter 2nd array elements")
array_two = [int(input()) for _ in range(array_size)]

# Combine arrays and sort
combined_array = array_one + array_two
sorted_array = sorter_method(combined_array)

# Print the final sorted array
print("Final Sorted Array:", sorted_array)