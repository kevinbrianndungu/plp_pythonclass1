num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
operator=(input("key in the operator(*,+,-,/ :"))

if operator=="*":
    result = num1 * num2
    print(f"{num1} + {num2} = {result}")
elif operator=="+":
    result = num1 + num2
    print(f"{num1} + {num2} ={result}")
elif operator=="-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator=="/":
    if num2 != 0:
          result = num1 / num2 
          print(f"{num1} / {num2} ={result}")
    else :
          print("calculation error")
else:
    print("operation error!")
