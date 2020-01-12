#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/12 下午5:43
# @Author   : alex
# @File     : code.py
# @Project  : Algorithm
# @Software : PyCharm


def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


data = [1568, 4458, 5847, 854, 15, 48, 151, 84, 1, 2185, 4]
bubble_sort(data)
print(data)
