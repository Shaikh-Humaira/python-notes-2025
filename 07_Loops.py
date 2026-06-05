"""LOOPS IN PYTHON"""
# Loops are used to repeat a block of code
# Two main types: for loop, while loop


"""FOR LOOP"""
# Syntax: for variable in iterable:
# Iterates(repeats) over a sequence (list, tuple, string, range, dict, etc.)

subjects = ["Python", "SQL", "Power BI", "ML"]
for sub in subjects:
    print("Learning:", sub)
else:
    print("End","\n")  # else block runs only if loop is NOT broken


# range() – returns a sequence of numbers
# range(start (optional, from 0 by default if not present), increments by 1 (by default), stop (before a required number), step (optional, default=1))
for a in range(3):
    print("range:", a)  # 0, 1, 2

for b in range(2, 10, 2):
    print("range(3S):", b,"\n")  # 2, 4, 6, 8


# Nested for loop (Matrix)
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for val in row:
        print("Nested for loop:", val)

# Loop with else
for i in range(3):
    print("Loop with else:", i)
else:                               #Else block runs only if loop is not broken
    print("Loop completed without break.\n")

# pass – null statement/placeholder for future code, does nothing
for i in range(3):
    pass # No operation


"""WHILE LOOP"""
# Syntax: while condition:
# Repeats as long as the condition is True

count = 0           # initialization
while count < 3:    # stopping condition
    print("While Loop:", count,"\n")
    count += 1      # update (prevents infinite loop)

# Infinite loop – dangerous unless condition changes
# while True:
#     print("Runs forever")


"""CONTROL STATEMENTS"""

# break – exits the loop immediately
for g in range(5):
    if g == 4:
        break
    print("Break at 4:", g)

h = 1
while h <= 5:
    print(h)
    if h == 3:
        break
    h += 1
print("Break:End of loop","\n") #break at 3


# continue – skips the current iteration, jumps to next
for i in range(5):
    if i == 2:
        continue
    print("Continue at 2:", i) # 0,1,3,4

i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print("Continue:", i)
    i += 1

# Print only odd numbers using continue
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print("Odd:", i,"\n")
    i += 1


"""ADVANCED LOOP TECHNIQUES"""

# enumerate() – gives index + value while looping
skills = ["Python", "DSA", "ML"]
for index, skill in enumerate(skills, start=1):
    print(f"skill,{index}: {skill}","\n") #serial no + item


# zip() – parallel iteration over two or more iterables
tools = ["Python", "SQL"]
levels = ["Advanced", "Intermediate"]
for tool, level in zip(tools, levels):
    print(f"{tool}: {level}","\n") #like a zipper joins two sides together


# Dictionary Looping 
student = {
    "name": "Humaira",
    "age": 18,
    "grade": "A+"
}

for key in student:                     # keys only
    print("Key:", key)

for val in student.values():            # values only
    print("Value:", val)

for key, val in student.items():        # key-value pairs
    print(f"{key}: {val}","\n")


# List Comprehension – advanced loop in 1 line
# Syntax: [expression for item in iterable if condition]
squares = [x**2 for x in range(5)]
print("Squares:", squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]# With condition
print("Even Squares:", even_squares,"\n")


"""EXERCISES"""

# Q1. Print elements of a list (traversal)
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in num:
    print("Q1. Value:", val)

# Q2. Search for a number x in a list using a loop
x = 49
idx = 0
for val in num:
    if val == x:
        print("Q2. Found", x, "at index:", idx)
    idx += 1

# Q3. Print numbers from 100 to 1 (reverse loop)
for a in range(100, 0, -1):
    print("Q3. Descending:", a)

# Q4. Print the multiplication table of a number n
n = int(input("Enter number: "))
for a in range(1, 11):
    print("Q4.",f"{n} * {a} =", n * a)

# Q5. Print numbers from 1 to 100 using while
c = 1
while c <= 100:
    print("Q5. Number:", c)
    c += 1

# Q6. Multiplication table using while
n = int(input("Multiples of: "))
d = 1
while d <= 10:
    print("Q6.", f"{n} * {d} =", d * n)
    d += 1

# Q7. Print squares of 1–10 using while
e = 1
while e <= 10:
    print(f"Q7. Square of {e}:", e * e)
    e += 1

# Q8. Search for a hero in a list using while
heroes = ["ironman", "thor", "superman", "batman"]
x = "superman"
f = 0
while f < len(heroes):
    if heroes[f] == x:
        print("Q8. Hero found at index:", f)
        break
    else:
        print("Q8. Not found yet...")
    f += 1

# Q9. Find the sum of first n numbers using while
n = 5
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Q9. Sum (1 to n):", total)

# ***Q10. Find factorial of a number using for
m = 5
fact = 1
for i in range(1, m + 1):
    fact *= i
print("Q10. Factorial:", fact)
