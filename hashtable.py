#!/usr/bin/python3
# hashtable 

"""
ADT:
    slot
    init
    private:
        _load_factory  计算负载因子
        _rehash  重新hash
        _hash  hash计算index
        _find_key
        _check_can_insert
        _find_slot_for_insert
    public:
        get
        add
        remove
reindex: (index * 5 + 1) % _len
factory: table_real_length / table_all_length
"""


class Slot:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    UNUSED = None  # 从未被使用过
    EMPTY = Slot(None, None)  # 使用过却被删除过

    def __init__(self):
        self._table = [HashTable.UNUSED] * 8  # 保持 2 * i 的次方的
        self.length = 0

    def __len__(self):
        return self.length  # 表的实际长度

    @property
    def _load_factory(self):
        # 负载因子超过0.8重新分配
        return self.length / float(len(self._table))

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        """ 寻找key元素返回其index, 否则为None """
        index = self._hash(key)  # 计算出索引
        _len = len(self._table)  # 表的总长度

        while self._table[index] is not HashTable.UNUSED:  # 使用过才能找到元素...
            if self._table[index] is HashTable.EMPTY:  # 被删除了
                index = (index * 5 + 1) % _len  # 重新计算位置
                continue  # 再次查找
            elif self._table[index].key == key:  # ok 返回索引
                return index
            else:  # 找不到哦
                index = (index * 5 + 1) % _len  # 重新计算位置
        return None

    def __contains__(self, key):
        """ 使用_find_key查找哈希表是否包含指定key """
        index = self._find_key(key)
        return index

    def _check_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or
                self._table[index] is HashTable.UNUSED)

    def _find_slot_for_insert(self, key):
        """ 寻找可以插入的槽位置 """
        index = self._hash(key)
        _len = len(self._table)
        while not self._check_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def _rehash(self):
        """ 重新hash """
        old_table = self._table
        new_size = len(self._table) * 2  # 扩展2倍
        self._table = [HashTable.UNUSED] * new_size
        self.length = 0

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:  # 有数据
                index = self._find_slot_for_insert(slot.key)  # 寻找可插入的槽
                self._table[index] = slot
                self.length += 1

    def add(self, key, value):
        """ 添加元素到哈希表, 如果存在则覆盖 """
        if key in self:  # call __contains__
            index = self._find_key(key)  # 既然存在则寻找其位置
            self._table[index].value = value  # 重新赋值
        else:  # 新元素
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)  # ok
            self.length += 1
            if self._load_factory >= 0.8:
                self._rehash()  # 重新hash
            return True

    def get(self, key, default=None):
        """ 获取key的value, 没有则返回None """
        index = self._find_key(key)
        if index is None:
            print("in default")
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        """ 移除一个key及其value """
        index = self._find_key(key)
        if not index:
            raise KeyError("key不存在")
        value = self._table[index].value

        self._table[index] = HashTable.EMPTY
        self.length -= 1
        return value

    def __iter__(self):
        for s in self._table:
            if s not in (HashTable.UNUSED, HashTable.EMPTY):
                yield s.key


if __name__ == '__main__':
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)

    print('len ', len(h))
    print('get a : ', h.get('a'))
    print('get b : ', h.get('b'))
    print('get c : ', h.get('c'))
