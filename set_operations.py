'''my_set={10,20.5,"hello","world",10,(100,100.5)}
my_set.add(30)
print(my_set)
my_set.update([50,60])
print(my_set)'''


#my_set=set([1,2,3]),set((4,5,6))
#print(my_set)

'''my_set={10,20.5,"hello",100,10,"hello"}
print(my_set)
my_set.add(20)
print(my_set)
my_set.discard(100)
print(my_set)
my_set.clear()
print(my_set)'''

'''a_1={10,20,30,40}
b_1={20,40,50,60}
print(a_1.union(b_1))
print(b_1.union(a_1))
print(a_1|b_1)'''

'''a_1={10,20,30,40}
b_1={20,40,50,60}
print(a_1.intersection(b_1))
print(a_1&b_1)'''

'''a={10,20,30,40}
b={20,40,50,60}
print(a-b)
print(b-a)
print(a.difference(b))
print(b.difference(a))'''

'''a={10,20,30,40}
b={20,40,50,60}
print(a^b)
print(a.symmetric_difference(b))
a.difference_update(b)
print(a)'''

'''a_1={10,20,30}
a_2={10,20}
b_1=frozenset([10,20,30])
b_2=frozenset([10,20])
print(b_1.issubset(a_1))
print(a_1.issubset(a_2))'''

'''a_1={10,20,30}
a_2={10,20}
b_1=frozenset([10,20,30])
b_2=frozenset([10,20])
print(a_2.issuperset(b_2))
print(a_2.issuperset(b_1))'''

#a=frozenset([10,20,30])
#print(a)

'''a=(10,20,"hello")
b=frozenset(a)
print(b)'''

#union operator

'''a={10,20,30,40}
b={20,40,50,60}
print(a|b)
print(b|a)'''

#intersection operator

'''a={10,20,30,40}
b={20,40,50,60}
print(a&b)
print(b&a)'''

#difference operator

'''a={10,20,30,40}
b={20,40,50,60}
print(a-b)
print(b-a)'''

#symmetric difference operator

'''a={10,20,30,40}
b={20,40,50,60}
print(a^b)
print(b^a)'''

#discard()

'''set_1={10,20,30,40}
set_2={30,40,50,60}
set_1.discard(30)
print(set_1)
set_1.discard(50)
print(set_1)'''

#remove()

'''set_1={10,20,30,40}
set_1.remove(20)
print(set_1)
set_1.remove(50)
print(set_1)'''

#pop()

'''set_1={10,20,30,40}
set_1.pop()
print(set_1)
set_1.pop(20)
print(set_1)'''

#global variable

'''a="global"
def demo():
    print("variable:",a)

demo()
print(a)'''

#local variable

'''def demo():
    a="local"
    print(a)

demo()
print(a)'''

'''var=int(input("enter the number:"))
def demo():
    print("number:",var)

demo()'''






























