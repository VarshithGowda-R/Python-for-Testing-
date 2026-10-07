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

