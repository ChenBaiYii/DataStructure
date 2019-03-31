#!/usr/bin/python3
# 冒泡排序


def bubble(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


if __name__ == '__main__':
    a = [1, 4, 3, 8, 2, 99, 11]
    c = bubble(a)
    print(c)
