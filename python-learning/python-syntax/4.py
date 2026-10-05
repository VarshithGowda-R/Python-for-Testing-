
my_tuples = ("apple" , "mango", "banana" , 1,2,3,)
print(my_tuples)

# accessign the tuples
print(my_tuples[0])
print(my_tuples[-1])

# Slicing Tuples:
print(my_tuples[1:3])

# Tuple Operations
# Tuple Concatenation:

nums1_tuples = (2,4,5,6,6,7)
nums2_tuples = (4,5,6,6,5,8)
combined_nums = (nums1_tuples +nums2_tuples)
print(combined_nums)

# tuples Repetition

print(nums1_tuples *3)

#  Tuple Methods
print(5 in nums1_tuples)


#  Tuple Methods
#count methods
count_tuples = (1,5,7,85,7,9,49,4)
print(count_tuples.count(7))
#Index methods
print(count_tuples.index(49))

# Sets in Python

syntax = { "element1","element2"," element3" }
print(syntax)

#  Set Operations
# union
set1 = {5,8,3,4,9,12}
print(set1)
set2 = {7,8,9,4,5,6}
print(set1 | set2)

# Intersection: The intersection of two sets returns elements that are common to both sets.

print(set1 & set2)

# Difference: The difference between two sets returns elements that are in the first set but not in the second.
print(set1 - set2)

# Set Methods
set1.add(96)
set1.remove(96)
s = set1.pop()
print(s)
set1.clear()
print(type(set1))

# conversation form tuples to set 
tuples_conversation = (1,2,3,5,8)
tuplestoset = set(tuples_conversation)
print(type(tuplestoset))

# conversation form set to tuples 
set_converstion = (4,5,8,6,9,3)
tuple_holder = tuple(set_converstion)
print(type(tuple_holder))

# Dictionary

items = {
    "water":"its a basic needs",
    "bat":"which is used to hit the ball",
    "ball":"it is used to play cricket"
}
print(items)
print(items["water"])


place_items = {
    "bengaluru":"masala dosa",
    "mysore":"mysore part sweet",
    "mangaluru":"neer dose",
    "kalburgi":"roti"
}

#add 
place_items["tumkur"] = "cocont plants"
print(place_items)

# get
print(place_items.get("bengaluru"))

# update
place_items["mysore"] = "mysore park"
place_items["bengaluru"] ="ragi mudde"

# Delete
place_items.pop("tumkur")
print(place_items)


