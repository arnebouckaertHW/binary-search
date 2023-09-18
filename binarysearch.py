def search(a, first: int, target: int):
    """Searches part of a sorted list for a specified target starting at a[first]

    Args:
        a (int): the list to search
        first (int): the list index at which the search will start
        target (int): the element to search for

    Returns:
        int: If target appears in the list, index of the element that contains target; else -1
    """
    # set boolean variable found to false
    found = False

    # set int variable size to the list length - first
    size = len(a) - first
    
    # set int variable middle to the first + size / 2
    middle = int(first + size / 2)

    # if there are no more elements to search, return -1
    if size <= 0:
        return -1
    else:
        # while there are more elements to search and the target has not been found
        while size > 0 and not found:
            # if the middle element is the target, target is found
            if a[middle] == target:
                found = True
            # else if the middle element is greater than the target
            elif a[middle] > target:
                size = int(size / 2)
            # else if the middle element is less than the target
            else:
                first = middle + 1
                size = int((size - 1) / 2)

            # recompute middle
            middle = int(first + size / 2)

    # if the target was found, return the index of the target
    if found:
        return middle
    # else return -1    
    else:
        return -1