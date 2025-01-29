import json
with open('mortgage_prompts.json', 'r') as file:
    MSG = json.load(file)

def prompt(message):
    print(f"==> {message}")

prompt(MSG['welcome'])

def validate(input_num):
    while True:
        try:
            if float(input_num) >= 0:
                return True
            else:
                return False
        except Exception:
            return False

while True:
    prompt(MSG['loan_amount'])
    loan_amount = input()
    if not validate(loan_amount):
        prompt(MSG['invalid'])
    else:
        break
loan_amount = float(loan_amount)

while True:
    prompt(MSG['APR'])
    annual_percentage_rate = input()
    if not validate(annual_percentage_rate):
        prompt(MSG['invalid'])
    else:
        break

if annual_percentage_rate == 0:
    monthly_rate == 0
else:
    monthly_rate = (float(annual_percentage_rate) / 100) / 12

while True:
    prompt(MSG['loan_duration'])
    loan_duration = input()
    if not validate(loan_duration):
        prompt(MSG['invalid'])
    else:
        break

loan_months = float(loan_duration)*12

if loan_amount == 0:
    prompt(MSG["free_house"])
elif loan_months == 0:
    prompt(MSG["zero_time"])
elif monthly_rate == 0:
    prompt(MSG["principal_only"])
    print(f"${loan_amount/loan_months:.2f}")
else:
    monthly_payment = loan_amount * (monthly_rate / (1 - ((1 + monthly_rate) ** (-loan_months))))
    prompt(MSG["std_payment"])
    print(f"${monthly_payment:.2f}")
