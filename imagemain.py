#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PIL import Image,ImageOps,ImageQt,ImageMath,ImageFilter,ImageChops
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication,QLabel,QHBoxLayout, QVBoxLayout,QWidget,QFileDialog)
from PyQt5.QtGui import QPixmap


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #ボタン
        btn1 = QPushButton("画像読み込み",self)
        btn1.clicked.connect(self.button1)

        btn2 = QPushButton("左右反転",self)
        btn2.clicked.connect(self.button2)

        btn3 = QPushButton("色交換", self)
        btn3.clicked.connect(self.button3)

        btn4 = QPushButton("線画抽出", self)
        btn4.clicked.connect(self.button4)

        # ラベル表示
        global label

        label = QLabel()

        # ボタンレイアウト
        button_layout = QHBoxLayout()

        button_layout.addWidget(btn1)
        button_layout.addWidget(btn2)
        button_layout.addWidget(btn3)
        button_layout.addWidget(btn4)

        # 画像レイアウト
        image_layout = QVBoxLayout()
        image_layout.addWidget(label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(image_layout)
        main_layout.addLayout(button_layout)

        # セントラルウィジェットを作成
        widget = QWidget(self)

        widget.setLayout(main_layout)

        # セントラルウィジェットの設定
        self.setCentralWidget(widget)

        self.setGeometry(300,300,850,450)
        self.setWindowTitle("画像操作")

        self.show()

    def button1(self): #画像読み込み
        global img
        # dp = os.path.expanduser + 'D:\画像'
        # ディレクトリ選択ダイアログを表示
        filters = "Image (*.png *.gif *.jpg)"
        fileObj = QFileDialog.getOpenFileName(None, "FILE", "", filters)
        filePath = fileObj[0]
        #画像を読み込んでラベルにセットすｒｙ
        img = Image.open(filePath, "r")
        img1 = ImageQt.ImageQt(img)
        Qtimg = img1.copy()
        pm = QPixmap.fromImage(Qtimg)
        label.setPixmap(pm)

    def button2(self): #左右反転
        # pillowで読み込んだ画像を反転
        pm1 = ImageOps.mirror(img)
        # 読み込んだ画像をpillowからQImageに変換
        img1 = ImageQt.ImageQt(pm1)
        Qtimg = img1.copy()
        # QImageからQPixmapに変換
        pm2 = QPixmap.fromImage(Qtimg)
        # labelにセットし表示する
        label.setPixmap(QPixmap(pm2))

    def button3(self): #色交換
        h, s, v = img.convert("HSV").split()
        _h = ImageMath.eval("(h + 230) % 255", h=h).convert("L")
        pm1 = Image.merge("HSV", (_h, s, v)).convert("RGB")
        img1 = ImageQt.ImageQt(pm1)
        Qting = img1.copy()
        pm3 = QPixmap.fromImage(Qting)
        label.setPixmap(pm3)

    def button4(self): #線画抽出
        gray = img.convert("L")
        gray2 = gray.filter(ImageFilter.MaxFilter(5))
        senga_inv = ImageChops.difference(gray2,gray)
        senga = ImageOps.invert(senga_inv)
        img1 = ImageQt.ImageQt(senga)
        Qting = img1.copy()
        pm4 = QPixmap.fromImage(Qting)
        label.setPixmap(pm4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())