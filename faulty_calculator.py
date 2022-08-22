                                       #FAULTY CALCULATOR
# 45*3==555 , 56+9==77 , 56/6==4

num1 = int(input("enter first no.= "))

print("select operators\n + , - , * , /")
opr = input("select operator")

num2 = int(input("enter second no.= "))


if num1==45 and num2==3 and opr=="*":
    print("555")
elif num1==56 and num2==9 and opr=="+":
    print("77")
elif num1==56 and num2==6 and opr=="/":
    print("4")
elif opr=="*":
    print("ans" ,num1*num2)
elif opr=="+":
    print("ans" , num1+num2)
elif opr=="-":
    print("ans" , num1-num2)
elif opr=="/":
   print("ans" , num1/num2)

else:
    print("invalide syntax")
