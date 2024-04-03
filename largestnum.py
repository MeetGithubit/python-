a=input("enter first number")
b=input("enter a second number")
c=input("enter third number")


a1=int(a)
b2=int(b)
c3=int(c)

if(a1>b2):                                 
     if(a1>c3):
       print("the largest value is",a1)
     else:
       print("the largest value is",c3)
else:
     if(b2>c3):
       print("the largest number is",b2)
     else:
       print("the largest value is",c3)
