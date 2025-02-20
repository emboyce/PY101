def oddities(lst):
    odd_lst = lst
    return odd_lst[0::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

print("q9")
import random
def rand_ted():
    print(f"Teddy is {random.randint(0,100)} years old!")
rand_ted()

print("q10")
from datetime import date
year = date.today().year

age = int(input("What is your age? "))
retire = int(input("At what age would you like to retire? "))
retire_year = retire - age + year
print(f"It's {year}. You will retire in {retire_year}.")
print(f"You only have {retire - age} years of work to go!")