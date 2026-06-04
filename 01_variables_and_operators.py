# Variables and data types
print (" hello, world! ")#string

# variable declarations
#A variable is a name given to a memory location in a program

Name= "Shaikh Humaira Mohd Aasim" #string
age=18                            #integer
DOB=6.7                           #float
old=False                         # boolean (should start with capital)
a= None                           #nonetype 

print("My name is", Name) 
print("I'm", age ,"years old")
print("My DOB is", DOB)

# Data Type
print("Types:", type(age), type(DOB),type(Name))
print(type(old),type(a))

# Type Functions
a = float(1)
print("Convert int to float:", a)
print("Convert string to int:", int("10"))

# Comments
#single line comment
"""
this is a
 mmultiline comment"""
# To comment out multiple lines
# ctrl + (/)

# Operators
#An operator is a symbol that performs a certain operation between operands.
# These work for: Strings, Lists, and Tuples
b = 2 
c = 3

#  Arthematics operators
# (+,-.*,/,%,**)
sum=b+c
diff=b-c
print(sum) #avoid using as it is a built-in function
print(diff)
print("Addition:", b + c)
print("Subtraction:", b - c)
print("Multiplication:", b * c)
print("Division:",b / c)
print("Floor Division:", b // c ) # Discards decimal
print("Modulus:", b % c) # Finds Remainder
print("Exponentiation:", b ** c) #b^c finds Power 

# Relational/Comparison Operators (==, !=, >, <, >=, <=)
#(always give boolen value) 
print("equal:", b == c)
print("unequal:", b != c)
print("greater than or equal:", b >= c)
print(" greather than :", b > c)
print("greater than or equal:", b <= c)
print(" greather than :", b < c) 

# Assignment operators 
# (=, +=, -=, *=, /=, %=, **=)
b += 10 # <= ex adds 10 to b
print(b)

# logical operators 
# (and, not, or )
x = True
y = False

print("AND:", x and y) #ans is true only if both val are true
print("OR:", x or y) #ans is true even if any one val is true
print("NOT x:", not x) # not gives opp to what is true,always in boolens  
print("or:", b == c or b > c) # direct evaluated in expression 
 
# TYPE CONVERSION

# Automatic
d = 2
e = 4.25
print(d + e) #2.0 + 4.25 => 6.25 ie converts int into float
 # error if sum "2"+1

# Manual Casting
f = int("2") # to typecaste string having same data type, we use functions like int or float
g = 4.25 
print(f + g)

# Sequence Operators

# Concatenation (+)
# Joins two sequences of the same type
str1 = "Hello"
str2 = "World"
print("String Concatenation:", str1 + str2)  # HelloWorld

list1 = [1, 2]
list2 = [3, 4]
print("List Concatenation:", list1 + list2)  # [1, 2, 3, 4]

tuple1 = (5, 6)
tuple2 = (7, 8)
print("Tuple Concatenation:", tuple1 + tuple2)  # (5, 6, 7, 8)

# Length (len())
# Returns the number of elements in a sequence
print("Length of string:", len(str1))     # 5
print("Length of list:", len(list1))      # 2
print("Length of tuple:", len(tuple1))    # 2

# Indexing ([])
# Accessing elements using position (0-based)
print("First char in str:", str1[0])      # 'H'
print("First item in list:", list1[0])    # 1
print("First item in tuple:", tuple1[0])  # 5
print("Negative indexing:", str2[-3:-1]) # Negative indexing: start from right i.e e= -1
#for multiple indicing it will consider start not the end

# Slicing ([start:end])
# Returns a subset (start included, end excluded)
print("Slice of string:", str2[1:4])      # 'orl'
print("Slice of list:", list2[0:2])       # [3, 4]
print("Slice of tuple:", tuple2[0:2])     # (7, 8)

# Step Slicing ([start:end:step])
# Can use step to skip or reverse
print("Every 2nd char:", str1[::2])       # 'Hlo'
print("Reverse string:", str1[::-1])      # 'olleH'

#6.6 Membership (in / not in)
print("'e' in str1:", 'e' in str1)        # True
print(2 in list1)                         # True
print(7 not in tuple1)                    # True

# Repetition (*)
print("Repeat string:", str1 * 2)         # HelloHello
print("Repeat list:", list1 * 2)          # [1, 2, 1, 2]
print("Repeat tuple:", tuple1 * 3)        # (5, 6, 5, 6, 5, 6)

# Built-in Functions
name = "Humaira"
print("ASCII of first letter:", ord(name[0]))    # ord() = char to int
print("Character of 97:", chr(97))               # chr() = int to char

# input
name = input("enter your name:")
print("welcome", name) # input is stored in the form of string only
val = int(input("age:")) # to store it in diff form we have to mention it eg "int"
print("age:", val)

# Excersize
# Q1. input 2 numbers & print their sum.
a = int (input("1:"))
b = int (input ("2:"))
print("sum:", a + b)

# Q2. input side of a square & print its area.
side = float (input("val:"))
print("area=", side * side )

# Q3. input 2 floating point numbers & print their average
a1 = float (input("num1:"))
b1 = float (input("num2:"))
print("average = ", (a1 + b1)/ 2 )

# Q4. input 2 int numbers, a and b. 
# Print True if a is greater than or equal to b. If not print False.
print(a1 >= b1)
