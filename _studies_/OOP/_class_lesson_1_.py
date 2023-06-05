print("\nEmployee Class: \n")

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #email
        self.email = "Email: " + first + '.' + last + '@company.com'
        #name_on_badge
        self.badge = "Name_On_Badge: " + first
        
    def fullname(self):
        #NOTE: return
        return 'Full Name: {} {}'.format(self.first, self.last)

emp1 = Employee("Andrew", "Snow", 15000)

print(emp1.fullname())
print(emp1.badge)
print(emp1.email)

print("\nCar Class: \n")

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started!")

    def drive(self, distance):
        print(f"The {self.brand} {self.model} has driven {distance} miles.")

car1 = Car("Honda", "Acord", 2024)
car1.start_engine()
car1.drive(1000)