numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
numbers2 = numbers.copy()
numbers2.reverse()
print(numbers, numbers2)

# numbers3 = numbers.copy()
numbers3 = sorted(numbers, reverse = True)
print(numbers, numbers3)

numbers4 = list(reversed(numbers))
print(numbers, numbers4)

numbers5 = numbers[::-1]
print(numbers, numbers5)


numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(True) if number1 in numbers else print(False)
print(True) if number2 in numbers else print(False)

print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))

listy = [1, 2, 3, 4, 5]
listy.pop(2)
print(listy)

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

if isinstance(numbers, list): print(True)
if isinstance(table, dict): print(True)

title = "Flintstone Family Members"
print(title.center(40))

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
print(statement1.count("t"))
print(statement2.count("t"))

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print("Lily" in ages)

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

big_dict = ages | additional_ages
print(ages, big_dict)

ages.update(additional_ages)
print(ages)