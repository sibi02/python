class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        pass
    def birthday(self):
        print("The Age is "+ str(self.age))
        self.age+=1
        print("The Age is "+str(self.age))
    def __str__(self) -> str:
        return self.name + " " + str(self.age)
        pass

class Employee(Person):
    def __init__(self, name, age,empid) -> None:
        super().__init__(name, age)
        self.empid=empid
    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age>=21:
            rate_of_pay+=2.50
        return hours_worked*rate_of_pay
    def __str__(self) -> str:
        return self.name + " " + str(self.age) +" "+ str(self.empid)
        pass

Super_Class = Person("Sibi",24)
print(Super_Class)

Parent_class = Employee("Sibi",24,1000.00)
print(Parent_class)
