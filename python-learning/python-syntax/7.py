# function in python 

# You define a function using the def keyword followed by the function name, parentheses, and a colon :.

def greeting () :
    print("hello very good morning ! ")
greeting()

# function with parameter 

def details(name,age,location):
     print(f"hello  {name}! you age is {age} you are staying in the {location}")
     details("varshith",45,"HSR layout bengaluru karnataka")

# function with parameter by using the user input 
def details (name,age,location):
    print(f"hello {name} your age is {age} staying in {location}")
details(input("please enter the name "),input("please enter the age "),input ("please enter the location "))

# Returning Values from a Function by using the return key word 

def add_to_value (x1,x2):
    return x1+x2 
result = add_to_value(10,20)
print(result)

# global varibale 
value = 30

def multi():
   value  = 32   #local variable 
   print(f"local_value { value }")
multi()   

print(value)

# Variable-Length Arguments

def add (*numbers):
    print(type(numbers))

add(10,30,10,80,20)


def total_sum(*nums):
    result = 0 
    for total in nums:
        result +=total
    return result
add = total_sum(2,8,7,12,30) 

print(add)

# Using **kwargs

def details(**student_infor):
    for name,age in student_infor.items():
        print(f"student name {name} age is {age}")
print(details(varhith=25,keerthi=21,harshith=31))
