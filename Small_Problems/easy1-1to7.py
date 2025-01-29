def maybe_odd(num):
    return (False if num % 2 == 0 else True)

print(maybe_odd(-4))

for num in range(1, 100):
    if maybe_odd(num): print(num)

for num in range(1, 100, 2):
    print(num)

for num in range(2, 99, 2):
    print(num)

def how_big():
    length, width = "", ""
    length = float(input("Enter rooom length in metres: "))
    width = float(input("Enter room width in metres: "))
    area_m = length * width
    area_ft = area_m * 10.7639
    print(f"Area is {area_m} sq m, or {area_ft} sq ft.")

# how_big()

def tip_calc():
    bill = float(input("What is the bill? "))
    rate = float(input("What percent do you wan to tip? "))
    print(f"The tip is ${(bill*rate/100):.2f} and the total is ${(bill*(rate + 1)/100):.2f}")

# tip_calc()

def summer(num, sp):
    if sp == "s":
        sums = sum([i for i in range(1, num + 1)])
        print(f"The sum of the integers between 1 and {num} is {sums}.")
    elif sp == "p":
        prod = 1
        count = num
        while count > 0:
            prod *= count
            count -= 1
        print(f"The product of the integers between 1 and {num} is {prod}.")

def get_inputs():
    inputs = []
    inputs.append(int(input("Enter an integer greater than 0: ")))
    inputs.append(input("Enter 's' to sum or 'p' for product: "))
    return inputs[0], inputs[1]

# x, y = get_inputs()
# summer(x, y)

# summer(*get_inputs())

def str_sort(str1, str2):
    final_str = ""
    len1, len2 = len(str1), len(str2)
    if len1 > len2:
        final_str = str_add(str2, str1)
    elif len1 < len2:
        final_str = str_add(str1, str2)
    else:
        print("Not looping")
    
    return final_str

def str_add(short_str, long_str):
    return (short_str + long_str + short_str)

print(str_sort("hi", "world"))
# These examples should all print True
print(str_sort('abc', 'defgh') == "abcdefghabc")
print(str_sort('abcde', 'fgh') == "fghabcdefgh")
print(str_sort('', 'xyz') == "xyz")

