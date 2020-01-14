#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/12 下午5:43
# @Author   : alex
# @File     : code.py
# @Project  : Algorithm
# @Software : PyCharm


import copy, random


def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def generate_random_test(max_size: int, max_value: int):
    result = []
    size = random.randint(0, max_size + 1)
    for i in range(size):
        result.append(((int)(max_value + 1) * random.random()) - (int)(max_value * random.random()))
    return result


if __name__ == '__main__':
    test_num = 10000
    max_size = 100
    max_value = 100
    flag = True

    for i in range(test_num):
        list1 = generate_random_test(max_size, max_value)
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        bubble_sort(list2)
        list3.sort()
        if list2 != list3:
            flag = False
            print(list1)
            print(list2)
            print(list3)
            break

    print("Nice" if flag else "Fuck")
