print("q1")

def repeat(str_, num):
    for _ in range(0, num):
        print(str_)

repeat('Hello', 3)

print("q2")

def crunch0(str_):
    new_str = ""
    for char in str_:
        if len(new_str) == 0:
            new_str += char
        else:
            if new_str[-1] != char:
                new_str += char
    return new_str

def crunch(str_):
    if str_ == "":
        return str_
    new_list = [str_[0]]
    new_ = [new_list.append(char) for char in str_ if new_list[-1] != char]
    return "".join(new_list)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

print("q3")

def print_in_box(str_):
    len_ = len(str_)
    top_border = "+-" + "-"*len_ + "-+"
    first_last = "| " + " "*len_ + " |"
    print(top_border)
    print(first_last)
    print("| " + str_ + " |")
    print(first_last)
    print(top_border)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')

print("q4")

def stringy(num):
    str_ = "1"
    while len(str_) < num:
        str_ += ("1" if len(str_) % 2 == 0 else "0")
    return str_

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

print("q5")

def triangle(num):
    for idx in range(num - 1, -1, -1):
        print(f'{"o"*idx}{"*" * (num-idx)}')

triangle(5)

print("skip q6")
print("q7")

def twice(num):
    mid = len(str(num)) // 2
    left = str(num)[0:mid]
    right = str(num)[mid:]
    return num if left == right else num * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True

print("q8")

def get_grade(n1, n2, n3):
    avg = (n1 + n2 + n3) / 3
    gradebook = {
        90: "A",
        80: "B",
        70: "C",
        60: "D",
        0: "F",
    }
    for key in gradebook.keys():
        if avg >= key:
            return gradebook[key]

print(get_grade(0, 0, 180))     # True
print(get_grade(50, 50, 95) == "D")      # True

print("q9")

def clean_up(str_):
    alpha_lst = [char if char.isalpha() else " " for char in str_]
    alpha_str = "".join(alpha_lst)
    changed = True
    while changed:
        og_len = len(alpha_str)
        alpha_str = alpha_str.replace("  ", " ")
        new_len = len(alpha_str)
        if og_len == new_len:
            changed = False
    print(alpha_str)
    return alpha_str
print(clean_up("-    --what's my +*& line?") == " what s my line ")
# True

print("q10")

'''
1 21 st
2 22 nd
3 23 rd
4 5 6 7 8 9 10 100 th

'''

def yearify(cent):
    last1 = cent[-1]
    last2 = cent[-2:]
    century = ""
    if last1 == "1" and last2 != "11":
        century = cent + "st"
    elif last1 == "2" and last2 != "12":
        century = cent + "nd"
    elif last1 == "3" and last2 != "13":
        century = cent + "rd"
    else:
        century = cent + "th"
    return century


def century(year):
    decade = str(year)[-2::]
    cent = str(year)[:-2]
    if year <= 100:
        return "1st"
    elif decade == "00":
        return yearify(cent)
    else:
        return yearify(str(int(cent) + 1))


print(century(2001))
    

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True