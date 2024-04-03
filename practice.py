# for i in range(1,101):
#     print(i)

# for i in range (24,76):
#     if (i%8)==0:
#         print(i)
# for i in range(75,20,-1):
#     print(i)

# m1=int(input("Enter a first number:"))
# m2=int(input("Enter a second number:"))
# #m3=int(input("Enter a third number:"))

# if (m1>m2):
#     print("the largest number is:",m1)
# else:
#     print("the largest number is:",m2)
# else:
#     if(m2<m3):
#         print("the largest number is:",m2)
#     else:
#         print("the largest number is:",m3)4

# n1=int(input("Enter student percentage:"))


# if(n1>=85):
#     print("YOU HAVE PASSED EXAM GRADE-A")
# elif(n1<85) and (n1>=85):

# w1=int(input("enter any number:"))

# if(w1%2==0):
#     print("the nuumber is even number:")
# else:
     
#      print("the nuumber is odd number:")

# h1=int(input("enter first number:"))
# h2=int(input("enter second number:"))
# h3=int(input("enter third number:"))
# h4=int(input("enter four number:"))
# h5=int(input("enter five number:"))
# h6=int(input("enter six number:"))
# h7=int(input("enter seven number"))

# sum=h1+h2+h3+h4+h5+h6+h7

# print("above all sevan number sum is:",sum)

# sum=1
# for i in range(21,31):
#      print(i)
#      sum*=i
# print("the multiply of all number is:",sum)

# num= int(input("enter a number:"))
# if num==1:
#      print("the number is not prime number")
# if num>1:
#      for i in range(2,num):
#           if num%i==0:
#            print(num,"is not a prime number")
#            break
#      else:
#          print(num,"is a prime number") 

# num=int(input("enter any number:"))


# sum=0
# for i in range(1,num):
#     if(num%i==0):
#        sum=sum+i

# if(num==sum):
#     print("the numbe is perfect number")
# else:
#     print('not')

# var=int(input("enter any number:"))

# t=(var)
# sum=0
# while (var>0):
#     r=var%10
#     sum=(sum*10)+r
#     var=var//10

# if(t==sum):
#     print("the num is palindrone")
# else:
#     print("not")

# i=1

# while(i<=5):
#     print(i * " *")
#     i=i+1

# i=5
# while(i>=0):
#     print(i* " *")
#     i=i-1
    
# var1=int(input("enter the  number 1 is:"))
# var2=int(input("enter the  number 2 is:"))
# var3=int(input("enter the  minus value is:"))

# import math
# print("\nabsolute",abs(var3))
# print("\nceil",math.ceil(var1/var2))
# print("\nfloor",math.floor(var1/var2))
# print("\nmax",max(var1,var2))
# print("\nsqrt",math.sqrt(var2))
# print("\nround",round(var1/var2)+1)
# print("\npower",pow(23,3))

# import random

# count=0
# for i in range(15,45,4):
#     if(count!=10):
#        print(random.randrange(15,45,4))
#     count= count+1

# input_string=input("Enter a string is:")

# if(input_string.isalpha()):
#     print("the string is alphabetic")
# elif(input_string.isnumeric()):
#     print("numetic")
# elif(input_string.isalnum()):
#     print("alnum")
# elif(input_string.isspace()):
#     print("space")
# else:
#     print("invalid")

# var=input("Enter the string")

# print("\ncapiatalize of",var.capitalize())
# print("\ncener",var.center(50))
# print("\nlower of",var.lower())
# print("\nsqwapcase of",var.swapcase())
# print("\nfind",var.find("MeeT"))
# print("\nrepalce",var.replace("MeeT","hiren"))
# print("\count",var.count("e"))
# print("\split",var.split())

# second=int(input("Enter the seconds is:"))

# hours=0
# mintues=second//60
# second=second%60
# while(mintues>59):
#     hours=hours+1
#     mintues=mintues-60
# while(second>59):
#     mintues=mintues+1
#     second=second-60
# print(hours,":",mintues,":",second)


# second=int(input("Enter the seconds is:"))

# hours=0

# mintues=second//60
# second=second%60

# while(mintues>59):
#     hours=hours+1
#     mintues=mintues-60

# while(second>59):
#     mintues=mintues+1
#     second=second-60

# print(hours,":",mintues,":",second)

# val=(input("Enter the amount:"))

# s=val.split(".")
# if(len(s)>1):
#     print("Amount is",s[0],"repees and",s[1],"paisa")
# else:
#     print("amount is".s[0],"rupees and 00 paisa")

# val=int(input("Enter the number:"))
# if (val>0):
#     print("the number is positive")
# elif(val==0):
#     print("the nmbwr is zero")
# else:
#     print('the number is negative')

# val=int(input("Enter the number:"))

# c=0
# d=0

# for i in range(1,val):
#     if(i%2==0):
#         c=c+1
#     else:
#         d=d+1


# print("the even number is:",c)
# print("the odd number is:",d)

# for i in range(1500,2700):
#     if(i%7==0 and i%5==0):
#         print("the number is:",i)

# import random

# var=int(input("enter the amount of 1 to 10"))

# r=random.randrange(1,11)
# while(var!=r):
#     var=int(input("enter number not match"))
# if(var==r):
#     print("right 7 carode jit gaye aap")


# list=[57,89,78,1]
# print(list)

# list.insert(2,50)
# list.insert(0,25)

# list.pop(-2)
# list.reverse()

# print("the maximum is list:",max(list))
# print("the miinimum list:",min(list))

# list.sort()
# print("the list sort",list)
# print(list)

# print(list[0:3])

# list.append(54)
# print(list)''

# tuple1=(65,12,78,12,23,7)
# print(tuple1)

# print(tuple1[3])

# print(tuple1[-2])

# print(tuple1.count(12))
# t1=("ccv,'ooad","nosql")
# print(t1)

# T=(74,58,89,7,7,65,4)
# print(T)

# print("the 4 th elemwnt is",T[3], "the 2 elemenr is",T[-2])

# print(T.count(7))

# t1=("mono db","ccv","ooad")
# print(t1)

# print("the maximum num is tuple",max(T))

# def addition (n1,n2):
#     ans=n1+n2
#     return ans

# def substraction (n1,n2):
#     ans=n1-n2
#     return ans
# def maultiply(n1,n2):
#     ans=n1*n2
#     return ans
# def division (n1,n2):
#     ans=n1/n2
#     return ans

# n1=int(input("enter the number"))
# n2=int (input("enter second number"))
# op=(input(" enter the opration :"))

# f1=addition(n1,n2)
# f2=substraction(n1,n2)
# f3=maultiply(n1,n2)
# f4=division(n1,n2)

# if(op=='+'):
#   print(f1)
# elif(op=='-'):
#     print(f2)
# elif(op=='*'):
#     print(f3)
# elif(op=='/'):
#     print(f4)

# def d(lim):

#     for i in range(1,6):
#         if(i%2==0):
#             for j in range(1,lim+1):
#               if(j%2==0):
#                   print("1",end=" ")
#             else:
#                   print("0",end=" ")
#             print()

#         else:
#             for k in range(1,lim+1):
#                 if(k%2==0):
#                     print("0",end=" ")
#                 else:
#                     print("1",end=" ")
#             print()

# i =int(input("enter the number"))
# print(d(i))  

# Students={"student1" : { Rollno”: 1,“name”:“MEET”,“semester”:1,“course”: “MSCIT”,“percentage”: 87.2}},{“student2”:{“Rollno”:2,“name”: “KISHAN”,“semester”:1,“course”: “MBA”,“percentage”: 74.2}},{“student3”: {“Rollno”:1,“name”: “NARENDRA”,“semester”:1“course”: “PHYSICS”,“percentage”: 94.2}},{“student4”: {“Rollno”:4,“name”: “SMIT”,“semester”:1“course”: “CHEMISTRY”,“percentage”: 67.2}},{“student5”: {“Rollno”:5,“name”: “DARSHAN”,“semester”:1“course”: “BIOLOGY”,“percentage”: 94.2}},

# Stack= []

# while True:

#     print("Menu")
#     print("1.push")
#     print("2,pop")
#     print("3.display")
#     print("4.exit")

#     choice=int(input("enter your choice"))

#     if(choice==1):
#       element=input("enter the elemnt to push")
#       Stack.append(element)
#       print(element,"pushed to the stack")
#     elif choice==2:
#       if len(Stack)==0 :
#          print("stack is empty  cannot pop from empty stack")
#       else:
#            popped_element=Stack.pop()
#            print("popped_element",popped_element)

#     elif choice==3:
#            if len(Stack)==0:
#               print("stack is empty")
#            else: 
#             print("stack",Stack)
    
#     elif choice==4:
#        print("exit")
#        break
#     else:
#        print("invalid")
# list=[1,2,3,4]
# print(list[-3:-1])

# i=1
# while(i<=5):
#     print(i * " *")
#     i=i+1

# i=5
# while(i>=0):
#     print(i * " *")
#     i=i-1


# num=int(input(""))

# 

# tuple=(78,12,12,58,6)
# print(tuple)

# print(tuple[0,3],tuple[-1-2])


# print(tuple.count(12))



# print(min(tuple),max(tuple))
# print(tuple)


