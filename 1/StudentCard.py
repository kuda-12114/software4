#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StudentCard():

    StudentCardList = []

    def getter(self):
        return self.accountBalance

    def setter(self, n):
        self.accountBalance = n

    def __init__(self, a, b):
        self.studentnum = a
        self.studentname = b
        self.accountBalance = 0
        self.StudentCardList.append(self)
