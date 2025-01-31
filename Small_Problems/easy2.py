def greetings(name_list, title_dict):
    full_name = " ".join(name_list)
    full_title = f"{title_dict["title"]} {title_dict["occupation"]}"
    message = f"Greetings, {full_name}! Nice to have a {full_title} around."
    return message

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

def yelly_greeting():
    name = input("What is your name?: ")
    if name[-1] == "!":
        print(f"HELLO {name.upper()}!")
    else:
        print(f"Hello {name}.")

# yelly_greeting()

def multiply(num1, num2):
    return num1 * num2

print(multiply(5, 3) == 15)  # True

def square(num):
    return multiply(num, num)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

def operate(num1, num2, operand):
    for operator in operand:
        print(f"{num1} {operator} {num2} = " , 
              str(eval(f"{num1}{operator}{num2}")))

# operate(input("Enter first num: "), input("Enter second num: "),
#         ["+", "-", "*", "/", "//", "%", "**"])

def penultimate(string):
    words = string.split()
    return words[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

def middle(string):
    words = string.split()
    if words == [] or len(words) % 2 == 0:
        return "Middle word is poorly defined. Empty or even string."
    else:
        return(words[len(words) // 2])
    return words

print(middle(""))
print(middle("hello world"))
print(middle("hello to world"))
print(middle("hello to the whole world"))
print(middle("hello to the whole wide world"))

def xor(check1, check2):
    return (True if (check1 or check2) and not (check1 and check2) else False)

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
