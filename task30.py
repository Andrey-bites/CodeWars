""" Nesting Structure Comparison.
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] ). """


def same_structure_as(original, other):
    
    pass
            
                
                    

print(same_structure_as([[[], []]], [[[], []]]))
print(same_structure_as([1, 1, 1], [2, 2, 2]))
print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
print(same_structure_as([[1, 1], 1], [2, [2, 2]]))
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
print(same_structure_as([1, [1, 1]], [[2], 2]))
print(same_structure_as([[[], []]], [[1, 1]]))
