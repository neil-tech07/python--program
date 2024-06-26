
#WAP TO CREATE A CALCULATOR :->

print("CALCULATION :-> ")
f = str(input("ENTER THE FUNCTION YOU WANT [+ , - , * , / , %] : "))
no1 = int (input("ENTER THE FIRST NUMBER YOU WANT : "))
no2 = int (input("ENTER THE SECOND NUMBER YOU WANT : "))
if(f == "+"):
    print("ADDITION IS : no1 + no2 = ",no1,"+",no2, "=" , no1 + no2)
elif(f == "-"):
    print("SUBTRACTION IS : no1 - no2 = ",no1,"-",no2, "=" , no1 - no2)
elif(f == "*"):
    print("MULTIPLICATION IS : no1 * no2 = ",no1,"*",no2, "=" , no1 * no2)
elif(f == "/"):
    print("DIVISION IS : no1 / no2 = ",no1,"/",no2, "=" , no1 / no2)
elif(f == "%"):
    print("MODULO IS : no1 % no2 = ",no1,"%",no2, "=" , no1 % no2)
else:
    print(" INVALID INPUT ")



