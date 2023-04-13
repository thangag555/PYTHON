#functions

'''print("hello")
"""it prints the string inside the function
it prints the string inside the function
it prints the string inside the function
it prints the string inside the function
it prints the string inside the function
it prints the string inside the function
it prints the string inside the function
it prints the string inside the function
it prints the string inside the function"""
#it, prints, the, string, inside, The, function=10,20,30,40,50,60,70
#print(it,prints)'''

#function with arguments

'''def add(a,b):

    return a+b

print(add(3,3))'''


'''def add(a,b):
    return a+b
print(add(5,5))'''

#function without arguments


'''def mul():
    return "hello world"
print(mul())'''



'''def display():
    print("python is a programming language ")

display()'''

#function with default arguments

""""def add(a,b,c=10):
    print(a+b+c)
add(5,15)

def add(a,b=1,c=10):
    print(a+b+c)

add(20,30,1)"""

#lambda function (unknown function):


'''a=lambda x,y,z:x+y+z
print(a(10,20,30))'''

#function with keyword arguments

'''def demo(**kwargs):
    print("hello",kwargs["name"])
    print("welcome to",kwargs["year"])
    print("thanks you",kwargs["name"])
    
my_list=["ganesh","suresh",]
for i in range(len(my_list)):
    demo(name=my_list[i],year=2022)'''

#function with arbitrary arguments

'''def demo(*args):
    print("hello",args[1])
    print("welcome to",args[0])
demo("world",2022)
demo(2022,"world")'''

'''def demo(*args):
    print("hello",args[2] + str("\twelcome to python"))

my_list=["ganesh","suresh","ramesh"]
demo(my_list[0],my_list[1],"mohan")'''

#format function

'''var_1="hello world"
print("{} is the first program".format(var_1))
print("{} is the first program".format("hello world"))'''


'''var1="hello world"
var2="python"
print("{} is the first program in {}".format(var1,var2))
print("{} is the first program in {}".format("hello world","python"))'''

'''var1="hello world"
var2="python"
print("{1} is the first program in {0}".format(var1,var2))
print(f"{var1} is the program in {var2}")     #f string
print("{var1} is the program in {var2}".format(var1="dance",var2="culturals"))'''

#recursion using normal function

def find_fact(x):
    result=1
    while x>=1:
        result=result*x
        x=x-1
    return result

#recursive function

'''def recursive_function(x):

    if x == 1:
        return x
    else:
        return x*recursive_function(x-1)

    #return x if x==1 else(x*recursive_function(x-1))
'''
print(find_fact(5))
#print(recursive_function(5))

























































































































































































