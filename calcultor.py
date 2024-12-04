x= float(input("first number:"))
y=float(input("second number:"))
operation = input("Enter the operation:")
while True:
    if operation == "+":
        print(x+y)
    elif operation == "-":
        print(x-y)
    elif operation == "*":
        print(x*y)
    elif operation == "/":
        if y == 0:
            print("Dividing by 0 is not possible.")
        else:
            print(x/y)
    elif operation == "**":
        print(x**y)
    else:
        print("invalide operation")
