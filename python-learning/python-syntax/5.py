# if  eles elif condition

time = 14

if time == 14:
    print("Login time")
elif time == 17:
    print("Its snacks time")
else:
    print("its time to logout")

# vote eligible
age = 6

is_nation_India = True

if age >=18 and is_nation_India:
    print("You are eligible for voteing ")
else:
    print('You are not eligible for voteing')


day = str(input("pleas enter the weekdays name"))
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("It's a weekend, let's visite Mysuru!")
    else:
        print("It's rainning ,Lets stay home")
else:
    print("It's a weekday, let's wait for the weekend")

#  Match case  age 
age = int(input("please Enter the age!  "))
ticket_price = 80

match age:
    case age if age<= 5:
        print("Below 5Years ticket are free")
    case age if age <=12:
        print("half ticket price of childerns")
    case age if age >=60:
        print("Half ticket price for senior persons")
    case _:
        print("pay the full ticket fair")


# Meal Time Checker:

daily_routen = int(input("Please enter the time!  "))
task = bool(input("Do you have any pending task!  "))

if daily_routen == 6:
    print("Time to login for work")
    if task == "yes" :
        print("please complete the pending task! ")
elif daily_routen == 8:
    print("Time to have the breakfase 8AM")
elif daily_routen == 1:
    print("Time to have Lunch break! 1PM")
elif daily_routen == 9:
    print("Time to have the Dinner 9Pm")
else :
    print("It's not a meal time")
     

    