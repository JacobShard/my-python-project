print("Welcome to Jacob's Calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1 = Add")
print("2 = Subtract")
print("3 = Multiply")
print("4 = Divide")

choice = input("Enter the number of your choice: ")

if choice == "1":
    result = num1 + num2
elif choice == "2":
    result = num1 - num2
elif choice == "3":
    result = num1 * num2
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid choice"

print("Result:", result)
