from linked_list import LinkedList

def merge_sort(linked_list):
    if linked_list.size() == 1 or linked_list.is_empty():
        return linked_list
    else:
        left_half, right_half = split(linked_list)
        left = merge_sort(left_half)
        right = merge_sort(right_half)
        return merge(left, right)
    
def split(linked_list):
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        
        print(left_half)
        print(right_half)
        return left_half, right_half
    
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid - 1)
        
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        print(left_half)
        print(right_half)
        return left_half, right_half
    
def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    """
    
    l = LinkedList()
    i = 0
    j = 0
    
    l.add(0)
    
    while i < left.size() and j < right.size():
        if left.node_at_index(i).data < right.node_at_index(j).data:
            l.insert(left.node_at_index(i).data, l.size())
            i += 1
        else:
            l.insert(right.node_at_index(j).data, l.size())
            
    while i < left.size():
        l.insert(left.node_at_index(i).data, l.size())
        i += 1
        
    while j < right.size():
        l.insert(right.node_at_index(j).data, l.size())
        j += 1
        
    return l

l = LinkedList()
l.add(25)
l.add(37)
l.add(15)
l.add(17)
l.add(9)
l.add(11)
l.add(3)

print(merge_sort(l))