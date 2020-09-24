from stack1 import Stack

def match(open,close):
    opens = '{[('
    closes = '}])'
    if opens.index(open) == closes.index(close):
        return True

def bracket_match(strings):
    s = Stack()
    tag = True  # 设置一个标志位
    index = 0
    while index < len(strings) and tag:
        string = strings[index]
        if string in '{[(':
            s.push(string)
        elif s.isEmpty():
            tag = False
        else:
            top=s.pop()
            if not match(top, string):
                tag = False
        index += 1
    
    if tag and s.isEmpty():
        return True
    else:
        return False


b = bracket_match('{([{}]([][]))}')
print(b)
