"""Conditional Statements"""
# Conditional statements are used to control the flow of code
# based on whether a condition is True or False

# if-elif-else (SYNTAX)

age = int(input("Enter your age:"))

if(age >= 18 and age < 60):
    category = "adult" 
elif(age > 13 and age < 18): 
    category = "teenage"
elif(age >= 0 and age <= 13):
    category = "child/infant"
elif(age >= 60):
    category = "old"
else:
    category = "dead/unborn"
print("The person is:", category )
#note
# if checks the first condition, if it is False, Python checks elif condition(s).
# elif can only be used after an if.
# You can have multiple elif statements.
# If all conditions are False, the else block executes.
# else is optional and can be written only once.
# Python uses indentation (4 spaces or a tab) to define code blocks.

#Excersize

# Q1. check if a num entered by the user is even or odd 
num = int(input ("enter the number:"))
if (num % 2 == 0): #or we can write rem=num % 2 and if (rem == 0)
    print ("EVEN")
else:
    print ("ODD")
 
# Q2. find the greatest of 3 num entered by the user
a = int(input ("num A:"))
b = int(input ("num B:")) 
c = int(input ("num C:")) 
if ( a > b and a > c):
    print("a is the greatest number")
elif(b > c and b > a):
    print("b is the greatest number")
else:
    print("c is the greatest number")

# Q3. find if the num is multiple of 7
num = int(input("enter the number:"))
if(num*7):
    print("Yes, the number is multiple of seven")
else:
    print("No, the number is multiple of seven")
