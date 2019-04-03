#!/usr/bin/python3
# link list


class Node:
    def __init__(self, initdata, next=None):
        self.data = initdata
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length is 0

    def right_add(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            position = self.head
            while position.next is not None:
                position = position.next
            position = Node(item)
            self.length += 1
                
            self.head.next = Node(item)
        self.length += 1

    def left_add(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            self.head = Node(item, self.head)
        self.length += 1


    def left_pop(self):
        item = self.head
        self.head = item.next
        self.length -= 1
        return item.data


# 15 -> 10 -> 111 ->None
l = LinkList()
print(l.is_empty())
# l.right_add(11)
l.left_add(10)
l.left_add(15)

print(l.head.data)
print(l.head.next.data)
print('len', l.length)
print('left pop', l.left_pop())
print('len', l.length)
print(l.head.data)

# 10 -> 111 ->None
l.right_add(111)
print('len', l.length)
print(l.head.next.data)
