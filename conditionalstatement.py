#odd even
a=int(input("enter the value of a:"))
if(a%2==0):
    print("even")
else:
    print("odd")
#nested if=greatest of three
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=int(input("enter the value of z:"))
if(x>y):
    if(x>z):
        print("gretest no. is:",x)
    else:
        print("greatest no. is:",z)
else:
    if(y>z):
        print("greatest no. is:",y)
    else:
        print("gretest no. is :",z)

