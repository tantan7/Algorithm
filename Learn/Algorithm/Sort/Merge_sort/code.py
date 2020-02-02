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


import copy
import random


def merge_sort(arr: list):
    merge__sort(arr, 0, len(arr) - 1)


def merge__sort(arr: list, left: int, right: int):
    if left == right:
        return
    mid = left + ((right - left) >> 1)
    merge__sort(arr, left, mid)
    merge__sort(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int):
    help_list = []
    temp, p1, p2 = 0, left, mid + 1

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


if __name__ == '__main__':
    flag = True
    for i in range(100):
        list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
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
