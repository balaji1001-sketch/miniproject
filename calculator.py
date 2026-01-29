def add(a,b):
   return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        print("error,number not divisible by zero")
    return a/b

while True:
    print(".......Simple Calculator......")
    print("1.ADD")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.EXIT")
    
    
    choice=input("choose an option (1-5):")
    
    if choice=='5':
        print("calculator closed")
        break
    
    
    
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))

    
    if choice=='1': 
        print("result:",add(num1,num2))

    elif choice=='2':
        print("result:",sub(num1,num2))

    elif choice=='3':
        print("result:",mul(num1,num2))
    
    elif choice=='4':
        print("result:",div(num1,num2))
    else:
        print("something is wrong,invalid choice")
     