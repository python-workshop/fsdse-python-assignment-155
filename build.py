def sort(data):
    if data is None:
        raise TypeError('data cannot be None')
    return _sort(data)


def _sort(data):
    if len(data) < 2:
        return data
    equal = []
    left = []
    right = []
    pivot_index = len(data) // 2
    pivot_value = data[pivot_index]
    # Build the left and right partitions
    for item in data:
        if item == pivot_value:
            equal.append(item)
        elif item < pivot_value:
            left.append(item)
        else:
            right.append(item)
    # Recursively apply quick_sort
    left_ = _sort(left)
    right_ = _sort(right)
    return left_ + equal + right_