
def binary_search(lists, target):
    first = 0
    last = len(lists) - 1
    
    while first <= last:
        midpoint = (first + last)//2
        if lists[midpoint] == target:
            return midpoint
        elif lists[midpoint] < target:
            
            first = midpoint + 1  
        else:
            last = midpoint - 1 

    return None


def verify(index):
    if index is not None:
        print('\nTarget found at index', index)
    else:
        print('Target not found')
        
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 6)
verify(result)
