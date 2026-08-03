#13_module
#  IF __NAME__== ‘__MAIN__’ IN PYTHON  
# ‘__name__’ evaluates to the name of the module in python from where the program is 
# ran. 
# If the module is being run directly from the command line, the ‘ __name__’ is set to 
# string “__main__”. Thus, this behaviour is used to check whether the module is run directly or imported to another file. 

def  myFunc():
    print("Hello World")

myFunc()
print("File",__name__)

if __name__ == "__main__": #the code inside this function block will not be imported to any other file. it will be runned in this file only add the output will be shown here only
    #if this code is directly excecuted by runnying the file its present in 
    print("We are directly running this code")
    print("hiiii")