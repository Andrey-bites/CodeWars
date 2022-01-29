""" Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'
# namelist([ {'name': 'Bart'} ])
# returns 'Bart'
namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'. """


def namelist(names):
    lst = []
    for i in names:
        if isinstance(i, dict):
            lst.append(i.get('name'))
    if len(lst) >= 2:
        lst.extend('&')
        lst[-1], lst[-2] = lst[-2], lst[-1]
    final_str = ' '.join(lst)
            
    return final_str

print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([ {'name': 'Bart'} ]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
