#Data encapsulation:

#public variable

'''class student:
    name="ganesh"
    __age__=19     #private variable
    Age=__age__
    __city__="tuticorin"
    def add(name,age,city):
        print("name is",name)
        print("age is",age)
        print("city is",city)


print(student.Age)
obj=student;
print(obj.name)'''


'''student.add("raj",30,"world")
a=student
print(student.name)
print(student.age)
print(student.city)
print(a.name)'''

#a=student;
#print(student.add("raj",2,'world'))

'''class student:
    def __init__(self,n,a):
        name=n
        age=a
        print("Name=",name)
        print("Age=",age)
s1=student("n",'a')'''

'''class hello:
    def world(a,b):
        __num_1__=a
        __num_2__=b
        print(__num_1__+__num_2__)'''

    #def add():
       # print(__num_1__)


#a=hello
#print(hello.world(10,20))

'''class student:
    __name__="ganesh"
    __age__=30
    Name=__name__
    Age=__age__
    def display(a=__name__,b=__age__):
        print("name is",a)
        print("age is",b)
    def add(__name__,__age__):
        print(__name__)
        print(__age__)

#k=student
#print(k.display())

print(student.add("raj","1"))
print(student.__name__)'''


'''class student:
    name="ganesh"
    age=19
    def display():
        print("polymorphism")
class normal_student:
    def display(a="name",b="age"):
        print("name is",a)
        print("age is",b)

d=student
print(d.display())

k=normal_student
print(k.display("raj","2"))'''


'''class calculator:
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









































