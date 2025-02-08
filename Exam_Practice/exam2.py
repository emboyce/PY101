rat = "test"

def function1():
  x = 10

  def function2():
      y = 20
      print(x)

      def function3():
          print(rat)

      function3()

  function2()
  print(x)

function1()
# print(x)
# print(y)

print("new")
var = 10

def function1():
    var = 20
    print(var)

function1()

try:
    print(var)
except NameError:
    print("Error occurred")

def function2():
    var += 5
    print(var)

try:
    function2()
except UnboundLocalError:
    print("Error occurred")

def function3():
    global var
    var += 5
    print(var)

function3()
print(var)

try:
    print(cat)
except NameError as e:
    print(f"Error occurred: {e}")

def assign():
    ham = 20
    print(ham)

assign()
print("new")
print(range(0,10))
print(len(range(5, 15)))
# print(my_range[1])
print(str(range(3, 7)))
print(list(range(12, 8, -1)))
print(list(range(5, 5, 1)))
print(5 in range(5))
print(5 not in range(5, 10))

example = range(0)
if example:
    print(list(example))
else:
    print(example)

def number_range(number):
    match number:
        case n if n < 0:
            print(f'{number} is less than 0')
        case n if n <= 50:
            print(f'{number} is between 0 and 50')
        case n if n <= 100:
            print(f'{number} is between 51 and 100')
        case final:
            print(f'{number} is greater than 100')
number_range(0)
number_range(25)

lst_one = [0, 1, 2, 3]
lst_two = lst_one.append(4)
if lst_two:
    print(lst_one)
else:
    print(lst_one)

my_list = [1, 2, 3, 4, 5]
ele = my_list.pop()
print("Popped element:", ele)
print("List after popping:", my_list)
ele1 = my_list.pop(1)
print("Popped element at index 1:", ele1)
print("Modified list after popping at index 1:", my_list)

elements = [0, 1 , 2, "Dima"]
print(elements.reverse())
print(elements)

ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

def get_val_of_dima(info):
    try:
        info['dimo']
        return info['dimo']
    except KeyError:
        return "Typo"

print(get_val_of_dima(ages))

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)
for key in keys:
    print(key)

my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)
for value in values:
    print(value)

my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)
for key, value in items:
    print( key, value)