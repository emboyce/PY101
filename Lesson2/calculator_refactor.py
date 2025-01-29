# Ask user for first number
# Validate first number
# Ask user for second number
# Validate second number
# Ask user for type of operation
# Validate type of operation
# Match case on operation
# Perform operation
# Display result

def prompt(message):
    print(f"==> {message}")

def validate(number):
    while True:
        try:
            float(number)
            return True
        except ValueError:
            return False


prompt("Welcome to the Calculator!")

prompt("Enter the first number:")
num1 = input()
while not validate(num1):
    prompt("You must enter a valid number:")
    num1 = input()
num1 = float(num1)

prompt("Enter the second number:")
num2 = input()
while not validate(num2):
    prompt("You must enter a valid number:")
    num2 = input()
num2 = float(num2)

while True:
    prompt("""Choose a number for which operation to perform:
    1 - Addition 2 - Subtraction 3 - Multiplication 4 - Division""")
    operation = input()
    if operation in ("1", "2", "3", "4"):
        break
    prompt("You must enter a valid number to select.")

match operation:
    case "1":
        answer = num1 + num2
    case "2":
        answer = num1 - num2
    case "3":
        answer = num1 * num2
    case "4":
        answer = num1 / num2
    case _:
        prompt("You have escaped the error handling.")

prompt(f"The result is: {answer:.2f}")
