from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains
    
    Returns a sorted linked list
    """
    if linked_list.size() == 1 or linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)
    
def split(linked_list):
    """
    
    """
    if linked_list == None or linked_list.is_empty():
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid - 1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        return left_half, right_half
    
    
def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    """
    
    merged = LinkedList()
    merged.add(0)

    left_head = left.head
    right_head = right.head
    
    current = merged.head
    
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            if left_head.data < right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node
        
    head = merged.head.next_node
    merged.head = head
    
    return merged
    

l = LinkedList()
l.add(25)
l.add(37)
l.add(15)
l.add(17)
l.add(9)
l.add(11)
l.add(3)

print("Original linked list:")
print(l)

print("Sorted linked list:")
print(merge_sort(l))