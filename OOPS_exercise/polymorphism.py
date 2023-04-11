
#function overloading


class student:
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
print(k.display("raj","2"))



#function overriding

'''class a():
    def add(self):
        print("hello")
class b(a):
    def add(self):
        print("hello world")



obj_1=b()
print(obj_1.add())'''