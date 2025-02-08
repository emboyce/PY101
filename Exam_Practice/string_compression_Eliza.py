'''
    String Compression
'''

string = "aabcccccaaa"

def string_compression(string):
    chop_str = string
    cstring = ""
    while len(chop_str) > 0:
        start_char = chop_str[0]
        cstring = cstring + start_char
        char_count = count_first(chop_str, start_char)
        cstring += str(char_count)
        chop_str = chop_str[char_count:]
    if len(cstring) < len(string):
        return cstring
    else:
        return string
        

def count_first(chop_str, start_char):
    char_count = 0
    for char in chop_str:
        if char == start_char:
            char_count += 1
        else:
            break
    return char_count


print(string_compression(string))
print(string_compression("abcd"))
print(string_compression(""))
print(string_compression("aaajjj$aa"))