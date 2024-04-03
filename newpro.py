for i in range(1,101):
    print(i)

for i in range(11,101):
    if(i%7)==0:
       print(i)

for i in range(75,20 -1):
    print(i)

n1=int(input("enter the first number"))
n2=int(input("enter the first number"))
n3=int(input("enter the first number"))

if(n1>n2):
    if(n1>n3):
        print("the largest number is",n1)
    else:
        print("the largest number is",n3) 
else:
    if(n2>n3):
        print("the largest nuumber is",n2)
    else:
         print("the largest number is",n3)  

m1=int(input("ENTER THE PERCENTAGE OF STUDENT IS:"))

if(m1>=85):
    print("grade A")
elif((m1<85) and (m1>=75)):
    print("grade -b")
elif((m1<75) and (m1>=65)):
    print("grade -c")
elif((m1<65) and (m1>=55)):
    print("grade -d")
elif((m1<55) and (m1>=40)):
    print("grade -e")
else:
    if(m1<=40):
       print("grade -f")

