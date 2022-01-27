

def sort_by_length(arr):
    last_item = len(arr) - 1
    for x in range(0, last_item):
        for y in range(0, last_item - x):
            if len(arr[y]) > len(arr[y + 1]):
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
    return arr


# print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))
print(sort_by_length(['beg', 'i', 'life', 'to']))
