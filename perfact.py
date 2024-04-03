#find num is perfect or not
#n=int(input("enter a any nuumber:"))
#sum1=0
#for i in range(1,n):
     #if(n%i==0):
        #sum1=sum1+i
#if(#sum1==n):
     #print("the number is  perfact nuumber")
#else:
     #print("the number is not perfact  number")

#find num is palindrome or not

# n=int(input("enter a any nuumber:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
    
# if(temp==rev):
#     print("the number is palindrome")
# else:
#     print("the number is not a palindrome")

# # * pattern use python
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
    # print()


# for i in range(1,101):
#     print(i)

# i=1
# while(i<6):
#     print(i)
#     i=i+1
    
# for i in range(11,101):
#     if(i%2==0):
#         print(i)

# n1=int(input("Enter first number"))5

# n2=int(input("Enter second number"))
# n3=int(input("Enter third number"))

# if(n1>n2):
#     if(n1>n3):
#         print("the largest number is:",n1)
#     else:
#         print("the largest number is:",n3)
# else:
#     if(n2>n3):
#         print("the largest number is:",n2)
#     else:
#         print("the largest number is:",n3)

# n1= int(input("Enter the student percentage"))

# if(n1>=85):
#     print("Grade -A")
# elif(n1<85 and n1>=75):
#     print("Grade- B")
# elif(n1<75 and n1>=65):
#     print("Grade - c")
# else:
#     if(n1<65):
#         print("Fail")

# num= int(input("Enter the number"))

# if num>1:
#     for i in range (2,int(num/2)+1):
#         if(num%i == 0):
#             print("not a prime number",num)
#             break
#     else:
#          print("prime number",num) 
# else:
#     print("it is not a prime numb5
# er",num)

# num= int(input("Enter any number"))

# sum=0

# for i in range(1,num):
#     if(num%i==0):
#         sum=sum+i

# if (num==sum):
#     print("this is perfect number")
# else:
#     print("not pefect")


# var= int(input("Enter any number"))

# rev=0
# x=var

# while(var>0):
#            rev=(rev*10 + var%10)
#            var=var//10
# if(x==rev):
#     print("palindrone number")
# else:
#     print("not palindrone")

# import math

# n1= int(input("Enter first number"))
# n2= int(input("Enter second number"))
# n3= int(input("Enter minus number"))

# print("Absolute value",abs(n3))
# print("ceil of number",math.ceil(n1/n2))
# print("max num",max(n1,n2))
# print("min num",min(n1,n2))
# print("sqrt roor",math.sqrt(n1))
# print("floor division",math.floor(n1/n2))
# print("power",math.pow(n1,2))
# print("round of two num",round(n1/n2))

# import random

# count=0

# for i in range(41,75,1):

#     if(count!=20):
#         print(random.randrange(41,75,1))
#         count=count+1



name=("my Father nAme Is maheSHbhaI")
print(name.capitalize())
print(name.center(40))
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.split())
print(name.find("he"))
print(name.endswith("I")) 
print(name.replace("Is", "are")) 
# print(name.endswith("I")) 




