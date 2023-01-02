def quick_sort(values):
    if len(values) <= 1:
        return values
    pivot = values[0]
    less_than_pivot = []
    greater_than_pivot = []

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

list = [3, 9, 7, 2, 6, 10, 29, 74, 8, 12, 35, 100, 97]
print(quick_sort(list))