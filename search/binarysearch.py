def binarySearch(alist, item):
    """有序表的二分搜索"""
    first = 0
    last = len(alist) - 1
    found = False
    
    while first <= last and not found:
        mid = (first+last) // 2
        if alist[mid] == item:
            found = True
        elif alist[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    
    if found:
        return mid
    else:
        return found
