#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/27 16:25
# @File     : 1.二叉树遍历.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Node:
    left = None
    right = None

    def __init__(self, value=None):
        self.value = value

    def pre_order_recursive(self):
        if self is None:
            return
        print(self.value, end=' ')
        if self.left:
            self.left.pre_order_recursive()
        if self.right:
            self.right.pre_order_recursive()

    def in_order_recursive(self):
        if self is None:
            return
        if self.left:
            self.left.in_order_recursive()
        print(self.value, end=' ')
        if self.right:
            self.right.in_order_recursive()

    def pos_order_recursive(self):
        if self is None:
            return
        if self.left:
            self.left.pos_order_recursive()
        if self.right:
            self.right.pos_order_recursive()
        print(self.value, end=' ')

    def pre_order_loop(self):
        print("pre order loop: ", end='')
        stack = [self]
        while stack:
            temp = stack.pop()
            print(temp.value, end=' ')
            if temp.right is not None:
                stack.append(temp.right)
            if temp.left is not None:
                stack.append(temp.left)
        print()

    def in_order_loop(self):
        print("in order loop: ", end='')
        if self is not None:
            stack = []
            temp = self
            while stack or temp is not None:
                if temp is not None:
                    stack.append(temp)
                    temp = temp.left
                else:
                    temp = stack.pop()
                    print(temp.value, end=' ')
                    temp = temp.right
        print()

    def pos_order_loop(self):
        """
        前序遍历的次序是：中左右
        后续遍历的次序是：左右中
        相当于将前序遍历中左右的顺序颠倒再倒着打印
        """
        print("pos order loop: ", end='')
        stack1 = []
        if self is not None:
            stack2 = [self]
            while stack2:
                temp = stack2.pop()
                stack1.append(temp)
                if temp.left is not None:
                    stack2.append(temp.left)
                if temp.right is not None:
                    stack2.append(temp.right)
        while stack1:
            print(stack1.pop().value, end=' ')


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)

    print("==============recursive==============")
    print("pre order recursive: ", end='')
    head.pre_order_recursive()
    print()
    print("in order recursive: ", end='')
    head.in_order_recursive()
    print()
    print("pos order recursive: ", end='')
    head.pos_order_recursive()
    print()

    print("============no recursive=============")
    head.pre_order_loop()
    head.in_order_loop()
    head.pos_order_loop()
