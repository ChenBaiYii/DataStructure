#!/usr/bin/python3f
# 二叉树


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BinaryTree:
    buffer = []

    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            self.buffer.append(self.root)
        else:
            while True:
                point = self.buffer[0]
                if point.left is None:
                    point.left = node
                    self.buffer.append(point.left)
                    return
                elif point.right is None:
                    point.right = node
                    self.buffer.pop(0)
                    self.buffer.append(point.right)
                    return

    def preface(self, subtree):
        if subtree is None:
            return None
        print(subtree, end=" ")
        self.preface(subtree.left)
        self.preface(subtree.right)

    def middle(self, subtree):
        if subtree is None:
            return None
        self.middle(subtree.left)
        print(subtree, end=" ")
        self.middle(subtree.right)

    def post_order(self, subtree):
        if subtree is None:
            return None
        self.post_order(subtree.left)
        self.post_order(subtree.right)
        print(subtree, end=" ")

    def reverse_tree(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse_tree(subtree.left)
            self.reverse_tree(subtree.right)


if __name__ == '__main__':
    t = BinaryTree()
    [t.add(x) for x in range(1, 6)]

    print(t.root.right)

    print("preface")
    t.preface(t.root)
    print("middle")
    t.middle(t.root)
    print('post order')
    t.post_order(t.root)
    print(t.root.left)
    print("reversed")
    t.reverse_tree(t.root)
    t.preface(t.root)
