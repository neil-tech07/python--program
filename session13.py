#Single inheritance

# class A:
#     varA= "welcome to class A"
# class B:
#     varB= "welcome to class B"
# class C(A,B):
#     varC= "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#Multi-level inheritance 

# class Car:
#     @staticmethod    #decorator
#     def start():
#         print("Car started...!")

#     @staticmethod    #decorator
#     def stop():
#         print("Car stopped!!!")

# class Toyotacar(Car):
#     def __init__(self , brand):
#         self.name = brand

# class Fortuner(Toyotacar):
#     def __init__(self , type):
#         self.type = type

# car1 = Fortuner("disel")
# car1.start()
# car1.stop()


#POLYMORPHISM :->

class Complex:
    def __init__ (self , real , img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i +", self.img , "j")

    def __add__(self , num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal , newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,5)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()
