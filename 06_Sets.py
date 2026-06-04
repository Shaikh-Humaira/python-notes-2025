"""SETS"""
# A set is unordered, unindexed collection of unique elements.
# Written with curly braces { }
# No duplicate items allowed (auto-removed)
# Mutable, but elements inside must be immutable (like int, str, tuple)
# Very fast for membership testing (checking if an item exists)

# Empty set
my_set = set()  # NOT {}, because {} creates a dictionary
print("Empty set:", my_set)

fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits,"\n")

# conversion
nums = set([1, 2, 2, 3, 4, 4])
print("list to set:", nums) #Method 1
letters = "hello" 
print("String to set:", set(letters),"\n") #Method 2

# Uncomment to see error:
# invalid_set = { [1, 2], 3 }  #  list is mutable

# ACCESSING ELEMENTS (Membership)
print("Is 'apple' in the fruits set?", "apple" in fruits)
print("Is 'mango' in the fruits set?", "mango" in fruits,"\n")


# ADDING & REMOVING
fruits.add("mango")               # Add one
print("After add:", fruits)

fruits.update(["grape", "kiwi"])  # Add multiple
print("After update:", fruits)

fruits.remove("banana")           # Remove ( error if not found)
print("After remove:", fruits)

fruits.discard("papaya")          # Remove ( no error if not found)
print("After discard:", fruits)

popped_item = fruits.pop()        # Removes random item
print("Popped item:", popped_item)
print("After pop:", fruits)

fruits.clear()  # Empty the set
print("After clear:", fruits,"\n")

# SET OPERATIONS
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union(M1):", A | B)  # OR operator
print("Union(M2):", A.union(B),"\n") #no repetation

print("Intersection(M1):", A & B)  # AND operator
print("Intersection(M2):", A.intersection(B),"\n")

print("Difference(A-B) (M1):", A - B)  # Elements in A not in B
print("Difference(A-B) (M2):", A.difference(B),"\n")

print("Symmetric Difference(M1):", A ^ B)  # Elements in A or B but not both
print("Symmetric Difference(M2):", A.symmetric_difference(B),"\n")

# SET RELATIONS
C = {1, 2}
print("Is C subset of A?", C.issubset(A))
print("Is A superset of C?", A.issuperset(C))
print("Are A and B disjoint?", A.isdisjoint({7, 8}),"\n")

# IMMUTABLE SETS – frozenset()
fs = frozenset([1, 2, 3])
print("Frozen set:", fs,"\n")
# fs.add(4)  # ERROR – can't modify

# USE CASES
# Removing duplicates from list
my_list = [1, 2, 2, 3, 3, 4]
no_dup = list(set(my_list))
print("List without duplicates:", no_dup,"\n")

# Fast membership checking
if 5 in set(my_list):
    print("Is in the list (checked via set)")
else:
    print("Not in the list","\n")

# EXERCISES

#Q1. Create a set of even numbers from 1 to 20
Q1 = {x for x in range(1, 21) if x % 2 == 0}
print("Q1.", Q1)

#Q2. Given two sets, find only the elements unique to the first set
Q2 = {1, 2, 3, 4} - {3, 4, 5}
print("Q2.", Q2)

# Q3. Check if one set is a subset of another
Q3 = {1, 2}.issubset({1, 2, 3})
print("Q3.", Q3)

# Q4. Remove duplicates from the list: [5,5,6,7,8,8,9]
Q4 = list(set([5, 5, 6, 7, 8, 8, 9]))
print("Q4.", Q4)

# Q5. Create an immutable set of vowels
Q5 = frozenset("aeiou")
print("Q5.", Q5)

# Q6. Find Student having both subjects
students_math = {"Alice", "Bob", "Charlie"}
students_science = {"Bob", "David"}
print("Q6. Students in both:", students_math & students_science)