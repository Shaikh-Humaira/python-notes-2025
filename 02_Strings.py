'''strings'''
#(can use ',",""")
#  Strings are sequences of characters enclosed in quotes
#  Can be created using single, double, or triple quotes

# Example string
name = "Shaikh Humaira"
str1 = '''This is
a multi-line
string.'''

print(name)
print(str1)

# Useful String Methods (it works for once only and does not make changes in original str)
print("UPPERCASE:",name.upper())                            # UPPERCASE
print("lowercase:",name.lower())                            # lowercase
print("Title Case:",name.title())                           # Title Case
print("Capitalize first letter:",name.capitalize())         # Capitalize first letter
print("Index of first 'i':",name.find("i"))                 # 1st index of 1st occurence 'i'
print("Count of 'a':",name.count("a"))                      # Count the occurrence of substr 'a'
print("Replace all 'a' with '@':",name.replace("a", "@"))   # Replace all ccurrences of old with new ie 'a' with '@'
print("Endswith:",name.endswith("ra"))                      # True if string ends with substr
print("Startswith:",name.startswith("Sha"))                 # 
print("Strip:",name.strip())                                # Remove whitespace
print("Split:",name.split(" "))                             # Split by space into list
print("   hello   ".strip())                                # 'hello'

# Escape Characters
print("Hi \nMy name is Humaira! \t I am 17 yrs old." )
#Line 1\nLine 2" nxt line
#Column1\tColumn2" tab 

# String Formatting
# Method 1 - f-strings (recommended)
age = 18
print("My name is {name} and I am {age} years old.")

# Method 2 - format()
print("My name is {} and I am {} years old.".format(name, age))

# Reverse a String
original = "Humaira"
reversed_str = original[::-1]
print("Reversed:", reversed_str) #ariamuH

#Excersize
# Q1. input user's first name and print its length
a = input("user's first name: ")
print("length of first name :", len(a))

# Q2. find the occurance of $ in string.
str = "$ value is greater than rps. $ is used in multiple countries. Hi $"
print ("occurrence of $ in str:", str.count("$"))

# Q3. input user's name and print it in uppercase and find vowels count in it.
user_name = input("Enter your name: ")
print("Name in uppercase:", user_name.upper())
print("Vowel count:", sum(user_name.lower().count(v) for v in "aeiou"))

