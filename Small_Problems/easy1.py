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
    while not length is float:
        length = float(input("Enter rooom length in metres: "))
    width = float(input("Enter room width in metres: "))
    area_m = length * width
    area_ft = area_m * 10.7639
    print(f"Area is {area_m} sq m, or {area_ft} sq ft.")

how_big()
