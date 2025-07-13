""" Variables and data types """

print (" hello, world! ")#string

#variable declarations
#A variable is a name given to a memory location in a program
Name= "Shaikh Humaira Mohd Aasim" #string
age=17 #integer
DOB=6.7 #float
old=False # boolean (should start with capital)
a= None #nonetype 
print("My name is", Name) 
print("I'm", age ,"years old")
print("My DOB is", DOB)

#Data Type
print(type(age), type(DOB),type(Name))
print(type(old),type(a))

#single line comment
"""
this is a
 mmultiline comment"""
# To comment out multiple lines
# we should ctrl + forwardslash (/)
# them after selecting

"""Operators"""
#An operator is a symbol that performs a certain operation between operands.
b=2 
c=3

# 1. Arthematics operators
# (+,-.*,/,%,**)
sum=b+c
diff=b-c
print(sum) #avoid using as it is a built-in function
print(diff)
print("sum:", b+c)
print("diff:", b - c)
print("multi:", b * c)
print("div:",b / c)
print("modulus:", b % c) # Finds Remainder
print("exponentiation:", b ** c) #b^c finds Power 

# 2. Relational/comparison operators 
#(always give boolen value) 
# (==,!=,>=,<=,<,>)
print("equal:", b == c)
print("unequal:", b != c)
print("greater than or equal:", b >= c)
print(" greather than :", b > c) 

# 3. Assignment operators 
# (=, +=, -=, *=, /=, %=, **=)
b += 10 # <= ex adds 10 to b
print(b)

# 4. logical operators 
# (and, not, or )
print(not False)
print("not:", not ( b > c) ) # not gives opp to what is true,always in boolens
val1 = True 
val2 = False 
print("and:",val1 and val2) #ans is true only if both val are true 
print("or:", val1 or val2) #ans is true if any one val is true 
print("or:", b == c or b > c) # direct evaluated in expression 
 
"""TYPE CONVERSION"""

# Automatic
d = 2
e = 4.25
print(d + e) #2.0 + 4.25 => 6.25 ie converts int into float
 # error if sum "2"+1

# Manual Casting
f = int("2") # to typecaste string having same data type, we use functions like int or float
g = 4.25 
print(f + g)

"""input"""
name = input("enter your name:")
print("welcome", name) # input is stored in the form of string only
val = int(input("age")) # to store it in diff form we have to mention it eg "int"
print("age:", val)

"""Examples"""

#1. input 2 numbers & print their sum.
a = int (input("1:"))
b = int (input ("2:"))
print("sum:", a + b)

#2.  input side of a square & print its area.
side = float (input("val:"))
print("area=", side * side )

#3. input 2 floating point numbers & print their average
a1 = float (input("num1:"))
b1 = float (input("num2:"))
print("average = ", (a1 + b1)/ 2 )

#4. o input 2 int numbers, a and b. 
# Print True if a is greater than or equal to b. If not print False.
print(a1 >= b1)