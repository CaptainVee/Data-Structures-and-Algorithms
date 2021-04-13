
def linear_search(lists, target):
    '''
     returns the index position of the target value if found, else returns none
    '''
    
    for i in range(0, len(lists)): #loop through 0 to the length of the list
        if lists[i] == target:# if its the target 
            return i       #return it else contine
    return None     #else return None


def verify(index):
    if index is not None:
        print('\nTarget found at index', index)
    else:
        print('Target not found')
        
numbers = [1,2,3,4,5,6,7,8,9,10]
result =linear_search(numbers, 2)
verify(result)




