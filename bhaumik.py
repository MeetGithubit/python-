# a=(5**3)
# print(a)

# num1=int(input("Enter a first number:"))

# operator=(input("enter a operator(+,-,*,/,//,):"))
# num2=int(input("Enter a second number:"))


# if(operator=='+'):
#    print(num1+num2)
# elif(operator=='-'):
#    print(num1-num2)
# elif(operator=='*'):
#    print(num1*num2)
# elif(operator=='/'):
#    print(num1/num2)
# else:
#    print("inalid operator")

# class Fact(object):
    
#     def __init__(self,numerator=1,denominator=1):
#          self.denominator=denominator
#          self.numerator=numerator

#     def add(self,f):
#            if self.denominator == f.denominator:
#                 return (self.numerator + f.numerator), self.denominator
#            else:
#                 n1=(self.numerator * f.denominator) + (self.denominator * f.numerator)
#                 n2=(self.denominator * f.denominator)
#                 return n1,n2
                     
    
#     def mul(self,m):
#          if  (self.denominator == m.denominator):
#             return (self.numerator * m.numerator), self.denominator
#          else:
#               n1=(self.numerator * m.denominator) * (self.denominator * m.numerator)
#               n2=(self.denominator * m.denominator)
#               return n1,n2
         
# def main():
#      object1 = Fact(1,4)
#      object2 = Fact(1,4)
#      n,d = object2.add(object1)
#      print(n,"/",d)
#      m,l = object2.mul(object1)
#      print(m,"/",l)
# main()


# class len(object):

#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         return self.length * self.breadth
    
# def main():
#     object2 = len(30,24)
#     print("The Area is:",object2.area())
# main()=x


# import math

# class point(object):
#     def __init__(self,x,y):

#         self.x=x
#         self.y =y

#     def ec(self,p):
#         return math.sqrt(((self.x-p.x)**2) + ((self.y-p.y)**2))
    
# def main():
#     obj1 = point(4,2)
#     obj2 = point(7,2)
#     print(obj2.ec(obj1))

# main()

# 
# class mark(object):

#     def __init__(self,name,sem,marks):

#         self.name = name
#         self.sem = sem
#         self.marks = marks

#     def mar(self):
#         sum=0
#         for i in self.marks:
#             sum = sum+i
#         return sum / len(self.marks)
    
# def main():
#     obj1 = mark(name = 'patel kishan',sem=5,marks=[80,40,50,60,78,98])
#     print(obj1.mar())

# main()


# class complex(object):

#     def __init__(self,r=0 ,i=0):

#         self.r = r
#         self.i = i

#     def com(self,x,y):
#         self.x = x.r + y.r
#         self.y = x.i + y.i
#         return complex(self.x, self.y)
    
#     def mul(self, x1,y1):
#         self.x = x1.r * y1.r
#         self.y = x1.i * y1.i
#         return complex(self.x, self.y)
    
# def main():
#     obj1 = complex(10,20)
#     obj2 = complex(30,50)
#     obj3 = complex()
#     obj4 = complex()
#     obj3 = obj3.com(obj1,obj2)
#     obj4 = obj4.mul(obj1,obj2)

#     print("The sum imaginary number",obj3.i)
#     print("The sum real number",obj3.r)
#     print("The mul imaginary number",obj4.i)
#     print("The mul real number",obj4.r)

# main()


# class dat(object):

#     def __init__(self,year,day,month):
#         self.year = year
#         self.day = day
#         self.month = month
     
#     def validate(self):
#         if self.isday() and self.ismonth() and self.isyear():
#             return "the  date is digit"
#         else:
#             return "the date is wrong"
        
#     def ismonth(self):
#         if self.month>=1 or self.month<13:
#             return True
#         else:
#             return False
        
#     def isyear(self):
#         if self.year >= 1 or self.year<9999:
#             return True
#         else:
#             return False
        
        
#     def isday(self):
#        match(self.month):
#         case 1,3,5,7,8,10,12:
#                return self.day >=1 or self.day<32
           
#         case 2:
#                return self.day >=1 or self.day <30
           
#         case default:
#                return self.day >=1 or self.day<31
           
# def main():
#     obj1 = dat(month=3,day=12,year=2003)
#     print(obj1.validate())

# main()

# class Height:

#     def __init__(self,feet,inch):
#         self.feet = feet
#         self.inch = inch
    
#     def is_valid_height(self):
#         return self.inch < 12
    
#     def add_height (self,other):
#         total_feet = self.feet + other.feet
#         total_inch = self.inch + other.inch

#         if total_inch >= 12:
#             total_feet += total_inch // 12
#             total_inch = total_inch % 12
#             return Height(total_feet, total_inch)
    
#     def display_height(self):
#         if self.is_valid_height():
#             print(f"{self.feet} feet {self.inch} inches")
#         else:
#             print("Invalid Height")

# height1 = Height(5,8)
# height2 = Height(3,10)

# height3 = height1.add_height(height2)
# height3.display_height()

# n=int(input("enter a number is:"))

# match n:

#     case 0:
#         print("n is zero")
#     case 1:
#         print('n is positive')
#     case 2:
#         print("n is nehative")
#     case default:
#         print("invalid n")



# for i in range(1,15,3):
#      print(i)

# colors= ["red","blue","green","gray","yellow","white","black"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# i=0
# while True:
#     print(i)
#     i=i+1
#     if(i%20 == 0):
#         break


# 
# for i in range(30):
#         if(i == 25):
#             print("skip")
#             continue
#         print(i)

# 

# def calculategmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)

# def isGreater(a, b):
#  if (a>b):
#    print("first number is greate")
#  else:
#    print("second number is greate")
        
# a=9
# b=8

# isGreater(a, b)
# calculategmean(a, b)


# c=8
# d=74

# # isGreater(c, d)
# # calculategmean(c, d)


def name(** name):
#     # 
    
#     print("Hello",name["fname"],name["mname"],name["lname"])

# name(mname="Meet",fname="sathavara",lname="maheshbhai")
    # print("the average is:",sum/len(numbers))
#     return 1


# c=average(5,6,7,1,8)
# # print(c)