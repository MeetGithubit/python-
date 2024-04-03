a=int(input("enter a any number is even odd :"))
if(a%2==0):
    print("the number",a,"is even number.")
else:
    print("the number",a,"is odd number.")


#sum of 07 seven nuumber
a=int(input("enter a first number"))
b=int(input("enter a second number"))
c=int(input("enter a third number"))
d=int(input("enter a four number"))
e=int(input("enter a five number"))
f=int(input("enter a six number"))
g=int(input("enter a seven number"))

sum=a+b+c+d+e+f+g
print("The above sum of 7 number is:",sum)

#calculate sum of all num bet 71 to 80

sum=0
for i in range(71,80):
    print(i)
    sum+=i

    print("the sum of all the number",sum)
