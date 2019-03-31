#!/usr/bin/python3
# 共享属性实现单例模式

"""
创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法
"""


class Singleton:
    _sates = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Singleton, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._sates
        return ob


class MyClass(Singleton):
    a = 1


a = MyClass()
b = MyClass()

print(id(a))
print(id(b))
