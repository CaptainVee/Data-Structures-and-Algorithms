

def merge_sort(lists):
    """
    Sorts a list in accending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge all the sorted sublist created in the previous step
    """
    
    if len(lists) <=1:
        return lists
    
    left_half, right_half = split(lists)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(lists):
    """
    Divide  the sorted list at midpoint into sublists
    Returns two sublists - left and right
    """
    midpoint = len(lists)//2
    left = lists[:midpoint]
    right = lists[midpoint:]
    
    return left, right


def merge(left, right):
    """
    Merge two list (arrays), sorting them in the process
    Returns a new merged list
    """
    
    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
            
        else:
            l.append(right[j])
            j += 1
            
    
    while i < len(left):
        l.append(left[i])
        i += 1
        
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l


def verify_sorted(lists):
    n = len(lists)
    
    if n == 0 or n == 1:
        return True 
    
    return lists[0] < lists[1] and verify_sorted(lists[:0])

        
alist = [9,8,7,6,5,0,3,2,4]

l = (merge_sort(alist))
print(verify_sorted(alist))
print(verify_sorted(l))
    
    
    
    
    
    
    
    
    
    
    
    
    









