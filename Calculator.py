def calculator(a,b):
    print("Choose operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice=int(input("Enter your option\n"))
    match choice:
        case 1: 
            print("sum=",a+b)
        
        case 2:
            print("sub=",a-b)
        
        case 3:
            print("mul=",a*b)
        
        case 4:
            print("div=",a/b)
        case 5:
            print("Bye")
            
         
        case _:
            print("Invalid operation")

x=input("Do you want to start calculation(yes/no):\n")
while True:
  if(x=="yes"):
    a=int(input("Enter a\n"))
    b=int(input("Enter b\n"))
    calculator(a,b)
    x=input("Do you want to start calculation(yes/no):\n")
    continue
  else:
    print("Thank you for using calculator..")
    break 