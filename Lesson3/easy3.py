numbers = [1, 2, 3, 4]

while numbers:
    numbers.pop()

print(numbers)

numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)

print([1, 2, 3] + [4, 5])

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
    
def is_colour_valid(colour):
    return colour == "blue" or colour == "green"

def is_colour_valid1(colour):
    return colour in ["blue", "green"]

print(is_colour_valid1("blue"))
print(is_colour_valid1("red"))