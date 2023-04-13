Age = int(input("enter your age:"))
if Age > 0 and Age < 12:
    #print("Child")
    if Age==1 or Age==7:
        print("Notable Age")
    elif Age==5 or Age==8:
        print("it's also a notable age")
    else:
        print("Child")
else:
    print("adult")

#eligible to vote or not


'''var_1=int(input("enter the number:"))
if var_1>=18:
    print("you can vote")
    print("thank you")
elif var_1<18:
    print("you are not eligible")
else:
    print("enter the correct value")'''
