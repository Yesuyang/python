def binarySearch2(alist, item):
    """有序表的递归二分搜索"""
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] > item:
                return binarySearch2(alist[:mid], item)
            else:
                return binarySearch2(alist[mid:], item)



