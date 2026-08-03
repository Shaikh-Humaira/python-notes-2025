# File I/O

# python can be used to perform operations on a file (read & write data)

# syntax 1
# f = open("file_name.ext","mode")
#data = f.read() #reads the entire file
#we can also speciefy the no of char to read in the brackets. eg: f.read(3) will read only 3 char from the file.
# line = f.readline() #reads only one line from the file. If we call this function again, it will read the next line.but if we call it after reading the file once,
# it will return an empty string as the pointer is at the end of the file. We can use f.seek(0) to reset the pointer to the beginning of the file.
#f.close() #closes the file so someone else can not access it. It is a good practice to close the file after reading or writing.

# syntax 2
#with open("file_name.ext","mode") as f:
#   data = f.read() #reads the entire file
#   f.write("hello") #writes the data to the file.
#   print(data) no need to close the file as it will be closed automatically after the with block is executed.

# 'r' : open for reading (default)
# 'w' : open for writing, truncating(empting) the file first
# 'x' : create a new file and open it for writing
# 'a' : open for writing, appending to the end of the file if it exists, creates a new file if it does not exist. # funny thing is it will append same line again and again if we run the code multiple times. 
# 'b' : binary mode (e.g. images. these files need to be mentioned in binary mode to open them, also we can use 'rb' or 'wb' for reading and writing in binary mode and these are not human readable)
# 't' : text mode (default)(even if we don't write it, file will be opened in text mode)
# '+' : open a disk file for updating (reading and writing)
# 'r+': read + overwrite  (pointer starting) #no truncate
# 'w+': write + overwrite (pointer ending) #truncate
# 'a+': read + append (pointer ending) # no truncate

# Types of all files
# 1.Text Files : .txt, .docx, .log etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc.

f = open("practice.txt","r")
data = f.read() 
print("Reading Data:", data)
# print("Reading line:",line)
print(type(data),"\n")
f.close() 

f = open("practice.txt","a") #append mode 
f.write("\n I also like programming in C++.") 

#DELETING A FILE
#import os # is used to perform operations on files and directories. It is a built-in module in python.
#os.remove("practice.txt") # deletes the file from the directory.

#Excersize
#Q1. Create a new file “practice.txt” using python. Add the following data
with open ("practice.txt","r") as f:
    # print(f.write("Q1. Hi everyone \n we are learning File I/O \n using Java. \n I like programming in Java.\n"))
    data = f.read()
 
#Q1.1 replace all occurrences of “java” with “python” in above file
new_data = data.replace("Java","Python")
print("Q1.1 new data:",new_data)

f = open("Practice.txt","w")
Data = f.write(new_data) 
    
    
 #1.2 Search if the word “learning” exists in the file or not  
if(data.find("learning") != -1):
     print("Q1.2 Learning word found")
else:
    print("Learning word not found")

#Q1.3 WAF to find in which line of the file does the word “learning”occur first. 
# Print -1 if word not found
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("Q1.3 Line number:", line_no)
                return
            line_no += 1
    return -1
print("Q1.3 Line number:", check_for_line())

#Q2. From a file containing numbers separated by comma, print the count of even numbers
with open("practice.txt","r") as f:
    data = f.read()
num = ""
for i in range(len(data)):
    if(data[i] == ","):
        print("Q2. ", num)
        num = ""
    else:
        num += data[i]
#method 2
nums = data.split(",")
print("Q2. ", nums)

#Q3. even numbers from a file containing numbers separated by comma, print the count of even numbers
# count = 0
# with open("practice.txt","r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):  #will give error if we use this function in file containing non-numeric values. So we can use try-except block to handle this error.
#             print("Q3. Even number:", val)
#             count += 1
# print("Q3. Count of even numbers:", count)