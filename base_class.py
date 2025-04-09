import sys
import time
import random
from logging import raiseExceptions

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


color0 = "rgb(255, 255, 255)"
color1 = "rgb(255, 255, 200)"
color2 = "rgb(255, 255, 127)"
color3 = "rgb(200, 200, 200)"
color_error = "rgb(255, 0, 0)"
color_error1 = "rgb(255, 123, 123)"
color0_ = QColor(255, 255, 255)
color1_ = QColor(255, 255, 200)
color2_ = QColor(255, 255, 127)
color3_ = QColor(200, 200, 200)
color_error_ = QColor(255, 0, 0)
color_error1_ = QColor(255, 123, 123)
color_error_light_ = QColor(255, 200, 200)

log = []
teach = []
clas = []
urok = []
prog = [] # тут хранится программа каждого предмета в каждом классе

pred_example = {"Р": 0, "И": 0, "М": 0, "Ф": 0, "Х": 0, "О": 0}
print(pred_example)


pred = ["Р", "И", "М", "Ф", "Х", "О"]

for i in range(5, 12):
    prog.append({"М": 0, "Р": 0, "И": 0, "Ф": 0, "Х": 0, "О": 0})


class G:
    info = False
    run = False
    start = True
    back = False

    cI = 0
    ctI = 0
    les = 0

    visual = True # Если True, вырисовывается последние изменения

    check = False
    days = 4
    lessons = days * 2
    error = False
    error_type = 0
    error_info = [0, 0, 0, 0, 0]
    steps = 0 # сколько осталось
    steps_num = 0 # сколько всего было сделано

class Urok:
    def __init__(self, pred, teach):
        self.pred = pred
        self.teach = teach
        self.num_teach = 0
    def set(self, cI, ctI, les):
        t = clas[cI].teach[ctI]
        tip = 1
        if t.prior[les] >= 1000:
            tip = 4
        log.append(Log(tip, [cI, ctI, les, t.prior[les]]))
        urok[cI][les].teach = t.i
        t.hour -= 1
        teach[t.i].hour -= 1

class Teach1:
    def __init__(self, i, pred, hour, solo):
        self.i = i
        self.hour = hour
        self.maxHour = hour
        teach[i].hour += hour
        teach[i].maxHour += hour
        self.pred = pred
        self.prior = []
        self.need = False
        self.solo = solo # Если True - в программе всего одна пара и препод может вести у любого класса этого номера
        self.friend = -1
    def need_log(self, i, i1):
        log.append(Log(2, [i, i1]))
        self.need = True
    def prior_log(self, cI, j, les, prior):
        tip = 0
        if prior == -117:
            tip = 5
        log.append(Log(tip, [cI, j, les, self.prior[les], prior]))
        self.prior[les] = prior

class Clas1:
    def __init__(self, i, i1):
        self.i = i
        self.i1 = i1

class Clas:
    def __init__(self, num, name):
        self.i = -1
        self.num = num
        self.name = name
        self.teach = []
        self.prog = {}


class Teach:
    def __init__(self, pred, name = "Учитель", load = ""):
        self.i = -1
        self.name = name
        self.pred = pred
        self.hour = 0
        self.maxHour = 0
        self.clas = []
        self.load = load
        self.need = False   #Если True, то обязатеьно куда-то впихнуть
        self.work = [] #True, если может работать в этот день
    def need_log(self):
        log.append(Log(3, [self.i]))
        self.need = True

class Log:
    # 0: Вставка приоритета
    # 1: Вставка урока на выбор
    # 2: need внутри класса
    # 3: need у учителя в общем
    # 4: Вставка 100% урока
    def __init__(self, tip, info):
        self.tip = tip
        self.info = info
        import qt_run
        s = str(tip) + ' ' + str(info)
        color = color1_
        try:
            if tip == 0:
                c = clas[info[0]]
                s = ('PRIOR. Кл: ' + str(c.num) + '-' + str(c.name) + '; Ур: ' + str(info[2]) +
                     '; Уч: ' + teach[c.teach[info[1]].i].name + '; Приор: ' + str(info[3]))
                color = color0_
            elif tip == 1:
                c = clas[info[0]]
                s = ('UROK. Кл: ' + str(c.num) + '-' + str(c.name) + '; Ур: ' + str(info[2]) +
                     '; Уч: ' + teach[c.teach[info[1]].i].name + '; Приор: ' + str(info[3]))
                color = color2_
            elif tip == 2:
                c = clas[info[0]]
                s = ('NEED CLASS. Кл: ' + str(c.num) + '-' + str(c.name) +
                     '; Уч: ' + teach[c.teach[info[1]].i].name)
            elif tip == 2:
                c = clas[info[0]]
                s = ('NEED CLASS. Кл: ' + str(c.num) + '-' + str(c.name) +
                     '; Уч: ' + teach[c.teach[info[1]].i].name)
            elif tip == 3:
                s = ('NEED TEACH. Уч: ' + teach[info[0]].name)
            elif tip == 4:
                c = clas[info[0]]
                s = ('UROK. Кл: ' + str(c.num) + '-' + str(c.name) + '; Ур: ' + str(info[2]) +
                     '; Уч: ' + teach[c.teach[info[1]].i].name + '; Приор: ' + str(info[3]))
                color = color3_
            elif tip == 5:
                c = clas[info[0]]
                s = ('PRIOR. Кл: ' + str(c.num) + '-' + str(c.name) + '; Ур: ' + str(info[2]) +
                     '; Уч: ' + teach[c.teach[info[1]].i].name + '; Приор: ' + str(info[3]))
                color = color_error_light_
        except Exception as e:
            print(e)
            print(tip, info)
        num = len(log)
        s1 = ' '
        if num < 10:
            s1 += ' '
        if num < 100:
            s1 += '  '
        if num < 1000:
            s1 += '   '
        try:
            s = str(num) + s1 + s
            label = QListWidgetItem(s)
            label.setBackground(color)
            qt_run.log_box.addItem(label)
        except Exception as e:
            print(e)


