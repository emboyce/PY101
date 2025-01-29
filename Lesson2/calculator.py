# Ask user for first number
# Validate first number
# Ask user for second number
# Validate second number
# Ask user for type of operation
# Validate type of operation
# Match case on operation
# Perform operation
# Display result

print("Welcome to the Calculator!")

while True:
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("You must enter a valid number.")
        continue
    else:
        break

while True:
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("You must enter a valid number.")
        continue
    else:
        break

while True:
    message = """
    Enter one of the following options:
         Multiply - enter "m"
         Divide - enter "d"
         Subtract - enter "s"
         Add - enter "a"
    Your option: """

    operation = input(message)
    if operation in ("m", "d", "s", "a"):
        break
    print("You must enter a valid letter, no quotes.")

match operation:
    case "m":
        answer = num1 * num2
    case "d":
        answer = num1/num2
    case "s":
        answer = num1 - num2
    case "a":
        answer = num1 + num2
    case _:
        print("You have escaped the error handling.")

print(f"{answer:.2f}")
