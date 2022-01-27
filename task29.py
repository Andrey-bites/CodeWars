import re

''' In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore '''


def alphanumeric(password):
    check = r'[\W\s]+'
    for i in password:
        if i == '_':
            return False
    if password == '':
        return False
    res = re.findall(check, password)
    if len(res) != 0:
        return False
    else:
        return True


print(alphanumeric('pas#@! sw_or d'))
print(alphanumeric('pasd'))
print(alphanumeric("hello world_"))
print(alphanumeric("T4_kW"))
print(alphanumeric(""))