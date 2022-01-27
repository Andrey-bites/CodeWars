""" This time no story, no theory. The examples below show you how to write function accum:
Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z."""



def accum(s):
    stoper = len(s)
    d = []
    res = []
    while stoper > 0:
        starter = 1
        for i in s:
            d.append(i * starter)
            starter += 1
            stoper -= 1
    for k in d:
        res.append(k.capitalize())

    res = '-'.join(res)
    
    return res



print(accum('ZpglnRxqenU'))
