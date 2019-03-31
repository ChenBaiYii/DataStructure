#!/usr/bin/python3

a = [1, 2, 3, 6, 9, 10, 33, 66]


def liner_search(sequence, item):
    """ 查找序列中是否含有指定元素， 返回其index， 否则返回None """
    for index, value in enumerate(sequence):
        if value == item:
            return index
    return None


position = liner_search(a, 9)
print("liner search position: {}".format(position))


# 递归查找

def recursive_search(sequence, item):
    if len(sequence) == 0:
        return None
    index = len(sequence) - 1
    if sequence[index] == item:
        return index
    return recursive_search(sequence[0:index], item)


position = recursive_search(a, 9)

print("recursive search position: {}".format(position))
