"""Conditional Statements"""

# if-elif-else (SYNTAX)

age = int(input("enter your age:"))

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

#NOTES
#a. If if's statement isn't true then we check elif-if/ 2nd if statement(to write elif statement, if statement is mandatory)
#b. You can write as many if/elif statements as needed
#c. If all if/elif statements, the else statement will execute, its can be written once only
#d. Python uses indentation(tab/4 spcaes)



#Examples

# 1. check if a num entered by the user is even or odd 
num = int(input ("enter the number:"))
if (num % 2 == 0): #or we can write rem=num % 2 and if (rem == 0)
    print ("EVEN")
else:
    print ("ODD")
 
# 2. find the greatest of 3 num entered by the user
a = int(input ("num A:"))
b = int(input ("num B:")) 
c = int(input ("num C:")) 
if ( a > b and a > c):
    print("a is the greatest number")
elif(b > c and b > a):
    print("b is the greatest number")
else:
    print("c is the greatest number")

# 3. find if the num is multiple of 7
numb = int(input("enter the number:"))
if(num*7):
    print("Yes, the number is multiple of seven")
else:
    print("No, the number is multiple of seven")
