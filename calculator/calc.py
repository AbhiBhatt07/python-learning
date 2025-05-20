# Function's of calculation. 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "⚠️ Error: Division by zero!"

# Display menu
print("📱 Basic Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")


try: 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("result: ", add(num1, num2))
    elif choice == "2":
        print("result: ", subtract(num1, num2))
    elif choice == "3":
        print("result: ", multiply(num1, num2))
    elif choice == "4":
        print("result: ", divide(num1, num2))
    else: 
        print("Please enter the vaild choice, 1, 2, 3, or 4.")

except ValueError:
    print("⚠️ Please enter valid numbers!")