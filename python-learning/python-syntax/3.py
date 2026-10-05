#input output, string maunipalation , comments 

Boy_name = input(" Boy Name : ")
Boy_age = int(input("Boy age: "))
Girl_name = input(" Girl Name:  ")
Girl_age = int(input("Girl age : "))

#Absalute concept using by just abs
age_difference = abs(Boy_age-Girl_age)

# string concatination
print(Boy_name +" loves "+Girl_name)
print(f"{Boy_name} is {Boy_age} loves {Girl_name} at {Girl_age} age difference between them is {age_difference}")


# Repitation
greeting ="ERROR  "*3
print(greeting)

# String methods 
Desk = "  Python is awesome!  "
print(Desk.upper())
print(Desk.lower())
print(Desk.replace("awesome", "easy laguage to learn"))
print(Desk.strip())
print(Desk.count("Python"))

# String Indexing 
text = "python"
print(text[2]) #t
print(text[5]) #n
print(text[-3]) #H


name = input(" please entire the name: ")
print(f"{name.__len__()}")

S = "laundrymate.in is laundry service company in bengaluru \n which will help the everyday laundry problems for each\thouseholds \\"
print(S)

''' List Manipulation Exercise:

Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation. '''

items = ["keybord","mouse","monitor","mobile","headset"]
items.append("waterbottal")
items.insert(1,"pen")
items.remove("monitor")
print(items[:2])
# print(items)
print(items.__len__())
print(sum(items))


''' Reverse and Sort a List: Create a list of numbers and:
Sort it in descending order.
Reverse the sorted list and print it.'''

nums = [1,6,8,4,23,55,85,7]
nums.sort()
print(nums)

# Reverse the sorted list and print it.
nums.sort(reverse=True)
print(nums)
