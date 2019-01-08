#!/usr/bin/env python
# -*- coding: utf-8 -*-
from StudentCard import StudentCard
import datetime


class MainShopCharger():
    ChargeDate = "NoCharge"

    def insertStudentCard(self, num):
        self.insertedStudentCard = StudentCard.StudentCardList[num]

    def chargeMoney(self, money):
        if self.insertedStudentCard is None:
            print("学生証が挿入されていません")
        else:
            self.setChargeDate()
            self.insertedStudentCard.setter(
                self.insertedStudentCard.getter() + money)
            self.printAccountBalance()
            self.printChargeDate()

    def printAccountBalance(self):
        print(self.insertedStudentCard.studentname)
        print(str(self.insertedStudentCard.accountBalance))

    def setChargeDate(self):
        self.ChargeDate = datetime.datetime.now()

    def printChargeDate(self):
        print(self.ChargeDate)

    def printSimWord(self):
        if self.insertedStudentCard is None:
            print("学生証が挿入されていません")
        else:
            print("出身地に関係する単語を表示します")
            print("!注意! 環境によってはメモリ不足でエラーが起きますのでご注意ください")
            self.insertedStudentCard.simPrint()

    def main(self):
        self.insertedStudentCard = None
        StudentCard1 = StudentCard(0, "tut", "Osaka")
        StudentCard2 = StudentCard(1, "tenpaku", "Osaka")
        print("機能を選んでください")
        print("0 : チャージ機能")
        print("1 : 出身地の類似語を表示")
        print("2 : 出身地の天気を表示")
        mode = input()
        self.insertStudentCard(0)
        if mode == '0':
            # 1枚目へ処理
            self.chargeMoney(1000)
            self.chargeMoney(-300)
            # 2枚目へ処理
            self.insertStudentCard(1)
            self.chargeMoney(500)
            self.chargeMoney(-1000)
        elif mode == '1':
            # 類似語の表示
            self.printSimWord()
        elif mode == '2':
            # 出身地の天気を表示
            self.insertedStudentCard.getWeather()
        else:
            print("入力エラー")


if __name__ == '__main__':
    m = MainShopCharger()
    m.main()
