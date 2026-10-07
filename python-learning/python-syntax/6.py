# loops in python
is_student_failed =  True
attemp = 1
while is_student_failed :
    if attemp%2 !=0:
        attemp = attemp + 1
        continue
    print(f"student attempted {attemp}")
    attemp = attemp + 1
    if attemp >100:
        break

print("Give up")

i = 1
while i <= 10:
    print(f"interation value {i}")
    i += 1

# Create a program that prints all odd numbers between 1 and 20 using a while loop.

i = 1
while i<=20:
    if i%2 != 0:
        print(f"value of i { i } odd number ")
    i += 1

 # Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.

i = 10
while i > 0 :
    print(f"countdown start {i}")
    i -= 1
print("happy new year")

# Let’s stop counting sheep after 5 sheep, even though the condition allows counting up to 10:

sheep_count = 1
while sheep_count<= 10:
    print(f"sheep {sheep_count}")
    if sheep_count == 5:
        print("That's enough couting")
        break
    sheep_count += 1

# Let’s say you want to skip counting sheep that are number 4:

sheep_input = 1
while sheep_input <= 10:
    if sheep_input == 4:
        sheep_input += 1
        continue
    print(f"sheep { sheep_input }")
    sheep_input+= 1

    # You can use a while loop to repeatedly ask the user for input until they provide valid data.

#nested for while loop 

trail = 0
amount = 10000

while trail >=0:
  atm_pin = int(input("Please enter the pincode!  "))

  if atm_pin == 1010:
    customer_request = int(input("Please enter the cash to be collected! "))

    if customer_request >= amount:
        print(f"account balance {amount} insufficent amount")
    elif customer_request <= amount :
        print(f"please collect the cash")
        break
  else :
    trail += 1
    print ("please enter the pin code correctly ")


# for loop
cities = ["bengaluru" ,"mangaluru","mysuru","hubballi"]
for karnataka in cities:
    print(karnataka)

# range with for loop
for i in range(1,11):
    print(i, end=" ")

# Counting by 2s from 1 to 10
for i in range(1,11,3):
    print(i, end=" ")

# Looping Over Strings
name = "varshith R"
for letters in name:
    print(letters)

# Looping Through a List with enumerate()
state = "karnataka"
for index,letters in enumerate(state):
    print(f"letter {index}: {letters* (index+1)}")

# Using else with for Loops
city = ["bengaluru","mumbhai","kolkatha","gurgarm","channi"]
for toptire_city in city:
    print(toptire_city, end= "  ")
else:
    print("\n no more cities ")

''' Real-Life Example: Distributing Laddus
Imagine you have 5 laddus to distribute among friends. You can use a for loop to give each friend one laddu.'''

laddu = 5
menbers = ["raju","ramu","raki","navya","bhavya","divya","keerthi","supriya"]
for distribution in menbers:
    if laddu >0:
        print(f"{distribution} gets a laddu")
        laddu -= 1
    else:
        print(f"{distribution}  no laddu left")


# Multiplication of 3 to 30 using for loop
for i in range(3,31):
    for j in range(1 ,11):
        print(f"{i} X { j} = {i*j}")

#count the number vowels in a string and print the letters
user = str(input("Please enter the string!  ")).lower()
vowels = "aeiou"
vowels_count = 0
vowels_found = []
for letters in user:
     if letters in vowels:
       vowels_found.append(letters)
       vowels_count += 1


print(f"total number of vowels  {vowels_count} and { vowels_found}")

x = 0
while x < 100:
    x += 2
print(x)

# Sum of the given list

sum = [1,5,8,3,8]
total = 0
for i in sum:
     total += i
     
print(total)

# double the given list vaule in the list 

list_num = [25,35,3,6,78,52]
double = []

for variable in list_num: 
    double.append(variable*2)

print(double)


# looping the dictonary

demo = {"name":"varshith","age":25,"city":"bengaluru","area":"HSR_layout"}
for variable in demo.items() :
    print(variable)


demo = {"name":"varshith","age":25,"city":"bengaluru","area":"HSR_layout"}
for variable in demo.keys() :
    print(variable)

    
demo = {"name":"varshith","age":25,"city":"bengaluru","area":"HSR_layout"}
for variable,biodata in demo.items() :
    print(f"{variable}-----{biodata}")

demo = {"name":"varshith","age":25,"city":"bengaluru","area":"HSR_layout"}
for variable in demo.values() :
    print(variable)


# Adding marks to students using index values

students = ["chandan","varshith","darshan","harshi"]
marks = [95,69,32,75]

students_marks = {}
for i in range(len(students)):
    students_marks[students[i]] =marks[i]

print(students_marks)

# List Comprehension
nums = [ x for x in range(0,100)]
dnumbs = [ i  *2  for i in nums]
print(dnumbs)

#  Creating a dictionary of squares

num = [x for x in range(0,11)]
squares = [ i * i for i in num]
print(squares)

#  Converting a list of names to a dictionary of name lengths

students = ["chandan","varshith","darshan","harshi"]
name_len = {student:len(students) for student in students}
print(name_len)

names = ["Anand", "Geetha", "Kumar"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)


# Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

nation_state  = ["karnataka","west bengal","delhi","tamilnadu"]
Upper_case_city = [states.upper() for states in nation_state]
print(Upper_case_city)

city = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
upper_case = [state.upper() for state in city]
print(upper_case)

# Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.

dtry = {"laptop":26000,"mobile":500000,"cpu":15000,"tv":120000}
total_value = 0
for var in dtry.values():
    total_value += var
    
print(total_value)

# Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.

squares = [ x for x in range(0,11)]
dl = [x ** 2 for x in squares]
print(dl)

# Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.

d = {"bengaluru":10000000,"magaluru":200000,"kolara":200000,"chikkaballapura":40000}
large_city = {city:city_population for city,city_population in d.items() if city_population > 1000000}
print(large_city)

age = {"varshith":24,"chethan":32,"bharath":31,"piyali":28}
older_person = { person: age for person, age in age.items() if age>21} 
print(older_person)

# Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

# Prints the entire matrix row by row.
# Prints the sum of each row in the matrix.

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
for i in range(rows):
    # Take space-separated integers for each row
    row = [int(num) for num in input(f"Enter {cols} values for row {i + 1} separated by space: ").split()]
    matrix.append(row)


print("Your Matrix:")
for row in matrix:
    print(row)