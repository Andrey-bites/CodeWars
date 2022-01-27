import re

''' Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string. '''
""" String incrementer """


def increment_string(strng):

    if len(strng) == 0:
        return '1'
    for i in strng:
        if strng[-1].isdigit():
            tpl1 = r'[\d]+'
            tpl2 = r'[a-zA-Z\W]+'
        else:
            return strng + '1'

    lst = re.findall(tpl1, strng)
    lenght_lst = len(lst[0])
    lst_int = int(lst[0]) + 1
    lst_str = str(lst_int)
    final_str = lst_str.zfill(lenght_lst)

    lst2 = re.findall(tpl2, strng)
    final_str2 = ''.join(lst2)

    strng = final_str2 + final_str

    return strng


print(increment_string("foo"))
print(increment_string("foobar001"))
print(increment_string("foobar1"))
print(increment_string("foobar00"))
print(increment_string("foobar99"))
print(increment_string("foobar099"))
print(increment_string(""))
