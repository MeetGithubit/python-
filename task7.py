# class student:

#     def __init__(self, name, rollno, m1, m2):

#         self.name = name
#         self.rollno = rollno
#         self.m1 = m1
#         self.m2 = m2

#     def accept(self, Name, Rollno, marks1, marks2):
#          ob = student(Name, Rollno, marks1, marks2)
#          Is.append(ob)

#     def dispaly (self,ob):
#         print("Name:",ob.name)
#         print("Rollno:",ob.rollno)
#         print("Marks1:",ob.m1)
#         print("Marks2:",ob.m2)
#         print("\n")

#     def search (self,rn):
#         for i in range(len(Is)):
#             if Is[i].rollno == rn:
#                 return i
            
#     def delete(self,rn):
#         i = obj.search(rn)
#         if i is not None:
#             del Is[i]

#     def upadte(self,rn,No):
#         i = obj.search(rn)
#         if i is not None:
#             Is[i].rollno = No

 
# Is = []
# obj = student('',0,0,0)

# while True:
#     print("\n Opearation available:")
#     print("1. Accept student details")
#     print("2. Display student Details ")
#     print("3. search Details of a student")
#     print("4. Delete Details of student")
#     print("5. Update student Details")
#     print("6. Exit")

#     ch = int(input("Enter choice :"))

#     if ch == 1:
#         obj.accept(input("Enter name: "),int(input("Enter Rollno: ")),int(input("Enter Marks1: ")),int(input("Enter marks2: "))) 

#     elif ch == 2:
#         print("\nlist of student\n")
#         for i in range (len(Is)):
#             obj.dispaly(Is[i])

#     elif ch == 3:
#         rn = int(input("Enter Rollno to search:"))
#         s = obj.search(rn)
#         if s is not None:
#             obj.dispaly(Is[s])
#         else:
#             print("student not founnd")

#     elif ch == 4:
#         rn = int(input("Enter rollno to delete:"))
#         obj.delete(rn)
#         print("list after deletion")
#         for i in range(len(Is)):
#             obj.display(Is[i])

#     elif ch == 5:
#         rn = int(input("Enter Rollno to update:"))
#         new_roll = int(input("Enter new Rollno:"))
#         obj.update(rn,new_roll)
#         print("List after updation")
#         for i in range(len(Is)):
#             obj.display(Is[i])

#     elif ch == 6:
#         break

#     else:
#         print("invalid choice.please choose a valid option")

# print("Thank you!")

# class Employee:
#     def __init__(self, name, id, company):
#        self.name = name
#        self.id = id
#        self.company = company

#     def accept(self, Name, id, company):
#      ob = Employee(Name, id, company)
#      Is.append(ob)

#     def display(self, ob):
#        print("Name: ", ob.name)
#        print("Employee Id: ", ob.id)
#        print("Company Name: ", ob.company)
#        print("\n")

#     def search(self, rn):
#         for i in range(len(Is)):
#              if Is[i].id == rn:
#                 return i
             
#     def delete(self, rn):
#      i = obj.search(rn)
#      if i is not None:
#            del Is[i]

#     def update(self, rn, No):
#      i = obj.search(rn)
#      if i is not None:
#         Is[i].id = No

# Is = []
# obj = Employee('', 0, '')

# while True:
#           print("\nOperations available:")
#           print("1. Accept Employee details")
#           print("2. Display Employee Details")
#           print("3. Search Details of an Employee")
#           print("4. Delete Details of an Employee")
#           print("5. Update Employee Details")
#           print("6. Exit")


#           ch = int(input("Enter choice:"))

#           if ch == 1:
#                     obj.accept(input("Enter Name:"), int(input("Enter Id:")), input("Enter Company Name:"))

#           elif ch == 2:
#                      print("\nList of Employees\n")
#                      for i in range(len(Is)):
#                           obj.display(Is[i])

#           elif ch == 3:
#                      rn = int(input("Enter Id to search:"))
#                      s = obj.search(rn)
#                      if s is not None:
#                          obj.display(Is[s])
#                      else:
#                          print("Employee not found.")
               
#           elif ch == 4:
#                     rn = int(input("Enter ID to delete:"))
#                     obj.delete(rn)
#                     print("List after deletion")
#                     for i in range(len(Is)):
#                          obj.display(Is[i])

#           elif ch == 5:
#                     rn = int(input("Enter ID to update:"))
#                     new_id = int(input("Enter new ID:"))
#                     obj.update(rn, new_id)
#                     print("List after updation")
#                     for i in range(len(Is)):
#                            obj.display(Is[i])

#           elif ch == 6:
#                      break
          
#           else:
#                print("Invalid choice. Please choose a valid option.")
# print("Thank You!")

# numbers = [1,7,14,21,28,35,42,49,56,63]
# result = list(map(lambda x: x*7+10,numbers))

# print("original list:",numbers)
# print("Modified list  (multiples of 7+10):", result)

# import math

# from multipledispatch import dispatch

# class Surface:
#       @dispatch(int)

#       def area(self, l):
#         areas = 6 * l ** 2
#         print('Cube:', areas)

#       @dispatch(float)

#       def area(self, r):
#          areas = 4 * math.pi * r ** 2
#          print('Sphere:', areas)

#       @dispatch(int, int)

#       def area(self, r, h):
#          areas = 2 * math.pi * r * (r + h)
#          print('Cylinder:', areas)

# obj = Surface()
# obj.area(5)

# class Person:

#     def __init__(self, name, code):
#        self.name = name
#        self.code = code

# class Account(Person):

#      def __init__(self, name, code, pay):
#         Person.__init__(self, name, code)
#         self.pay = pay

# class Admin(Person):

#      def __init__(self, name, code, experience):
#         Person.__init__(self, name, code)
#         self.experience = experience

# class Master(Admin, Account):
#       def __init__(self, name, code, pay, experience):
#             Admin .__init__(self, name, code, experience)
#             Account.__init__(self, name, code, pay)

# person1 = Person("Aman", 501)
# accountant1 = Account("Hardik", 601, 5000)
# admin1 = Admin("Hnkal", 701, 5)
# master1 = Master("Dhruv", 801, 9000, 8)

# print("Person:", person1.name, person1.code)
# print("Accountant:", accountant1.name, accountant1.code, accountant1.pay)
# print("Admin:", admin1.name, admin1.code, admin1.experience)
# print("Master:", master1.name, master1.code, master1.pay, master1.experience)

# class Vehicle:

#      def __init__(self, ModelNo, Type, Price):
#          self.ModelNo = ModelNo
#          self.Type = Type
#          self.Price = Price

#      def display(self):
#          print("Model No:", self.ModelNo)
#          print("Type:", self.Type)
#          print("Price:", self.Price)

# class Car(Vehicle):

#      def __init__(self, ModelNo, Type, Price, EngineNumber, Color, FuelType):
#            super().__init__(ModelNo, Type, Price)
#            self.EngineNumber = EngineNumber
#            self.Color = Color
#            self.FuelType = FuelType

#      def display(self):
#             super().display()
#             print("Engine Number:", self.EngineNumber)
#             print("Color:", self.Color)
#             print("Fuel Type:", self.FuelType)

# class Bike(Vehicle):
     
#       def __init__(self, ModelNo, Type, Price, MachineCC, Mileage):
#             super().__init__(ModelNo, Type, Price)
#             self.MachineCC = MachineCC
#             self.Mileage = Mileage
              
#       def display(self):
#             super().display()
#             print("Machine CC:", self.MachineCC)
#             print("Mileage:", self.Mileage)

# car1 = Car("NexonEV", "TATA", 90000, "78562146", "Sliver", "Charging")

# bike1 = Bike("Apache", "Sports", 75000, 450, "35 km/l")

# print("Car Details:")
# car1.display()
# print("\nBike Details:")
# bike1.display()

# numbers = [5, 10, -2, -7, 0, 30, 9]
# positive_numbers = list(filter(lambda x: x > 0, numbers))
# negative_numbers = list(filter(lambda x: x < 0, numbers))
# zero_numbers = list(filter(lambda x: x == 0, numbers))

# print("Positive Numbers:", positive_numbers)
# print("Negative Numbers:", negative_numbers)
# print("Zero Numbers:", zero_numbers)






