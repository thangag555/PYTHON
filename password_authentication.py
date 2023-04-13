'''
password=input("enter your password:")

i=1
while password!="hello" and i<5:
    print("invalid code")
    i=i+1
    password=input("enter your password:")
    if password=="hello":
        print("good to have")
    elif i==5:
        print("access denied")

if password=="hello":
    print("good to have")

'''

'''password=input("enter your password:")
if password=="hello":
    print("welcome")
    print("access granted")
else:
    i=1
    while password!="hello" and i<5:
        print("invalid password")
        i=i+1
        password=input("enter your password:")
        if password=="hello":
            print("welcome")
            print("access granted")
        elif i==5:
            print("access denied")'''
# print("access granted")























