# def sum(a , b , c , d , e): #parameter
#     sum = a+b+c+d+e
#     print(sum)
#     return sum

# sum(10 , 20 , 30, 50 , 70) #30
# sum(3 , 6 , 45 , 89 , 45)
# sum(900 , 1000 , 7000 , 400 , 600) #argument



# def print_hello():
#     print("HELLO , I'M NEIL ....")
    
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# def func_ave(a , b , c):
#     sum = a+b+c
#     print(sum/3)
#     return func_ave

# func_ave(6 , 7 , 8)
    

#1.
num = [1,2,3,4,5]

def list_len(list):
    print(len(list))

list_len(num)


#4.

def usd_inr(usd):
    con = 87*usd
    print("in inr : " , con)


usd_inr(2)

#2.
num = [1,2,3,4,5,6,7,8,9]
def list_single(list):
    for item in list:
     print(item , end=" ")

list_single(num)


#3.

def fact_num(n):
    fact = 1
    for i in range(1 , n+1):
       fact *=i
       print(fact)

fact_num(5)





