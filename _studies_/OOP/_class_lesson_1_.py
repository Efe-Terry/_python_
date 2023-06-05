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

#simple OOP with class..