#!/usr/bin/python3
# double link list  双向链表  前后添加删除， 首尾指针， 长度计数， show_all


class Node:
    def __init__(self, init_data, pre=None, next=None):
        self.data = init_data
        self.pre = pre
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None
        self.end = None
        self.length = 0 

    def is_empty(self):
        return self.length is 0

    def left_add(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.end = self.head
        else:
            p = Node(item, next=self.head)
            self.head.pre  = p
            self.head = p
        self.length += 1                

    def right_add(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            p = Node(item, next=Node, pre=self.end)
            self.end =  p
        self.length += 1

    def  right_pop(self):
        if self.is_empty():
            return None
        else:
            p = self.end
            self.end = p.pre
            self.length -= 1
            return p.data
    
    def left_pop(self):
        if self.is_empty():
            return None
        else:
            p = self.head
            self.head = p.next
            self.length -= 1
            return p.data


# 10 11 33

l = LinkList()
print("len", l.length)
l.left_add(11)
l.left_add(10)
print("len", l.length)
print('first ', l.head.data)
print('end', l.end.data)
print("end.pre", l.end.pre.data)

l.right_add(33)
print('end', l.end.data)
print("end.pre", l.end.pre.data)

result = l.right_pop()
print("right pop 33? ", result)

print('left pop 10? ', l.left_pop())
print('first ', l.head.data)










    





        
