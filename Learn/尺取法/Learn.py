#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/28 16:14
# @File     : Learn.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def solve_loop(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return i, j


def solve_rule(arr, target):
    pass


if __name__ == '__main__':
    for _ in range(100):
        list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        t_num = list1[random.randint(0, len(list1))]
        if solve_loop(list2, t_num) != solve_rule(list3, t_num):
            print("target = ", t_num)
            print("list = ", list1)
            exit("Fuck!")
    print("Nice!")
