

# python support oop --> encapsulation --> hide data , limit accessibility

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#         self.net_salary = salary*.8



# add property -> display netsalary

# emp= Employee('Jack', 5000)
# print(emp.net_salary)
# emp.net_salary = 10000


# configure calculated fields ??

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#
#     def net_salary(self):
#         return self.__salary*.8  # return value represent object
#
# emp = Employee('<NAME>', 5000)
# print(emp.net_salary())




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def net_salary(self):
        return self.__salary*.8  # return value represent object

emp = Employee('<NAME>', 5000)
print(emp.net_salary)
emp.net_salary=43534634


