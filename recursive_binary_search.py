

def recursive_binary_search(lists, target):
    if len(lists) == 0:
        return False
    else:
        midpoint = (len(lists))//2
        
        if lists[midpoint] == target:
            return True
        elif lists[midpoint] < target:
            return recursive_binary_search(lists[midpoint+1 :], target)
        else:
            return recursive_binary_search(lists[: midpoint], target)
        
def verify(result):
    print('Target found', result)
    
numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 1)
verify(result)
            
        
            