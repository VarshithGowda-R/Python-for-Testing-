class Car :
    # attribute / constructure 
    def __init__(self,brand,model,year):
        self.brand = brand #instance variable 
        self.model = model #instance variable 
        self.year = year # insstance variable 

    # method
    def car_details(self):
         print(f"car brand : {self.brand} and {self.model} maunifatured in the year of {self.year}")

    # creating the car details object
my_car = Car("Toyota", "supra", "2009")
my_car.car_details()

class Bike :
    # attribute / constructure 
    def __init__(self,brand,model,year):
        self.brand = brand #instance variable 
        self.model = model #instance variable 
        self.year = year # insstance variable 

    # method
    def bike_details(self):
         print(f"bike brand : {self.brand} and {self.model} maunifatured in the year of {self.year}")

    # creating the bike details object
my_bike = Bike("Yamaha", "R1", "2020")
my_bike.bike_details()

class Truck :
    # attribute / constructure 
    def __init__(self,brand,model,year):
        self.brand = brand #instance variable 
        self.model = model #instance variable 
        self.year = year # insstance variable 

    # method
    def truck_details(self):
         print(f"truck brand : {self.brand} and {self.model} maunifatured in the year of {self.year}")

    # creating the truck details object
my_truck = Truck("Ford", "F-150", "2018")
my_truck.truck_details()


class Student_information :
    # attribute / constructure 
    def __init__(self,name,roll_no,age,course):
        self.name = name #instance variable
        self.roll_no = roll_no #instance variable
        self.age = age #instance variable
        self.course = course #instance variable

    # method
    def student_details(self):
         print(f"Student name : {self.name} and roll number is {self.roll_no} and age is {self.age} and course is {self.course}")

    # creating the student details object
my_student1 = Student_information("jaki", "12345", "20", "Computer Science")
my_student2 = Student_information("john", "67890", "22", "Mechanical Engineering")
my_student3 = Student_information("emma", "54321", "19", "Electrical Engineering")
my_student4 = Student_information("oliver", "98765", "21", "Civil Engineering")

my_student1.student_details()
my_student2.student_details()
my_student3.student_details()
my_student4.student_details()

# method call using class name
Student_information.student_details(my_student1)