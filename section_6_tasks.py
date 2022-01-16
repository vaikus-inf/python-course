# Задание № 1
from distutils.command.build_scripts import first_line_re


class Name:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = self.first_name + ' ' + self.last_name
        self.initials = self.first_name[0] + '.' + self.last_name[0]

a1 = Name('john', 'SMITH')
print(a1.first_name)
print(a1.last_name)
print(a1.full_name)
print(a1.initials)

# Задание № 2
class Calculator:
    
    def add(self, n1, n2):
        return n1 + n2
        
    def subtract(self, n1, n2):
        return n1 - n2
    
    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        return n1 / n2

calculator = Calculator()
print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))

# Задание № 3
class Employee:
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    @classmethod
    def from_string(cls, s):
        # parsing = s.split('-')
        # return cls(parsing[0], parsing[1], int(parsing[2]))

        # Или такой вариант:
        first_name, last_name, salary = s.split('-')
        return cls(first_name, last_name, int(salary))

emp1 = Employee('Mary', 'Sue', 60000)
print(emp1.first_name)
print(emp1.salary)

emp2 = Employee.from_string('John-Smith-55000')
print(emp2.first_name)
print(emp2.salary)

# Задание № 4
class Pizza:
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order
    
    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])

    @classmethod        
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])
    
    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

p1 = Pizza(['bacon', 'parmesan', 'ham'])
p2 = Pizza.garden_feast()
print(p1.ingredients)
print(p2.ingredients)
print(p1.order_number)
print(p2.order_number)