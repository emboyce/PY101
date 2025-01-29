import json

with open('calculator_multi.json', 'r') as file:
    MESSAGES = json.load(file)


def prompt(message):
    print(f"==> {message}")

def validate(number):
    while True:
        try:
            float(number)
            return True
        except ValueError:
            return False

if input("==> Use English or PigLatin\n") in ["PigLatin", "Piglatin", "piglatin"]:
    lang = "PigLatin"
else:
    lang = "English"

prompt(MESSAGES[lang]["welcome"])

def calculate():
    prompt(MESSAGES[lang]["num1"])
    num1 = input()
    while not validate(num1):
        prompt(MESSAGES[lang]["invalid"])
        num1 = input()
    num1 = float(num1)

    prompt(MESSAGES[lang]["num2"])
    num2 = input()
    while not validate(num2):
        prompt(MESSAGES[lang]["invalid"])
        num2 = input()
    num2 = float(num2)

    while True:
        prompt(MESSAGES[lang]["operation"])
        operation = input()
        if operation in ("1", "2", "3", "4"):
            break
        prompt(MESSAGES[lang]["invalid"])

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
            prompt(MESSAGES[lang]["escapee"])

    prompt(f"The result is: {answer:.2f}")
while True:
    prompt(MESSAGES[lang]["calculate"])
    do_calc = input()
    if do_calc in ["y", "essyay"]:
        calculate()
    elif do_calc in ["n", "ennyay"]:
        prompt(MESSAGES[lang]["goodbye"])
        break
    else:
        prompt(MESSAGES[lang]["invalid"])