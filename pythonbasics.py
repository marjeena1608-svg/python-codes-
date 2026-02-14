#basic
print("YASMIN ALI")
#check the datatype
a=10
print(type(a))
#in case of sum datatype
a="10"
b=8
print(type(a))
print(type(b))
#through giving choice python
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
ch=(input("enter your choice:+,-,/,*"))
c=a+b
d=a-b
e=a*b
f=a/b
if(ch=="+"):
    print("the add is c",a+b)
elif(ch=="-"):
    print("the sub is:",a-b)
elif(ch=="*"):
    print("the multiply is:",a*b)
elif(ch=="/"):
    print("the divide is:",a/b)
else:
    print("incorrect choice")
#implicit type conversion
a=2
b=2.5
c=a+b
print(type(c))
#explicit type conversion
m="2.0"
print(type(m))
o=2
print(type(o))
#expression evaluation in python
#numeric evaluation
u=int(input("enter the value of u:"))
v=int(input("enter the value of v:"))
print(u+(u+v*u))
#string expression
first=(input("enter your first name:"))
last=(input("enter your last name:"))
full_name=first+last
print(full_name)
#bool expression
y=3
x=9
print(x>y)
#function call expression
def add(x,y):
    z=x+y
    print(z)
    add(8,9)
#complex expression
k=int(input("enter the value of k:"))
l=int(input("enter the value of l:"))
print(x+y+(x*2+(x*5-(3*y)+x)))



