# students={
#     "student1":{
#     "Roll no":1,
#     "name":"MEET",
#     "semester":1,
#     "course":"MSCIT",
#     "percentage":87.2},
    
#     "student2":{
#     "Roll no":2,
#     "name":"KISHAN",
#     "semester":1,
#     "course":"MBA",
#     "percentage":78.2},

#     "student3":{
#     "Roll no":3,
#     "name":"NARENDRA",
#     "semester":1,
#     "course":"PHYSICS",
#     "percentage":89.8},


#     "student4":{
#     "Roll no":4,
#     "name":"SMITH",
#     "semester":1,
#     "course":"CHEMISTRY",
#     "percentage":90.2},

#     "student5":{
#     "Roll no":5,
#     "name":"DARSHAN",
#     "semester":1,
#     "course":"BIOLOGY",
#     "percentage":81.2}}


# #update semester of student3 to 2
# students["student3"]["semester"]= 2

# #delete the data of 4th student
# del students["student4"]

# #copy this disctionary to dict2
# dict2=students.copy()

# #dispaly the length of both the disctionaries
# print("Lenght of student dictionary:",len(students))

# print("length of dict2 dictionary",len(dict2))

# countries= {
#     "Spain":"Madrid",
#     "France":"Paris",
#     "Germany":"Berlin",
#     "Norway": "Oslo"}

# print("The capital of Germany is",countries["Germany"])

# del countries["Norway"]

# user_country=input("Enter a country:")

# if user_country in countries:
#     print("The index of",user_country,"is",list(countries.keys()).index(user_country))
# else:
#     print(user_country,"is not present in the dictionary.")

#     countries["india"]="New Dellhi"

#     print(countries)


# stack=[]
# while True:
#     print("Menu:")
#     print("1.Push")
#     print("2.Pop")
#     print("3.Dispaly")
#     print("4.Exit")

#     choice=int(input("Enter your choice:"))

#     if choice==1:
#         element=input("Enter the element to push:")
#         stack.append(element)
#         print(element,"pushed to the stack")

#     elif choice==2:
#         if len(stack)==0:
#             print("stack is empty.cannot pop from an empty stack")
#         else:
#               popped_element=stack.pop()
#               print("popped element:",popped_element)
#     elif choice ==3:
#         if len(stack)==0:
#             print("stack is empty.")
#         else:
#             print("stack:",stack)
    
#     elif choice==4:
#         print("Exiting.....")
#         break
#     else:
#         print("invalid choice.please enter a valid option.")


# queue=[]

# while True:
#     print("Menu:")
#     print("1.Insertion")
#     print("2.Deletion")
#     print("3.Display")
#     print("4.Exit")

#     choice=int(input("enter your choice:"))

#     if choice==1:
#         element=input("Enter the element to Insert:")
#         queue.append(element)
#         print(element,"insertion into the queue.")

#     elif choice==2:
#         if len(queue)==0:
#             print("queue is empty.cannot Delete from an empty queue.")
#         else:
#             deleted_element=queue.pop(0)
#             print("Deleted element:",deleted_element)
#     elif choice==3:
#         if len(queue)==0:
#             print("Queue is empty.")
#         else:
#             print("Queue:",queue)
#     elif choice==4:
#         print("Exiting...")
#         break
#     else:
#         print("invalid choice.please enter a valid option.")

def calculate_toatl_salary(name,department,basic_salary=9000):

    DA=0.1*basic_salary
    HRA=0.15*basic_salary
    total_salary=basic_salary+DA+HRA
    return total_salary

name=input("Enter employee name:")
department=input("Enter department:")
basic_salary=input("Enter basic salary(optional)")
    
if basic_salary:
     total_salary=calculate_toatl_salary(name,department,float(basic_salary))
else:
     total_salary=calculate_toatl_salary(name,department)
print("Total salary of",name,"in",department,"is",total_salary)

