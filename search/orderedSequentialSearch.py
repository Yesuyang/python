def orderedSequentialSearch(alist, item):
    """有序表的顺序搜索"""
    pos = 0
    found = False
    stop = False
    
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos = pos + 1
    
    if found:
        return pos
    else:
        return found
