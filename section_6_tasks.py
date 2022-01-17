# Задача № 1
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

# Задача № 2
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

# Задача № 3
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

# Задача № 4
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

# Задача № 5
import math

class Circle:
    
    def __init__(self, radius = 0):
        self.radius = radius    
    
    def get_area(self):
        return math.pi * math.pow(self.radius, 2)
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(10)
area = circle.get_area()
perimeter = circle.get_perimeter()
print(area)
print(perimeter)

# Задача № 6
prices = {'Strawberries' : 1.5, 'Banana' : 0.5, 'Mango' : 2.5,
		'Blueberries' : 1, 'Raspberries' : 1, 'Apple' : 1.75,
		'Pineapple' : 3.5}

class Beverage:

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.prices = prices

    def get_cost(self):
        return '$' + str(format(sum(self.prices[v] for v in self.ingredients), '.2f'))
    
    def get_price(self):
        return '$' + str(format(float(self.get_cost()[1:]) * 2.5, '.2f'))
    
    def get_name(self):
        sorted_ingredients = sorted([v.replace('berries', 'berry') for v in self.ingredients])
        sorted_ingredients.append('Fusion') if len(sorted_ingredients) > 1 else sorted_ingredients.append('Smoothie')
        return ' '.join(sorted_ingredients)

s1 = Beverage(['Mango', 'Banana', 'Strawberries'])
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())

# Задача № 6 (решение из курса)
prices = {'Strawberries' : 1.5, 'Banana' : 0.5, 'Mango' : 2.5,
		'Blueberries' : 1, 'Raspberries' : 1, 'Apple' : 1.75,
		'Pineapple' : 3.5}

class Beverage:

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        return f'${self.cost:.2f}'
    
    def get_price(self):
        return f'${self.price:.2f}'
    
    def get_name(self):
        lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
        return f'{" ".join(lst)} {"Fusion" if len(lst) > 1 else "Smoothie"}'
	
s1 = Beverage(['Mango', 'Banana', 'Strawberries'])
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())