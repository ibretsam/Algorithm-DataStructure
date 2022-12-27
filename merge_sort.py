def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """
    
    if len(list) <= 1:
        return list
    
    left_list, right_list = split(list)
    left = merge_sort(left_list)
    right = merge_sort(right_list)
    
    return merge(left, right)

def split(list):
    midpoint = len(list) // 2
    left_list = list[:midpoint]
    right_list = list[midpoint:]
    return left_list, right_list

def merge(left_list, right_list):
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

alist = [12, 25, 18, 97, 23, 75, 64, 36]
print(merge_sort(alist))