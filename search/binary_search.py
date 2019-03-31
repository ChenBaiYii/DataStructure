#!/usr/bin/python3
# 二分查找 要求序列必须是有序的

a = [1, 2, 3, 6, 9, 10, 33, 66]


def binary_search(sequence, item):
    if len(sequence) <= 0:
        return None
    begin = 0
    end = len(sequence) - 1

    while begin <= end:
        mid = (begin + end) // 2
        if sequence[mid] == item:
            return mid
        elif sequence[mid] > item:  # to left
            end = mid - 1
        else:
            begin = mid + 1
    return None


def test_binary_search():
    assert binary_search(a, 9) == 4
    assert binary_search(a, 66) == 7
    assert binary_search(a, 666) is None
