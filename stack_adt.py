#!/usr/bin/python3
# 列表栈 init_stack push pop show_all is_empty get


class Stack:
    def __init__(self):
        self.data = list()

    
    def is_empty(self):
        return len(self.data) < 1

    
    def push(self, item):
        self.data.append(item)


    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def get(self):
        p = self.data[-1]
        return p

    def shwo_all(self):
        for i in self.data:
            print(i, end='  ')
        print()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print("get ", s.get())

s.shwo_all()
print('pop ', s.pop())
s.shwo_all()



        
    


    














