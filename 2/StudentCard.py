#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import requests
import json
from gensim.models import KeyedVectors


class StudentCard():

    StudentCardList = []

    Img = cv2.imread("Image.png", 0)

    def getter(self):
        return self.accountBalance

    def setter(self, n):
        self.accountBalance = n

    def simPrint(self):
        model_dir = 'entity_vector.model.bin'
        model = KeyedVectors.load_word2vec_format(model_dir, binary=True)
        similar_rugby_list = model.most_similar(self.freetext)
        for similar_set in similar_rugby_list:
            print(similar_set)

    # 温度変換(ケルビン→摂氏)
    def k2c(sekf, k):
        return k - 273.15

    def getWeather(self):
        print("出身地の天気を表示します")
        print("インターネットに接続されていない場合エラーが起きますのでご注意ください")
        # APIキーの指定
        apikey = "cf133c6636d1768ba2283e0943623008"
        # 天気を調べたい都市の一覧
        cities = [self.freetext]
        # APIのひな型
        api = "http://api.openweathermap.org/data"
        api += "/2.5/weather?q={city}&APPID={key}"
        # 各都市の温度を取得する
        for name in cities:
            # APIのURLを得る
            url = api.format(city=name, key=apikey)
            # 実際にAPIにリクエストを送信して結果を取得する
            r = requests.get(url)
            # 結果はJSON形式なのでデコードする
            data = json.loads(r.text)
            # 結果を出力
            print("+ 都市=", data["name"])
            print("| 天気=", data["weather"][0]["description"])
            print("| 最低気温=", self.k2c(data["main"]["temp_min"]))
            print("| 最高気温=", self.k2c(data["main"]["temp_max"]))
            print("| 湿度=", data["main"]["humidity"])
            print("| 気圧=", data["main"]["pressure"])
            print("| 風向き=", data["wind"]["deg"])
            print("| 風速度=", data["wind"]["speed"])
            print("")

    def __init__(self, a, b, c):
        self.studentnum = a
        self.studentname = b
        self.accountBalance = 0
        self.freetext = c
        self.StudentCardList.append(self)
