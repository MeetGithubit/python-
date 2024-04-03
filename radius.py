# r=float(input("entre a radius value"))
# value=3.14*r*r
# print("result is:",value)


# n=int(input("enter a number:"))

# if (n<0):
#     print("negative")
# elif(n==0):
#     print("zero")
# else:
#     print("positive")


# 

import time

timestamp=time.strftime('%H:%M:%S')
print(timestamp)

val=int(input("enter time:"))

if(val>6 and val<12):
    print("Good morning bhai")
elif(val>12 and val<17):
    print("Good aftrtnoon")
elif(val>17 and val<24):
    print("Good night")
else:
    print("Chal chal have!!!")