def add(a,b):
    print(a+b)
def sub(a,b):
    print(num_1-num_2)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

num_1=int(input("enter the value:"))
num_2=int(input("enter the value:"))
num_3=input("enter the operator:")
if num_3=="+":
    add(num_1,num_2)
elif num_3=="-":
    sub(num_1,num_2)
elif num_3=="*":
    mul(num_1,num_2)
elif num_3=="/":
    div(num_1,num_2)
else:
    print("enter the correct value")
