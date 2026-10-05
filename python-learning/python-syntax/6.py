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
    print("no more cities ")


    
