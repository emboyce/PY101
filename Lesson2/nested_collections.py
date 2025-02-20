lst1 = [1, [2, 3], 4]

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

dict1 = {'first': [1, 2, [3]]}

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}

lst1[1][1] = 4
lst2[2] = 4
dict1['first'][2][0] = 4
dict2['a']['a'][2] = 4

print(lst1, lst2, dict1, dict2, sep="\n")

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for index in range(0, len(munsters)):
    name = list(munsters.keys())[index]
    age = munsters[name]['age']
    gender = munsters[name]['gender']
    print(f"{name} is a {age}-year old {gender}.")

for name, info in munsters.items():
    print(f"{name} is a {info["age"]}-year-old {info["gender"]}.")
