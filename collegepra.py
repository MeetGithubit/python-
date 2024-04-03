#use while loop
#i=1
#while i<=50:
     #print(i)
     #i=i+1;

#use for loop
i=1
j=50
for i in range(1,51):
    print(i)

#for loop use
for i in range(11,101):
    if(i%7==0):     
       print(i)

for i in range(75,20,-1):
    print(i)

a1=int(input("enter first number"))
b2=int(input("enter a second number"))
c3=int(input("enter third number"))


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
