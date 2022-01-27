def add_binary(a, b):
    sum = (a + b)
    binary = ''

    while sum > 0:
        binary = str(sum % 2) + binary
        sum = sum // 2
 
    return binary

print(add_binary(4,5))
print(add_binary(0,1))
print(add_binary(1,0))
print(add_binary(2,2))
print(add_binary(51,12))
