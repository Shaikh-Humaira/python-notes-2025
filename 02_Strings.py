'''strings'''
#(can use ',",""")
str1 = "hi \n I name is Humaira! \t I am 17 yrs old." 
str2 = "Apple"
# \n is used for nxt line , \t is used for tab 
print(str1)

"""string operations"""
# 1. concatenation 
print(str1 + str2) #ex hello + world = helloworld

# 2. length 
print(len(str2)) #length: counts all characters like space and digits

# 3. indexing
print(str2 [0]) #it starts with 0 and counts space too we can not change the value of string 

# 4. slicing (accessing part of str)
print("1:", str2[2 : 4]) #lastindex is not included
print("2:", str2[ : 4]) #[0:4]
print("3:", str2[2: ]) # empty space after colon is last str and can be written as [2:len(str2)]
print("4:", str2[-3:-1]) # Negative indexing: start from right i.e e= -1

"""string Function""" 
# (it works for once only and does not make changes in original str)
#some useful str fuctions
print("a:", str1.capitalize()) #capitalize first letter 
print("b:", str1.endswith("old.")) #returns true if string ends with substr
print("c:", str1.replace("i","H")) #replace all occurrences of old with new ie 'i' with 'H' 
print("d:", str1.find("a")) #returns 1st index of 1st occurence
#if word is absent in str output will be -1(as its doesn't exist in index except slicing)
print("e:", str1.count("I")) #counts the occurrence of substr

"""Examples"""
# 1. input user's first name and print its length
a = input("user's first name: ")
print("length of first name :", len(a))

# 2. find the occurance of $ in string.
str = "$ value is greater than rps. $ is used in multiple countries. Hi $"
print ("occurrence of $ in str:", str.count("$"))

