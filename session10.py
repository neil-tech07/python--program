# class student:
#     name = "webbocket"

# s1 = student()
# print(s1)
# print(s1.name)

# s2 = student()
# print(s2)
# print(s2.name)


# class car:
#     color = "black"
#     brand = "tata altroz"
# car1 = car()
# print(car1.color)
# print(car1.brand)
# print(car1.color , car1.brand)


# class student:
#    def __init__(self , fullname):
#     self.name = fullname
#     print("we can add a student in our database : ")
# s1 = student("webbocket")
# print(s1.name)

# s2 = student("software")
# print(s2.name)


# class student: 
#   #default constructor 
#   def __init__(self):
#     pass
  
#   #parameterized constructor

#   def __init__ (self , name , marks):
#       self.name = name 
#       self.marks = marks
#       print("Adding new student to the database : ")
# s1 = student("webbocket" , 89)
# print(s1.name , s1.marks)

# s2 = student("software" , 98)
# print(s2.name , s2.marks)


# class student:
#     college_name = "ABC college"
#     name = "Anonymous" #class Attributes

#     def __init__(self, name, marks):
#         self.name = name #object attributes > class atrributes 
#         self.marks = marks
#         print("ADING NEW STUDENT TO THE DB : ")

# s1 = student("rohan", 98)
# print(s1.name) #rohan


#example of method :->

class student:
    def __init__ (self , name , marks):
        self.name = name
        self.marks = marks 

    def welcome(self):
        print("welcome student " , self.name)

    def get_marks(self):
        print("your mark is : " , self.marks)

s1 = student("rohan" , 98)
s1.welcome()
s1.get_marks()