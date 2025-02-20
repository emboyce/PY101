def center_of(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2 
    if len(s) % 2 != 0:
        return s[middle]
    else:
        return s[middle - 1 : middle + 1]
    


print(center_of('I Love Python!!!') == "Py")    # True 
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True

print("Q12")

def negative(num):
    return -abs(num)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True