# def add(num1,num2):
#     sum=num1+num2
#     return sum
# def sub(num1,num2):
#     subs=num1-num2
#     return subs
# def mul(num1,num2):
#     mult=num1*num2
#     return mult
# def div(num1,num2):
#     div = num1/num2
#     return div


# a = True

# while a:
#     print("###############")
#     print("Calculator")
#     print("###############")
#     choice = int(input("1 : Addition\n2 : substration\n3 : Multiplication\n4 : Divison\n5 : Quit\n Enter your choice:"))
#     num1 = int(input("Enter your first number: "))
#     num2 = int(input("Enter Your second number: "))
    
#     if choice == 1:
#         print("Result : ",add(num1,num2))
        
#     elif choice == 2:
#         print("Result : ",sub(num1,num2))
#     elif choice == 3:
#         print("Result : ",mul(num1,num2))
#     elif choice == 4:
#         print("Result : ",div(num1,num2))
#     elif choice == 5:
#         print("Exit")
#         a = False
#         break
        
#     else:
#         print("Invalid Number...! RETRY")

"""Another Method"""
        
def add(num1,num2):
    sum=num1+num2
    return sum
def sub(num1,num2):
    subs=num1-num2
    return subs
def mul(num1,num2):
    mult=num1*num2
    return mult
def div(num1,num2):
    div = num1/num2
    return div

a= True

while a:
    print("1.Add\n2.Substract\n3.Mul\n4.Div\n5.Exit...")
    choice = int(input("Enter your choice:"))
    if choice in (1,2,3,4,5):
        if choice == 5:
            print("exit...")
            break
            a=False
        elif choice==1:
            num1=int(input("Enter first num: "))
            num2=int(input("Enter Second num: "))
            print("Result: ",add(num1,num2))
        elif choice==2:
            num1=int(input("Enter first num: "))
            num2=int(input("Enter Second num: "))
            print("Result: ",sub(num1,num2)) 
        elif choice==3:
            num1=int(input("Enter first num: "))
            num2=int(input("Enter Second num: "))
            print("Result: ",mul(num1,num2))
        elif choice==4:
            num1=int(input("Enter first num: "))
            num2=int(input("Enter Second num: "))
            print("Result: ",div(num1,num2))
        