from base_class import *

from rasp import *

import sys

but = []
butL = 0
group_pred = []

font = QtGui.QFont()
font.setPointSize(6)

_translate = QtCore.QCoreApplication.translate


def open(self, filename = None):
    if filename == None:
        print("OPEN")
        filename, _ = QFileDialog.getOpenFileName(None, "Open File", ".",
                    "Файлы расписания (*.rsp *.rasp);;Файлы расписания старой версии (*.rasp)")
    if filename:
        file = ui.open(filename)
        print(filename)
        if filename[-4:] == ".rsp":

            G.days = int(file.readline()[:-1])
            ui.lineEdit_days.setText(str(G.days))

            for i in range(7):
                s = file.readline()[:-1]
                if (s != '0'):
                    ui.load_le[i].setText(s)

            for row in range(ui.tableWidget.rowCount()):
                for column in range(ui.tableWidget.columnCount()):
                    s = file.readline()[:-1]
                    if (s != '0'):
                        ui.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(s))

            for i in range(len(group_pred)):
                g = group_pred[i]
                I1 = i
                l1 = int(file.readline()[:-1])
                l2 = len(g.but_del)
                l = l1

                if (l1 > l2):
                    for i2 in range(l2, l1):
                        I = len(g.but_del)
                        g.but_del.append(QtWidgets.QPushButton(g.group[0]))
                        g.but_del[I].setFont(font)
                        g.but_del[I].setObjectName("pushButton_2")
                        g.but_del[I].setText(_translate("MainWindow", "Удалить"))
                        g.but_del[I].clicked.connect(lambda a=0, b=i, c=I: delete_teach(a, b, c))
                        g.layout[0].addWidget(g.but_del[I], I + 1, 0, 1, 1)
                        g.edit.append(QtWidgets.QLineEdit(g.group[0]))
                        g.edit[I].setText("")
                        g.edit[I].setObjectName("lineEdit")
                        g.layout[0].addWidget(g.edit[I], I + 1, 1, 1, 1)
                        g.edit1.append(QtWidgets.QLineEdit(g.group[0]))
                        g.edit[I].setText("")
                        g.edit1[I].setObjectName("lineEdit")
                        g.layout[0].addWidget(g.edit1[I], I + 1, 2, 1, 1)

                        g.but.append([])

                        for i in range(G.days):
                            g.group.append(QtWidgets.QGroupBox(ui.scrollAreaWidgetContents))
                            g.group[i + 1].setTitle("")
                            g.group[i + 1].setObjectName("groupBox")
                            ui.gridTechLoad.addWidget(g.group[i + 1], I1, i + 1, 1, 1)

                            g.layout.append(QtWidgets.QGridLayout(g.group[i + 1]))
                            g.layout[i + 1].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
                            g.layout[i + 1].setContentsMargins(2, 2, 2, 2)
                            g.layout[i + 1].setSpacing(0)
                            g.layout[i + 1].setObjectName("gridLayout")

                            g.space.append(QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum,
                                                                 QtWidgets.QSizePolicy.Fixed))
                            g.layout[i + 1].addItem(g.space[i], 0, 0, 1, 2)

                        for d in range(G.days):
                            for i1 in range(2):
                                g.but[I].append(QtWidgets.QPushButton(g.group[d + 1]))
                                g.but[I][d * 2 + i1].setObjectName("pushButton_2")
                                g.but[I][d * 2 + i1].setMinimumWidth(35)
                                g.but[I][d * 2 + i1].setFont(font)
                                g.but[I][d * 2 + i1].setText(_translate("MainWindow", ""))
                                g.layout[d + 1].addWidget(g.but[I][d * 2 + i1], I + 1, i1, 1, 1)
                elif (l1 < l2):
                    for I in range(l2 - 1, l1 - 1, -1):

                        g.but_del[-1].deleteLater()
                        g.edit[-1].deleteLater()
                        g.edit1[-1].deleteLater()
                        del g.but_del[-1]
                        del g.edit[-1]
                        del g.edit1[-1]

                        for d in range(G.days):
                            for i1 in range(2):
                                g.but[-1][-1].deleteLater()
                                del g.but[-1][-1]
                        del g.but[-1]

                for i in range(l):
                    try:
                        g.edit[i].setText(file.readline()[:-1])
                    except:
                        a = 0
                    try:
                        g.edit1[i].setText(file.readline()[:-1])
                    except:
                        a = 0
            file.close()
        elif filename[-5:] == ".rasp":

            for g in group_pred:
                for i in range(len(g.but_del)):

                    g.but_del[-1].deleteLater()
                    g.edit[-1].deleteLater()
                    g.edit1[-1].deleteLater()
                    del g.but_del[-1]
                    del g.edit[-1]
                    del g.edit1[-1]

                    for d in range(G.days):
                        for i1 in range(2):
                            g.but[-1][-1].deleteLater()
                            del g.but[-1][-1]
                    g.group[-1].deleteLater()
                    del g.group[-1]
                    del g.but[-1]

            G.days = int(file.readline()[:-1])
            ui.lineEdit_days.setText(str(G.days))

            #write(tinker_clas_load.entry_, file)
            for y in range(7):
                #write(tinker_clas_load.entry[y], file)
                #s = file.readline()[:-1]
                #if (s != '0'):
                ui.load_le[y].setText(file.readline()[:-1])
                for x in range(6):
                    #write(tinker_clas_load.entry1[y][x], file)
                    ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(file.readline()[:-1]))

            l = int(file.readline()[:-1])
            for i in range(l):
                s = file.readline()[:-1]
                s1 = file.readline()[:-1]
                s2 = file.readline()[:-1]
                for i_g in range(len(group_pred)):
                    g = group_pred[i_g]
                    if g.pred == s:
                        add_teach(0, i_g)
                        g.edit[-1].setText(s1)
                        g.edit1[-1].setText(s2)
                        break
                #tinker_teach_load.listbox[0].list.insert('end', file.readline()[:-1])
                #tinker_teach_load.listbox[1].list.insert('end', file.readline()[:-1])
                #tinker_teach_load.listbox[2].list.insert('end', file.readline()[:-1])

            """
            l = int(file.readline()[:-1])
            tinker_work.teacher.clear()
            for i in range(l):
                pred = file.readline()[:-1]
                name = file.readline()[:-1]
                load = file.readline()[:-1]
                l1 = int(file.readline()[:-1])
                work = []
                for i1 in range(l1):
                    if (file.readline()[:-1] == "True"):
                        work.append(True)
                    else:
                        work.append(False)
                tinker_work.teacher.append(tinker_work.Teacher(pred, name, load, work))
            reload()
            """
            file.close()


def save(self):
    print("SAVE")
    filename, _ = QFileDialog.getSaveFileName(None, "Save File", ".", "Файл расписания (*.rsp))")

    if filename:
        file = ui.save(filename)
        print(filename)

        file.write(str(G.days) + '\n')

        for i in range(7):
            val = 0
            try:
                val = int(ui.load_le[i].text())
            except:
                val = 0
            file.write(str(val) + '\n')

        for row in range(ui.tableWidget.rowCount()):
            for column in range(ui.tableWidget.columnCount()):
                val = 0
                try:
                    val = int(ui.tableWidget.item(row, column).text())
                except:
                    val = 0
                file.write(str(val) + '\n')

        for g in group_pred:
            l = len(g.but_del)
            file.write(str(l) + '\n')
            for i in range(l):
                s = ''
                try:
                    s = g.edit[i].text() + '\n'
                except:
                    s = ''
                file.write(s)
                try:
                    s = g.edit1[i].text() + '\n'
                except:
                    s = ''
                file.write(s)
        file.close()


def sort(a, i):
    g = group_pred[i]
    l = len(g.but_del)
    for i1 in range(l):
        g.edit[i1].setText(str(len(g.edit)) + "  " + str(i1))
        g.edit1[i1].setText(str(len(g.edit1)) + "  " + str(i1))
        g.but_del[i1].setText(str(len(g.but_del)) + "  " + str(i1))
        for d in range(G.days):
            for i2 in range(2):
                g.but[i1][d * 2 + i2].setText(str(len(g.but)) + "," + str(d * 2 + i2))

def add_teach(a, i):
    g = group_pred[i]
    I1 = i
    I = len(g.but_del)

    if I == 0:
        try:
            G.days = int(ui.lineEdit_days.text())
        except:
            print("Неправильно введёно количество дней")
        for i in range(G.days):
            g.group.append(QtWidgets.QGroupBox(ui.scrollAreaWidgetContents))
            g.group[i + 1].setTitle("")
            g.group[i + 1].setObjectName("groupBox")
            ui.gridTechLoad.addWidget(g.group[i + 1], I1, i + 1, 1, 1)

            g.layout.append(QtWidgets.QGridLayout(g.group[i + 1]))
            g.layout[i + 1].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            g.layout[i + 1].setContentsMargins(2, 2, 2, 2)
            g.layout[i + 1].setSpacing(0)
            g.layout[i + 1].setObjectName("gridLayout")

            g.space.append(QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
            g.layout[i + 1].addItem(g.space[i], 0, 0, 1, 2)

    g.but_del.append(QtWidgets.QPushButton(g.group[0]))
    g.but_del[I].setFont(font)
    g.but_del[I].setObjectName("pushButton_2")
    g.but_del[I].setText(_translate("MainWindow", "Удалить"))
    g.but_del[I].clicked.connect(lambda a=0, b=i, c=I: delete_teach(a, b, c))
    g.layout[0].addWidget(g.but_del[I], I + 1, 0, 1, 1)
    g.edit.append(QtWidgets.QLineEdit(g.group[0]))
    g.edit[I].setText("")
    g.edit[I].setObjectName("lineEdit")
    g.layout[0].addWidget(g.edit[I], I + 1, 1, 1, 1)
    g.edit1.append(QtWidgets.QLineEdit(g.group[0]))
    g.edit[I].setText("")
    g.edit1[I].setObjectName("lineEdit")
    g.layout[0].addWidget(g.edit1[I], I + 1, 2, 1, 1)

    g.but.append([])
    for d in range(G.days):
        for i1 in range(2):
            g.but[I].append(QtWidgets.QPushButton(g.group[d + 1]))
            g.but[I][d * 2 + i1].setObjectName("pushButton_2")
            g.but[I][d * 2 + i1].setMinimumWidth(35)
            g.but[I][d * 2 + i1].setFont(font)
            g.but[I][d * 2 + i1].setText(_translate("MainWindow", ""))
            g.layout[d + 1].addWidget(g.but[I][d * 2 + i1], I + 1, i1, 1, 1)


def delete_teach(a, i, I):
    g = group_pred[i]

    for i1 in range(I, len(g.but_del) - 1):
        g.edit[i1].setText(g.edit[i1 + 1].text())
        g.edit1[i1].setText(g.edit1[i1 + 1].text())

    g.but_del[-1].deleteLater()
    g.edit[-1].deleteLater()
    g.edit1[-1].deleteLater()
    del g.but_del[-1]
    del g.edit[-1]
    del g.edit1[-1]

    for d in range(G.days):
        for i1 in range(2):
            g.but[-1][-1].deleteLater()
            del g.but[-1][-1]
    del g.but[-1]




class Group_pred:
    def __init__(self, name, pred):

        l = len(group_pred)

        self.pred = pred
        self.group = []
        self.layout = []
        self.but_del = []
        self.edit = []
        self.edit1 = []
        self.but = []
        self.space = []

        self.group.append(QtWidgets.QGroupBox(ui.scrollAreaWidgetContents))
        self.group[0].setTitle("")
        self.group[0].setObjectName("groupBox")
        ui.gridTechLoad.addWidget(self.group[0], l, 0, 1, 1)

        self.layout.append(QtWidgets.QGridLayout(self.group[0]))
        self.layout[0].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout[0].setContentsMargins(2, 2, 2, 2)
        self.layout[0].setSpacing(0)
        self.layout[0].setObjectName("gridLayout")

        """
        for i in range(G.days):
            self.group.append(QtWidgets.QGroupBox(ui.scrollAreaWidgetContents))
            self.group[i + 1].setTitle("")
            self.group[i + 1].setObjectName("groupBox")
            ui.gridTechLoad.addWidget(self.group[i + 1], len(group_pred), i + 1, 1, 1)

            self.layout.append(QtWidgets.QGridLayout(self.group[i + 1]))
            self.layout[i + 1].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            self.layout[i + 1].setContentsMargins(2, 2, 2, 2)
            self.layout[i + 1].setSpacing(0)
            self.layout[i + 1].setObjectName("gridLayout")

            self.space.append(QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
            self.layout[i + 1].addItem(self.space[i], 0, 0, 1, 2)
        """

        self.label = QtWidgets.QLabel(self.group[0])
        self.label.setText(_translate("MainWindow", name))
        self.label.setObjectName("label")
        self.layout[0].addWidget(self.label, 0, 0, 1, 1)

        self.but_add = QtWidgets.QPushButton(self.group[0])
        self.but_add.setObjectName("Добавить учителя")
        self.but_add.setMinimumWidth(300)
        self.but_add.setText(_translate("MainWindow", "Добавить учителя"))
        self.but_add.clicked.connect(lambda a = 0, b = len(group_pred): add_teach(a, b))
        self.layout[0].addWidget(self.but_add, 0, 1, 1, 1)
        self.but_add.size().height()

        self.but_sort = QtWidgets.QPushButton(self.group[0])
        self.but_sort.setObjectName("Добавить учителя")
        self.but_sort.setMinimumWidth(300)
        self.but_sort.setText(_translate("MainWindow", "Сортировать"))
        self.but_sort.clicked.connect(lambda a = 0, b = len(group_pred): sort(a, b))
        self.layout[0].addWidget(self.but_sort, 0, 2, 1, 1)


def start():
    group_pred.append(Group_pred('Русский', 'Р'))
    group_pred.append(Group_pred('Иностранный', 'И'))
    group_pred.append(Group_pred('Математика', 'М'))
    group_pred.append(Group_pred('Физика', 'Ф'))
    group_pred.append(Group_pred('Химия', 'Х'))
    group_pred.append(Group_pred('ОБЗР', 'О'))


    for row in range(ui.tableWidget.rowCount()):
        for column in range(ui.tableWidget.columnCount()):
            ui.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(''))

    ui.action1.triggered.connect(save)
    ui.action2.triggered.connect(open)

    ui.lineEdit_days.setText(str(G.days))

