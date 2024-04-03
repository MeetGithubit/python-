name="my name is meet"
print(name)
name=input("enter your name")
print("hi !"+name)

# length method use
data="meet sathavara"  #(count alfabet with space)
x=len(data)
print(x)

#lower method use         #upper case to set lower case
data="MEET SATHAVARA"
x=(data.lower())
print(x)

#upper method use
data="meet sathavara"   #lower case set to upper case
x=(data.upper())
print(x)

#use capitalize method   #first later will be capital 
data="meet sathavara"
x=(data.capitalize())
print(x)

#replace method use   #suppose you want to repalce 
data="meet sathavara"
x=(data.replace("sathavara","kadia"))
print(x)

#use split method
data="meet sathavara"
x=(data.split())
print(x)

#center method use
data="meet sathavara"
x=(data.center(80))
print(x)

#endswitch method use
data="meet sathavara"
x=(data.endswith("gr"))
print(x)

#find method use
data="meet sathavra"
x=(data.find("th"))
print(x)

#index method use
data="meet sathavara"
x=(data.index("v"))
print(x)

#isalpha method use  #("") inside character only capital not small and not space
data="MEET RAJA"
x=(data.isalpha())
print(x)

#isdigit method use  #data digit ma che k nahi te check karse
data="012345"
x=(data.isdigit())
print(x)

#isspace method use  #data  blank che k nahi te check karse
data=" "
x=(data.isspace())
print(x)

#istitle method use  #istitle method both name start letter will be capital then print true
data="Meet Sathavara"
x=(data.istitle())
print(x)

#iscount method use  #aa string ma apple word ne count karse
data="i like apple banana grapes apple guava pinepal strobery apple appple"
x=(data.count("apple"))
print(x)



