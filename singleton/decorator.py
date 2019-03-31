#!/usr/bin/python3
# 装饰器实现单例模式


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class MyClass:
    a = 1


a = MyClass()
b = MyClass()

assert id(a) == id(b)
