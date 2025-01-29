def utf16_value0(str1):
    char_list = []
    char_list += str1
    #str_ords = [ord(char) for char in char_list]
    return sum(str_ords)

def utf16_value(str1):
    str_ords = [ord(char) for char in str1]
    return sum(str_ords)



# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)