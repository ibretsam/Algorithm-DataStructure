def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    
    Takes O(n log n) time
    """
    
    if len(list) <= 1:
        return list
    
    left_list, right_list = split(list)
    left = merge_sort(left_list)
    right = merge_sort(right_list)
    
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists: left and right
    
    Takes overall O(log n) time
    """
    midpoint = len(list) // 2
    left_list = list[:midpoint]
    right_list = list[midpoint:]
    return left_list, right_list

def merge(left_list, right_list):
    """
    Merges two lists, sorting them in the process
    Returns a new merged list
    
    Runs in overall O(n) time
    """
    l = []
    i = 0
    j = 0
    
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            l.append(left_list[i])
            i += 1
        else:
            l.append(right_list[j])
            j += 1
            
    while i < len(left_list):
        l.append(left_list[i])
        i += 1
        
    while j < len(right_list):
        l.append(right_list[j])
        j += 1
        
    return l

def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [12, 25, 18, 97, 23, 75, 64, 36]
l = merge_sort(alist)

print(verify_sorted(alist))
print(verify_sorted(l))