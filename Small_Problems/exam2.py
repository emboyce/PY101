str1 = "Hello, world!"
sub1 = str1[8:12]
print(sub1)
sub2 = str1[::-1]
print(sub2)
sub3 = str1[::2]
print(sub3)

mashup = "thIs is How we type careLEssly"
cleaned = mashup.capitalize()
print(cleaned)

name = "Abraham Lincoln"
print(f"{name} was a Pres")

stuff = 'tHIS iS bACKWARDS'
str1 = stuff.swapcase()
str2 = stuff.upper()
str3 = stuff.lower()
print(stuff)
print(str1)
print(str2)
print(str3)

s1 = "Hello"
# print(s1.isalpha())
s2 = "Hello World"
# print(s2.isalpha())
s3 = "Hello!"
# print(s3.isalpha())
s4 = "Hello123"
# print(s4.isalpha())
s5 = ""
# print(s5.isalpha())
s6 = "こんにちは"
print(s6.isalpha())
s7 = "HelloWorld"
print(s7.isalpha())
words = ["apple", "banana", "cherry"]
print(all(word.isalpha() for word in words))

print('"'.isascii())

string1 = "HelloWorld"
string2 = "12345"
string3 = "Hello World"

result1 = string1.isalpha()
result2 = string2.isalpha()
result3 = string3.isalpha()

print("Is '{}' alphabetic?".format(string1), result1)
print("Is '{}' alphabetic?".format(string2), result2)
print("Is '{}' alphabetic?".format(string3), result3)

s1 = "123abc"
print(s1.isdigit())
s2 = "123$%^"
print(s2.isdigit())
s3 = ""
print(s3.isdigit())
s4 = "1234505"
print(s4.isdigit())

print("Hello World".isalnum())
print("Hello@World".isalnum())
print("".isalnum())
print("Hello123".isalnum())

def punctuation_type(str):
    if str == str.upper():
        print('This is all caps')
    elif str == str.lower():
        print('This is all lowercase')
    else:
        print('Neither')

str1 = 'HELLO'
str2 = 'yolo'
str3 = 'My Name Is: '

punctuation_type(str1)
punctuation_type(str2)
punctuation_type(str3)

sentence = "Hello     World!   How are you?   "
sen2 = sentence.split()
print(sen2)

str1 = "    "
str2 = "  Hello   "
str3 = "Hello World"

print(str1.isspace())
print(str2.isspace())
print(str3.isspace())

sentence = "Hello     World!???   How are you?   "
print(sentence.split("?"))
word_count = sum(1 for word in sentence.split("?") if not word.isspace())
print("Number of words in the sentence:", word_count)

s = "   Hello, World!   "
print(s.strip())
print(s.strip(" !"))

s = 'impatient'
print(s.rstrip('tp'))
print(s.rstrip('p'))

s = "www.example.com"
print(s.lstrip('wcmo.'))

s = "Hello, World!"
print(s.replace("Hello", "Hi"))
print(s.replace(" ", "0"))

sentence = "This is a sample sentence."
words = sentence.split()
print(words)

csv_data = "John,Doe,30,New York"
fields = csv_data.split(",")
print(fields)

sentence = "This is a sample sentence."
words = sentence.split(maxsplit=2)
print(words)

str1 = "hello world"
str2 = str1.capitalize()
print("Original string:", str1)
print("Capitalized string:", str2)

truthy_values = [1, 2, 3, "hello", [1, 2, 3], {"a": 1}, True, 0, "", [], {}, None, False]


print("Values: ")
for value in truthy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")

x = 5
y = 10
z = 15

print(x > 0 and y < 20)
print(not x == y)
print(x < y and y < z)
print(x > y or y > z)
print(not (x > y))

a = 10
b = 20

print("end")
print(a < b < 30)
print(a > b or b == 20)
print(None or 3)
print(3 or None)
print(None and 3)

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)

print("new")
my_list = [1, 2, 3.0, 4, 5]
print(3 in my_list)
print(3 is 3.0)
print(6 not in my_list)

num = 12

if num / 3 < 3 and num > 10:
    print("Hello")
elif num >= 8 and num < 6 or num > 4 and num < 16:
    print("Hello 2")
elif num % 4 == 0 or num < 7 and num < 10:
    print("Hello 3")
else:
    print("Buy")

var = 10
def access():
    print(var)
access()

print("end")
def function1():
  p = 10

  def function2():
      k = 20
      print(p)

  function2()
  print(p)

function1()
print(p)
print(k)