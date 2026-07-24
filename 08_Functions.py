#Functions 
#Block of statements that perform a specific task.
#Can be used throughout the program
#Helps break the program into smaller parts 
#more organized & manageable
#function creation is not compulsory

#Define the function
#Built-in Functions: print( ), len( ), type( ), range( )

#Parameters:variable written inside parenthese with the name of function some work
#(a,b) are parameters          
def calc_sum(a, b): 
    return (a + b)

#Arguments: values passed to the parameters while calling the function
#eg (5,10) are arguments
print(calc_sum(5,10)) # funtion call(only using the name); #15
print(calc_sum(5.3,4.2)) #9.5
print(calc_sum("Hello","world")) #Helloworld
# we can use same function multiple time for different value of different types 

#default Parameters: Assigning a default value to parameter, which is used when no argument is passed. 
# eg (a=1, b=3, c=2), ("hello")
def null_function():
    print("hello")

null_function() #hello
null_function() #hello

#Arbitary Arguments: Allow a function to accept any number of inputs
#eg(*name)
#We can excess required value by using index number
def hello(*name):
    print ("hello, my name is",name[2])

hello("john","lisa","peter") #hello, my name is peter

#Excersizes 
#Q1. WAF to print the length of a list. ( list is the parameter)
cities = ["delhi", "mumbai", "pune", "chennai"]
countries = ["india", "cannada", "pakistan"]
def p_len(list):
    print("Q1.", len(list))

p_len(cities) #Q1. 4
p_len(countries) #Q1. 3

#Q2. WAF to print the elements of a list in a single line. ( list is the parameter)
def p_element(list):
    for item in list:
        print("Q2. ",item, end="")

p_element(cities ) #Q2.  delhi mumbai pune chennai
p_element(countries) #Q2.  india cannada pakistan

#Q3. WAF to find the factorial of n. (n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i 
    print("Q3. ", fact)

cal_fact(6) #Q3. 720

#Q4. WAF to convert USD to INR. 
def convertor(v):
    # value = 87.46
    # for i in range(1,v+1):
    #     value *= i 
    # print("Q4. ", v,"USD =", value, "INR")
                #OR
    inr = v * 87.46
    print("Q4. ",v,"USD =", inr,"INR")
convertor(7) #Q4. 7 USD = 612.22 INR

#Q5. check if a num entered by the user is even or odd 
def identifier(num):
    if (num % 2 == 0): 
        print ("Q5. EVEN")
    else:
        print ("Q5.ODD")

identifier(2) #Q5. EVEN

#Q6. WAF to Calculate the avg average of 3 no.
def avg(a, b, c):
    return (a + b + c) / 3

print("Q6. avg:", avg(3, 4, 5)) #Q6. avg: 4.0

