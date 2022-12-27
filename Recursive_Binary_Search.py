def recursive_binary_search(list, target):
    if len(list) == 0:
        return -1
    else:
        midpoint = len(list) // 2
        
        if list[midpoint] <= target:
            if list[midpoint] == target:
                return list[midpoint]
            elif list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1 :], target)
            else:
                return recursive_binary_search(list[:midpoint], target)
    
def verify(result):
    if result == -1:
        print("Target not found")
    else:
        print("Target found at position", result)
    
list = [1,2,3,4,5,6,7,8,9,10]
    
result = recursive_binary_search(list, 9)
verify(result)