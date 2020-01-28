#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/28 16:27
# @File     : 3061.Subsequence.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import sys

for item in range(int(input())):
    length, target = map(int, input().split())
    sequence = list(map(int, input().split()))
    left, right, ans = 0, 0, sys.maxsize
    sum_num = sequence[left]
    while right < length:
        if sum_num < target:
            right += 1
            sum_num += sequence[right]
        else:
            ans = min(right - left + 1, ans)
            sum_num -= sequence[left]
            left += 1
    print(ans if ans != sys.maxsize else 0)
