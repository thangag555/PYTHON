#single_inheritance


class calculator:
    a,b=10,20
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
class calculator_1(calculator):
    def mul(self,a,b):
        return a*b

c_1_obj=calculator_1()
print(c_1_obj.add(50,100))
print(c_1_obj.mul(10,10))'''


#multiple inheritance

'''class simple_calculator():
    a,b=10,20
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
class advanced_calculator():
    def mul(self,a,b):
        return a*b
class scientific_calculator(simple_calculator,advanced_calculator):
    def div(self,a,b):
        return a/b

sc_obj=scientific_calculator()
print(sc_obj.add(10,50))
print(sc_obj.mul(10,10))
print(sc_obj.div(50,50))'''

#multilevel inheritance

'''class basic_calculator():
    a,b=10,20
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
class advanced_calculator(basic_calculator):
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

class scientific_calculator(advanced_calculator):
    def sqrt(self,a,b):
        return a**b

sc_obj=scientific_calculator()
print(sc_obj.add(10,10))
print(sc_obj.mul(10,10))
print(sc_obj.sqrt(5,5))'''


'''class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is",self.name)
        print("age is",self.age)

b=student("ganesh",19)
b.display()'''

