class Stack:
    """定义一个栈的类，列尾为栈顶"""
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []     #此处为布尔判断
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
