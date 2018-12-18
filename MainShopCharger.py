#!/usr/bin/env python
# -*- coding: utf-8 -*-
from StudentCard import StudentCard


class MainShopCharger():

    def insertStudentCard(self, num):
        self.insertedStudentCard = StudentCard.StudentCardList[num]

    def chargeMoney(self, money):
        if self.insertedStudentCard is None:
            print("学生証が挿入されていません")
        else:
            self.insertedStudentCard.setter(
                self.insertedStudentCard.getter() + money)
            self.printAccountBalance()

    def printAccountBalance(self):
        print(self.insertedStudentCard.studentname)
        print(str(self.insertedStudentCard.accountBalance))

    def main(self):
        self.insertedStudentCard = None
        StudentCard1 = StudentCard(0, "tut")
        StudentCard2 = StudentCard(1, "tenpaku")
        # 1枚目へ処理
        self.insertStudentCard(0)
        self.chargeMoney(1000)
        self.chargeMoney(-300)
        # 2枚目へ処理
        self.insertStudentCard(1)
        self.chargeMoney(500)
        self.chargeMoney(-1000)


if __name__ == '__main__':
    m = MainShopCharger()
    m.main()
