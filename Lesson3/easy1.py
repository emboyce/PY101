famous_words = "seven years ago..."
the_score = "Four score and "
saying = the_score + famous_words
print(saying)
words = (the_score, famous_words)
saying = "".join(words)
print(saying)

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
munsters = munsters_description
print(munsters.casefold().capitalize())
print(munsters.capitalize())

munsters = "The Munsters are creepy and spooky."
print(munsters.swapcase())

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

dino_list = [str1, str2]
for str_ in dino_list:
    if not str_.find("Dino") == -1:
        print(str_.find("Dino"))

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
print(flintstones)

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])
print(flintstones)

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
print(advice.removesuffix("house training your pet dinosaur."))
print(advice.removesuffix("house"))
print(advice.rpartition("house")[0])

print(advice.replace("important", "urgent"))