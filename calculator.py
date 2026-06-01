print(" Welcome To Python Calculater")

print("""

1. Addition 
2. Subtraction
3. Multiplication
4. Division
5. Exit

""")

choice = input("Choice the right number")

if choice == "1":
    num1 = int(input("Enter your grater number"))
    num2 = int(input("Enter Your smaler number"))
    if choice == "1":
        print("Your Addition is" , num1 + num2)
            
elif choice == "2":
    num1 = int(input("Enter your grater number"))
    num2 = int(input("Enter Your smaler number"))
    if choice == "2":
        print("Your Addition is" , num1 - num2)

elif choice == "3":
    num1 = int(input("Enter your grater number"))
    num2 = int(input("Enter Your smaler number"))
    if choice == "3":
        print("Your Addition is" , num1 * num2)

elif choice == "4":
    num1 = int(input("Enter your grater number"))
    num2 = int(input("Enter Your smaler number"))
    if choice == "4":
      print("Your Addition is" , num1 / num2)

else:
    print("Bhai Sahi Number Daal")
