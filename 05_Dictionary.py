# DICTIONARIES

# A dictionary is a collection of key-value pairs.
# Syntax: {key: value}
#They are unordered, mutable(changeable) & don’t allow duplicate keys

# Empty dictionary
null_dict = {
}

student = {
    "name": "Humaira",
    "age": 18,
    "marks": 92.5,
    "subjects": ["Math", "IT"],
    "learning" : ("python", "sql", "power bi"),
    "pass": True
}
""" Dictionary methods """
print("Name:", student["name"])       # Access value
print("grade:", student.get("grade"))  # Returns None if key doesn't exist
print("learning:", student.get("learning"), "\n") # key according to value 
print("keys:", student.keys(), "\n")     # All keys
print("values:", student.values(), "\n")   # All values
print("items:",student.items(), "\n") # #returns all key, val) pairs as tuples
value = list(student.values())
print("Values:",value, "\n")
print("specific value:", value[0], "\n")

# Adding or updating values & dict
student["grade"] = "A"
student["age"] = 19
student.update(null_dict) # Merges another dictionary
print("updated:", student, "\n")

# Deleting key-value pairs
student.pop("marks")# Removes and returns the value
print("pop marks:", student, "\n")
del student["pass"] #delete 
print("delete pass:", student, "\n")
# student.clear()  # Empties dictionary
# print("clear dict:", student, "\n")

# Looping through dictionary
for key in student:
    print("Looping through dictionary", key, ":", student[key])

# Nested dictionary
users = {
    "user1": {
        "name": "Ali",   
        "email": "ali@email.com"
        },
    "user2": {
        "name": "Zara", 
        "email": "zara@email.com"
        }
}
print("\n", users["user2"]["name"], "\n")  # Zara

# Defaultdict (from collections)
# Automatically creates a default value for missing keys.
# defaultdict(int) gives 0 for a missing key, No KeyError even if "a" was missing
# Useful for counting without checking if the key exists
from collections import defaultdict
d = defaultdict(int)
d["a"] += 1 
print(d)

# Counter (from collections)
# Counts the frequency of elements automatically.
# Works with strings, lists, tuples, etc.
# Returns a dictionary-like object with item counts.
from collections import Counter
s = "banana"
count = Counter(s)
print(count)  # {'a': 3, 'b': 1, 'n': 2}

#Excersizes
# Q1. Store following word meanings in a python dictionary :
Dictionary = {
    "cat" : "a small animal",
    "table": ["a piece of furniture", "list of facts & figures"] 
}
print("Dictionary:",Dictionary, "\n")

# 2. enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {
    "English" : input("enter your marks in English:"),
}
marks["Biology"] = input("enter your marks in Biology:") # Method 1
marks.update({"Maths": input("enter your marks in maths:")})#Method 2
print(marks)