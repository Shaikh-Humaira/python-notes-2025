"""List""" 
#  Lists are ordered, mutable (changeable) collections.
#  Defined using square brackets [].
#  Can contain mixed data types.

# Mixed type list
info = ["Humaira", 17, 6.7, True]
print("Info:", info)
print(info)
print(type(info))
print(info[3])
info[1] = 90
print("Mutation:", info) #strings and tuples are immutable while lists are mutable(change value)

"""list methods""" #they are used sperately for str and int 

marks = [43, 54, 70]
marks.append(55.6)              #adds one element at the end
print("1. Append:", marks)
marks.sort( )                   #sorts in ascending order, for strs in alphabatical order
print("2. Sort:", marks)
marks.sort( reverse=True )      #sorts in descending order
print("3. Reverse sort:", marks)
marks.reverse( )                #reverses list 
print("4. Reverse:", marks)
marks.insert( 0, 70 )           #insert element at index (index, element)
print("5. Insert:", marks)
marks.remove(70)                #removes first occurrence of element
print("6. Remove:", marks)
marks.pop( 2 )                  #removes element at index 
print("7. Pop:", marks)

# List Functions
print("Max:", max(marks))
print("Min:", min(marks))
print("Sum:", sum(marks))
print("Average:", sum(marks) / len(marks))

# Checking presence
print(70 in marks)              # True
print(100 in marks)             # False

# Looping through list
for mark in marks:
    print("Mark:", mark) 

#Note: 
# runs once for each item seperately in the list.
# mark is a variable that stores the current item during each iteration.
# for loops make it easy to process all elements of a list without using indexes

# Nested Lists
matrix = [[1, 2], [3, 4], [5, 6]]
print("Element at [1][1]:", matrix[1][1]) #first[]is for outer list & 2nd [] is for inner list

"""Tuples"""
# Tuples are ordered, immutable (unchangeable) collections.
# Defined using round brackets ().
# Can contain mixed data types.

t1 = (5,) # For Tuple with one element (comma is mandatory) without comma it is just an integer       
print(type(t1))

# Check existence
print(5 in t1)     # True
print(10 in t1)    # False

# Nested tuple
t2 = (1, 2, (3, 4), 5)
print("Nested value:", t2[2][1])

# Excersizes:
# Q1. create a tuple of 5 subjects and print each
subjects = ("Math", "Python", "DBMS", "AI", "Statistics")
for subject in subjects:
    print("Subject:", subject)

# Q2. check if a list contains palindrome of elements 
list1 = [1,2,3,2,1]
list2 = list1.copy()
list2.reverse()
if (list1 == list2):
    print("palindromic")
else:
    print("Not palindromic")

# Q3. Count the number of student with the "A" grade in the following tuple
grade1 = ["C", "D", "A", "A", "B", "B", "A"]
print("A Grade Students:", grade1.count("A"))
grade1.sort()
print("Sorted list:", grade1)

# Q4. ask the user to enter names of their 4 fav movies and store them in a list 
mov1 = input("enter first favorate movie: ")
mov2 = input("enter second favorate movie: ")
mov3 = input("enter third favorate movie: ")

movies = [mov1, mov2] #1st method
movies.append(mov3) #2nd method
movies.append(input("enter fourth favorate movie: ")) #3rd method
print(movies)

# Q5. List of your favorite programming languages
languages = ["Python", "C++", "JavaScript", "SQL"]
print("Languages:", languages)
for language in languages:
    print("Language:", language)