'''class student:
    num1="10"
    name="hello"
    __age__="30"
    def display(num1,__age__):
        print("number=",num1)
        print("age=:",__age__)

class a:
    def add(a,b):
        print(a+b)

k.display()
student.display("1","2")
a.add(2,2)
print(student(num1))'''

'''class a:
    num_1=10
    __num2__=20
print(a.__num2__)
class b:
    num3=30


print(a.num_1)
print(b.num3)
print(a.__num2__)'''

class a():
    def add(self):
        print("hello")
class b(a):
    def add(self):
        print("hello world")



obj_1=b()
print(obj_1.add())
