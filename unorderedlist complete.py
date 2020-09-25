class Node:
    """节点"""
    def __init__(self,initdata):
        self.data = initdata
        self.next = None            #头节点
        
    def getData(self):
        return self.data            #数据域
    
    def getNext(self):
        return self.next            #指针域
    
    def setData(self,newdata):
        self.data = newdata
        
    def setNext(self,newnext):
        self.next = newnext         #修改节点
        
    
class UnordereddList:
    """无序链表"""
    def __init__(self):
        self.head =None             #空表
        
    def isEmpty(self):
        """判空"""
        return self.head == None    #头指针指向None则为空表
    
    def length(self):
        """长度"""
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    #
    def insert(self,i,item):
        """插入"""
        current = self.head
        previous = None
        temp = Node(item)
        if i == 0:                                  #在头部插入，即add(item)
            temp.setNext(self.head)
            self.head = temp
            
        elif i >= self.length():                     #在尾部插入,即append(item)
            for count in range(self.length()-1):
                previous = current
                current = current.getNext()
            current.setNext(temp)
            temp.setNext(None)
            
        else:
            for count in range(i):
                previous = current
                current = current.getNext()
            previous.setNext(temp)
            temp.setNext(current)
        
    def append(self,item):
        """尾插"""
        current = self.head
        previous = None
        for count in range(self.length()-1):
            previous = current
            current = current.getNext()
        temp = Node(item)
        current.setNext(temp)
        temp.setNext(None)
        
    def add(self,item):
        """头插"""
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    #
    def getIndex(self,item):
        """优化查找方法，找到返回下标，未找到返回False"""
        current = self.head
        count = 0
        found = False  # 设置一个标志位
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                count +=1
                current = current.getNext()
        if found == True:
            return count
        else:
            return found
        
    def search(self,item):
        "查找是否存在"
        current = self.head
        found = False                 #设置一个标志位
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def index(self,item):
        """存在返回下标"""
        current = self.head
        count = 0
        while current != None:
            if current.getData() == item:
                break
            else:
                count += 1
                current = current.getNext()
        return count
        
   #
    def remove(self,item):
        """删除存在的元素"""
        current = self.head
        previous = None
        found = False
        
        if current.getData() == item:
            self.head = current.getNext()       #需要删除的元素在表头，则直接修改头指针
            
        else:
            while not found:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
                
            previous.setNext(current.getNext())
        
        
    def pop(self,i=-1):                             #此处-1仅用作标识，因为不能此处直接设置成默认值self.length()-1
        """按位删除,默认删除尾部元素"""
        current = self.head
        previous = None
        if i == -1:
            for count in range(self.length() - 1):
                previous = current
                current = current.getNext()
            previous.setNext(current.getNext())
        elif i ==0:
            self.head = current.getNext()
        else:
            for count in range(i):
                previous = current
                current = current.getNext()
            previous.setNext(current.getNext())
    

