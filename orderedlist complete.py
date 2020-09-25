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
        
    
class OrdereddList:
    """有序链表,默认从小到大"""
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
    def add(self,item):
        """添加元素"""
        current = self.head
        previous = None
        stop = True
        temp = Node(item)
        if self.head == None:                 #在头部添加元素
            temp.setNext(self.head)
            self.head = temp
            
        else:
            while current != None and stop:
                if current.getData() > item:
                    stop = False
                else:
                    previous = current
                    current = current.getNext()
            previous.setNext(temp)
            temp.setNext(current)
   
    #
    def getIndex(self,item):
        """优化查找方法，找到返回下标，未找到返回False"""
        current = self.head
        count = 0
        found = False  # 设置一个标志位
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                count +=1
                current = current.getNext()
        if found and stop == True:
            return count
        else:
            return False
        
    def search(self,item):
        "查找是否存在"
        current = self.head
        found = False                 #设置两个标志位
        stop = True
        while current != None and not found and stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = False
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
    

mylist=OrdereddList()
for i in range(10):
    mylist.add(i)
print(mylist.length())