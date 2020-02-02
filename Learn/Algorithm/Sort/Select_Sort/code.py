#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/12 下午6:20
# @Author   : alex
# @File     : code.py
# @Project  : Algorithm
# @Software : PyCharm


def select_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


data = [1568, 4458, 5847, 854, 15, 48, 151, 84, 1, 2185, 4]
select_sort(data)
print(data)
