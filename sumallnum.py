#calculate sum of all num bet 71 to 80

sum=0
for i in range(71,81):
    print(i)
    sum+=i

print("the sum of all the number is :",sum)

#multiplication of all num bet 21 to 30

sum=1
for i in range(21,31):
    print(i)
    sum*=i

print("the multiplication of all nummber is :",sum)

#find num is prime or not input from user

num=int(input("enter any number :"))

if num>1:
    for i in range(2,int(num/2)+1):
        if(num%i==0):
          print(num,"is not a prime number")
        break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")







