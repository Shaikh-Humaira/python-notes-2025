
# Recursion
# Function calling itself to solve a smaller version of the same problem
# giving us a benefit of looping through data in order to get a result

# def hello():
#     print("hello")
#     return hello()
# print(hello()) (this will lead to max recurion depth which is around1k)

#advantages
# 1. Simplifies code, by breaking the complex task into small sub- parts
# 2. Makes code more readable, clean & organized
# 3. Useful for tree traversal and graph algorithms
# 4. Sequence generation becomes easier

#Disadvantages
# 1. Take up a lot of memory, as each function call is stored in the call stack until the base case is reached
# 2. Sometimes logic becomes hard to follow
# 3. debugging becomes difficult, as it is hard to keep track of the function calls and their return values

# Q1. reverse number
def show(n):
    if(n==0):  # must- base case(stop condition)    
        return
    print("Q1. ", n)
    show(n-1)# recursive case
    print("Q1. before: END")
show(5) 
print("Q1. after: END")     

#Q2. factorial
def factorial(n):
    if (n == 0 or n == 1):   # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive case, like if n=5 then 5*factorial(4) and so on until base case is reached

print("Q2. ", factorial(5))  # 5*4*3*2*1= 120

#Q3. fibonacci  (sequence of no's where each no is the sum of the two preceding ones  Starting from 0 & 1)
def fibonacci(n):
    if (n <= 0):  # base case 1
        return 0
    elif (n == 1):  # base case 2
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # recursive case

print("Q3.", fibonacci(6))  # 8

#Q4. sum of natural numbers
def sum_natural(n):  
    if (n == 0):  # base case
        return 0
        
    return n + sum_natural(n - 1)  # recursive case

print("Q4.", sum_natural(5))  # 15

# Q5. Indirect recursion example:
def funcA(x):
    if x > 0:   
        print("Q5.", x)
        funcB(x - 1)

def funcB(x):
    if x > 0:
        print("Q5.", x)
        funcA(x - 1)

funcA(3)  # 3 2 1 1 0 (pattern from A and B calls)

# Q6. Tail recursion:
def tail_factorial(n, acc=1):

    if n == 0:
        return acc
    return tail_factorial(n-1, acc*n)

print("Q6.", tail_factorial(5))  # 120 