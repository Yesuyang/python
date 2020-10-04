class HashTable:
    """散列表"""
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size     #存储键
        self.datas = [None] * size    #存储值

    def hashfunction(self, key):
        """散列函数"""
        return key % self.size

    def rehash(self, oldhash):
        """再序列函数"""
        return (oldhash + 1) % self.size  # 加1线性探测
    
    #
    def put(self, key, data):
        """添加或修改"""
        hashvalue = self.hashfunction(key)
        
        if self.keys[hashvalue] == None:        #空槽直接插入
            self.keys[hashvalue] = key
            self.datas[hashvalue] = data
        
        elif self.keys[hashvalue] == key:       #键相同则替换
            self.datas[hashvalue] = data
        
        else:                                   #非空槽寻找下一个空槽
            nextkey = self.rehash(hashvalue)
            while self.keys[nextkey] != None and self.datas[nextkey] != key:    #假设总可以分配一个槽
                nextkey = self.rehash(hashvalue)
                
            if self.keys[nextkey] == None:
                self.keys[nextkey] = key
                self.datas[nextkey] = data

            else:
                self.datas[nextkey] = data
                
    def __setitem__(self, key, data):
        """实现赋值操作"""
        self.put(key, data)
    
    #
    def get(self, key):
        """根据键查找值"""
        startkey = self.hashfunction(key)
        position = startkey
        data = None
        stop = False
        found = False
        while self.keys[position] != None and not found and not stop:
            if self.keys[position] == key:
                found = True
                data = self.datas[position]
            else:
                position = self.rehash(position)
                if position == startkey:
                    stop = True
        
        return data
    
    def __getitem__(self, key):
        """实现索引操作"""
        return self.get(key)
    
    #
    def __delitem__(self, key):
        """实现del dict[key]的删除操作"""
        self.put(key,data=None)
        self.keys[key] = None
        
    def __len__(self):
        """实现len(dict)操作"""
        count =0
        for i in range(self.size):
            if self.keys[i] != None:
                count += 1
        return count
    
    def __contains__(self, key):
        """实现in操作"""
        if self.get(key) == None:
            return False
        else:
            return True