def my_iter(limit):
    i = 0
    while i < limit:
        yield i + 1
        i += 1


it = my_iter(4)


print(next(it))
print(next(it))
print(next(it))
print(next(it))