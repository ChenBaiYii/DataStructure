#!/usr/bin/python3
# 字典

"""
ADT:
    private:
        _iter_slot  返回所有非空槽的迭代器
        __setitem__
        __getitem__

    public:
        items  返回所以非空槽key, value组成的迭代器
        keys  返回所以非空槽key组成的迭代器
        values  返回所以非空槽value组成的迭代器
"""

from hashtable import HashTable


class Dictionary(HashTable):

    def _iter_slot(self):
        """ 返回所有非空槽的迭代器 """
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield slot

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, item):
        if item not in self:
            raise KeyError('不存在的key')
        return self.get(item)

    def items(self):
        """ 返回所以非空槽key, value组成的迭代器 """
        for i in self._iter_slot():
            yield (i.key, i.value)

    def keys(self):
        """ 返回所以非空槽key组成的迭代器 """
        for i in self._iter_slot():
            yield i.key

    def values(self):
        """ 返回所以非空槽value组成的迭代器 """
        for v in self._iter_slot():
            yield v.value


if __name__ == '__main__':
    d = Dictionary()
    d['b'] = 1
    d['a'] = 0
    d.add('item', 'ok')

    f = d.items()
    for a in f:
        print(a)
