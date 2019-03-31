#!/usr/bin/python3
# 元组

"""
ADT:
    private:
        __and__  交集
        __sub__  差集
        __or__  并集

    public:
        add
        remove
"""

from hashtable import HashTable


class Sets(HashTable):

    def add(self, key):
        return super(Sets, self).add(key, True)

    def remove(self, key):
        return super(Sets, self).remove(key)

    def __and__(self, other_set):
        """ 取 a b 交集 """
        new_set = Sets()
        for element_a in self:
            if element_a in other_set:
                new_set.add(element_a)
        return new_set

    def __sub__(self, other_set):
        new_set = Sets()
        for element_a in self:
            if element_a not in other_set:
                new_set.add(element_a)
        return new_set


if __name__ == '__main__':
    s = Sets()
