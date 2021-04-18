

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
    
    lists = []
    i = 0
    j = 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    









