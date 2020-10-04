def binarySearch3(alist,first,last,item):
    """有序表的递归二分搜索,不使用切片"""
    if first > last:
        return False
    else:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        
        elif item > alist[mid]:
            return binarySearch3(alist, mid+1, last,item)
        
        else:
            return binarySearch3(alist, first, mid-1,item)

