#a=float(25)
#print(a)
#b=int(63.25)
#print(b)

#for i in range(1500,2700):
    #if(i%7==0 and i%5==0):
        #print("The number is:",i)

# import random
# var=int(input("Enter the number between 1 to 10"))
# r=random.randrange(1,11)
# while(var!=r):
#     var=int(input("Not Match enter another number"))
# if(var==r):
#     print("Guess is right")

# def calculate_toatl_salary(name,department,basic_salary=9000):

#         DA=0.1*basic_salary
#         HRA=0.15*basic_salary
#         total_salary= basic_salary+DA+HRA 
#         return total_salary 

# name=input("Enter employee name:")
# department=input("Enter department:")
# basic_salary=input("Enter basic salary(optional)")
        
# if basic_salary:
#      total_salary=calculate_toatl_salary(name,department,float(basic_salary))
# else:
#     total_salary=calculate_toatl_salary(name,department)

# print("Total salary of",name,"in",department,"is",total_salary)


# def fibonacci(n):
#     if n<=0:
#         return []
#     elif n==1:
#         return[0]
#     elif n==2:
#         return[0,1]
#     else:
#         fib_series=fibonacci(n-1)
#         fib_series.append(fib_series[-1]+fib_series[-2]
#         return fib_series
    
#     #test function
# number_of_terms=int(input("Enter the number of terms in the Fibonacci series:"))

# fibonacci_series=fibonacci(number_of_terms)

# print("The Fibonacci series up to",number_of_terms,"terms is",fibonacci_series)


# 

# st='''hey said,
# i am meet sathvara
# i am goood boy
# "i want an appple nd manhgp"'''
# name="kishan"
# print(name[-4:-2])

# b="rajamouli and nagaarjun"
# nm="i am Meet I Am a software developer,Meet,is I !!!"
# print(len(nm))

# print(nm.upper())
# print(nm.lower())
# print(nm.rstrip("!"))
# print(nm.split(" "))
# print(nm.replace("Meet","ravi"))
# print(nm.capitalize())
# print(b.center(80))
# print(nm.count("Meet"))
# print(nm.endswith("!!!"))
# print(nm.endswith("so",4,18))
# print(nm.find("d"))
# print(nm.index("a"))


n1=int(input("enter 1 numver"))
n2=int(input("enter 2 numver"))
n3=int(input("enter 3 numver"))
n4=int(input("enter 4 numver"))
n5=int(input("enter 5 numver"))

mul=n1+n2-n3*n4/n5

print("the sum of above range num:",mul)









