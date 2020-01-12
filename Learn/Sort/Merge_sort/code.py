# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ----------------------------------------------
# >>> File Name : code.py
# >>> Created Time: 2020年01月12日 星期日 22时25分25秒
# !/usr/bin/python
# -*- coding:utf-8 -*-
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


import sys
import copy
import random


def merge_sort(arr: list):
    mergesort(arr, 0, len(arr) - 1)


def mergesort(arr: list, left: int, right: int):
    if left == right:
        return
    mid = left + ((right - left) >> 1)
    mergesort(arr, left, mid)
    mergesort(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int):
    help_list = []
    i, p1, p2 = 0, left, mid + 1

    while p1 <= mid and p2 <= right:
        if arr[p1] < arr[p2]:
            help_list.append(arr[p1])
            p1 += 1
        else:
            help_list.append(arr[p2])
            p2 += 1

    while p1 <= mid:
        help_list.append(arr[p1])
        p1 += 1

    while p2 <= right:
        help_list.append(arr[p2])
        p2 += 1

    for j in range(len(help_list)):
        arr[left + j] = help_list[j]


def generate_random_test(max_size: int, max_value: int):
    result = []
    size = random.randint(0, max_size + 1)
    for i in range(size):
        result.append((int(max_value + 1) * random.random()) - int(max_value * random.random()))
    return result


if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    test_num = 10000
    max_size = 100
    max_value = 100
    flag = True

    for i in range(test_num):
        list1 = generate_random_test(max_size, max_value)
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        merge_sort(list2)
        list3.sort()
        if list2 != list3:
            flag = False
            print(list1)
            print(list2)
            print(list3)
            break

    print("Nice" if flag else "Fuck")
