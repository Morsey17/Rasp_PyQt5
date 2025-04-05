import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget

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
    days = 4
    lessons = days * 2
    error = False
    steps = 0

class Urok:
    def __init__(self, pred, teach):
        self.pred = pred
        self.teach = teach
        self.num_teach = 0

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

class Log:
    def __init__(self, tip, s):
        self.tip = tip
        self.s = s