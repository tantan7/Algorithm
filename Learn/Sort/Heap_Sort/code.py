# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/14 下午10:38
# @File     : code.py
# @Project  : Algorithm
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def heap_insert(arr: list, index: int):
    while arr[int((index - 1) / 2)] < arr[index]:
        arr[int((index - 1) / 2)], arr[index] = arr[index], arr[int((index - 1) / 2)]
        index = int((index - 1) / 2)


def heapify(arr: list, index: int, size: int):
    left = 2 * index + 1
    while left < size:
        largest = left + 1 if (left + 1 < size) and (arr[left + 1] > arr[left]) else left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        else:
            arr[index], arr[largest] = arr[largest], arr[index]
            index = largest
            left = 2 * index + 1


def heap_sort(arr: list):
    if len(arr) < 2:
        return
    for index in range(len(arr)):
        heap_insert(arr, index)
    size = len(arr)
    while size > 0:
        size -= 1
        arr[0], arr[size] = arr[size], arr[0]
        heapify(arr, 0, size)


if __name__ == "__main__":
    flag = True
    for i in range(100):
        list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        heap_sort(list2)
        list3.sort()
        if list2 != list3:
            flag = False
            print(list1)
            print(list2)
            print(list3)
            break

    print("Nice" if flag else "Fuck")
