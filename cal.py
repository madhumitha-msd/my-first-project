print("=== simple calculator ===")
num1=float(input("enter your first number"))
num2=float(input("enter your second number"))
print("choose the operation")
print("1. addition (+)")
print("2. subtraction (-)")
print("3. multiplication (*)")
print("4. division (/)")
choice = input("enter ur choice like 1 to 4")
if choice=="1":
     print("result is",num1+num2)
elif choice=="2":
     print("result is",num1-num2)
elif choice=="3":
     print("result is",num1*num2)
elif choice=="4":
     if num2!=0:
        print("result is",num1/num2)
     else:
        print("cannot divisible by zero")
else:
   print("Invalid Choice .Try again")
