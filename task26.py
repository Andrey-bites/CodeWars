''' Moving Zeros To The End '''


def move_zeros(array):
    res_list = []
    count = 0
    for elem in array:
        if elem != 0:
            res_list.append(elem)
        else:
            count += 1
    
    array = res_list
    zero_list = [0] * count
    array = array + zero_list
    

    return array


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
# print(move_zeros([0, 0]))
# print(move_zeros([0, 0]))
# print(move_zeros([0, 0]))
# print(move_zeros([0, 0]))
# print(move_zeros([0, 0]))
# print(move_zeros([0, 0]))
# print(move_zeros([0, 0]))
# print(move_zeros([0, 0]))