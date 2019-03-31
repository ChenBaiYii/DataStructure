#!/usr/bin/python3
# 二分递归查找 要求序列必须是有序的

a = [1, 2, 3, 6, 9, 10, 33, 66]


def binary_search_recursive(sequence, item, begin, end):
    if begin >= end:
        return None
    mid = (begin + end) // 2
    if sequence[mid] < item:  # to right
        return binary_search_recursive(sequence, item, mid + 1, end)
    elif sequence[mid] == item:  # find it
        return mid
    else:  # to left
        return binary_search_recursive(sequence, item, begin, mid - 1)


def test():
    assert binary_search_recursive(a, 9, 0, len(a)) == 4
    assert binary_search_recursive(a, 66, 0, len(a)) == 7
    assert binary_search_recursive(a, 666, 0, len(a)) is None
