#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/12 下午6:27
# @Author   : alex
# @File     : code.py
# @Project  : Algorithm
# @Software : PyCharm


def insert_sort(arr: list):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


data = [1568, 4458, 5847, 854, 15, 48, 151, 84, 1, 2185, 4]
insert_sort(data)
print(data)
