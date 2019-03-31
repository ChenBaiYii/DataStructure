#!/usr/bin/python3
# 列表队列  init_queue enqueue dequeue show_all

class Queue:
    def __init__(self):
        self.data = list()


    def is_empty(self):
        return len(self.data) < 1

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        p = self.data[0]
        del self.data[0]
        return p


    def show_all(self):
        for i in self.data:
            print(i, end='  ')
        print()



q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.show_all()
q.dequeue()
q.show_all()




