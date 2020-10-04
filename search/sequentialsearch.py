def sequentialSearch(alist, item):
    """无序表的顺序搜索"""
    pos = 0
    found = False
    
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    #找到则返回位置，未找到返回False
    if found :
        return pos
    else:
        return found