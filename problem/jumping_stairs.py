#!/usr/bin/python3
# 跳台阶 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法


fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
s = fib(10)
print(s)
