def multisum0(max_num):
    num_list = []
    for num in range(1, max_num + 1):
        if num in num_list:
            continue
        else:
            if num % 3 == 0:
                num_list.append(num)
            elif num % 5 == 0:
                num_list.append(num)
    
    return sum(num_list)

def multisum1(max_num):
    num_list = []
    for num in range(1, max_num + 1):
            if num % 3 == 0:
                num_list.append(num)
            elif num % 5 == 0:
                num_list.append(num)
    
    return sum(num_list)

def multisum(max_num):
    num_list = [num for num in range(1, max_num + 1) if num % 3 == 0 or num % 5 ==0]
    return sum(num_list)

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

