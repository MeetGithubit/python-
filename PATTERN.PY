#ef d(lim):
    #for i in range(1,6):
        #if(i%2==0):
            #for j in range(1,lim+1):
                #if(j%2==0):
                    #print("1",end=" ")
                #else:
                    #print("0",end=" ")
            #print()
        #else:
                 #for k in range(1,lim+1):
                      #if(k%2==0):
                           #print("0",end=" ")
                      #else:
                           #print("1",end=" ")
                 #print()

#i=int(input("enter the number :"))
#print(d(i)) 

#def i(limit):
    #c=1
    #for i  in range(1,limit+1):
        #for j in range(1,i):
            #print(c,end=" ")
            #c=c+1
        #print()

#i1=int(input("Enter the number:"))
#print(i(i1))



#def p(limit):
    #for i  in range(1,limit+1):
        #for j in range(1,i+1):
            #print("*",end=" ")
        #print()

    #for k in range(1,limit+1):
        #for p in range(k,limit):
            #print("*",end=' ')
        #print()

#i=int(input("Enter the number:"))
#print(p(i))

#def fact(number):
   # c=1
    #for i in range(1,number+1):
       # c=c*i
    #return c

#i=int(input("Enter the number:"))
#c=fact(i)
#print("Factorial number is:",c)

#def func(num1,num2):
    #list1=[]
    #list2=[]
    #list3=[]
    #c=0
    #d=0
    #for i in range(1,num1+1):
        #if(num1%i==0):
           # list1.insert(c,i)
           # c=c+1
    
    #for j in range(1,num2+1):
        #if(num2%j==0):
           # list2.insert(d,j)
           # d=d+1
        
    #for k in range(1,len(list1)):
      #  c1=0
        #(list1[k]==list2[m]):
                #list3.insert(c1,list1[k])
              #  c1=c1+1
    #if(len(list3)==0):
       # return 1
    #else:
      #  return max(list3)
    
#i1=int(input("enter the number1 is:"))
#j1=int(input("enter the number2 is:"))
#c1=func(i1,j1)
#print("The GCD of two number is:",c1)

def li(a):
    total=0
    avg=0
    for i in a:
        total+=i
        avg=total/len(a)
    return total,avg

i=int(input("Enter the total number:"))
d=[]
for j in range(1,i+1):
    c1=int(input("Enter the number:"))
    d.insert(j-1,c1)
c=li(d)
print("Sum of the elements are ",c[0])
print("avg of the elements are ",c[1])




                   
    
                    
