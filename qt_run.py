import time
from traceback import print_exc

from base_class import *
import qt_load

from rasp import *
_translate = QtCore.QCoreApplication.translate





letter = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С']

"""
g.but_del.append(QtWidgets.QPushButton(g.group[0]))
g.but_del[I].setFont(font)
g.but_del[I].setObjectName("pushButton_2")
g.but_del[I].setText(_translate("MainWindow", "Удалить"))
#"""


grp_clas = ui.grp_clas
grp_clas_ = ui.grp_clas_
grp_clas_u = ui.grp_clas_u
layout_clas = ui.layout_clas
layout_clas_ = ui.layout_clas_
layout_clas_u = ui.layout_clas_u
lbl_clas = ui.lbl_clas
lbl_clas_ = ui.lbl_clas_
lbl_clas_u = ui.lbl_clas_u
indicator_lbl_clas = ui.indicator_lbl_clas
indicator_lbl_clas_u = ui.indicator_lbl_clas_u
####
grp_teach = ui.grp_teach
grp_teach_ = ui.grp_teach_
grp_teach_u = ui.grp_teach_u
layout_teach = ui.layout_teach
layout_teach_ = ui.layout_teach_
layout_teach_u = ui.layout_teach_u
lbl_teach = ui.lbl_teach
lbl_teach_ = ui.lbl_teach_
lbl_teach_u = ui.lbl_teach_u
indicator_lbl_teach = ui.indicator_lbl_teach
indicator_lbl_teach_u = ui.indicator_lbl_teach_u




def click(obj, tip):
    import visual_func
    if G.run == False:
        type_click = 0
        I = 0
        J = 0
        if tip == 0:
            visual_func.clear_lbl()

        stop = False

        for i in range(len(lbl_teach)):
            lbl_teach[i].setStyleSheet("background-color:" + color0)
            lbl_teach_u[i][0].setStyleSheet("background-color:" + color0)

        for i in range(len(lbl_clas)):
            if obj == lbl_clas[i]:
                if tip == 0:
                    type_click = 1
                    I = i
                stop = True
                if indicator_lbl_clas[i] == 0:
                    indicator_lbl_clas[i] = 1
                    lbl_clas[i].setStyleSheet("background-color:" + color2)
                    for j in range(len(indicator_lbl_clas_u[i])):
                        indicator_lbl_clas_u[i][j] = 1
                        lbl_clas_u[i][j].setStyleSheet("background-color:" + color1)
                else:
                    indicator_lbl_clas[i] = 0
                    lbl_clas[i].setStyleSheet("background-color:" + color0)
                    for j in range(len(indicator_lbl_clas_u[i])):
                        indicator_lbl_clas_u[i][j] = 0
                        lbl_clas_u[i][j].setStyleSheet("background-color:" + color0)
                break

        if stop == False:
            for y in range(len(lbl_clas_u)):
                if stop == False:
                    for x in range(len(lbl_clas_u[y])):
                        if obj == lbl_clas_u[y][x]:
                            if tip == 0:
                                type_click = 2
                                I = y
                                J = x
                            if indicator_lbl_clas_u[y][x] < 2:
                                indicator_lbl_clas_u[y][x] = 2
                                lbl_clas_u[y][x].setStyleSheet("background-color:" + color2)
                                indicator_lbl_clas[y] = 1
                                lbl_clas[y].setStyleSheet("background-color:" + color2)
                            else:
                                indicator_lbl_clas_u[y][x] = 0
                                lbl_clas_u[y][x].setStyleSheet("background-color:" + color0)
                                indicator_lbl_clas[y] = 0
                                lbl_clas[y].setStyleSheet("background-color:" + color0)

                else:
                    break

        if stop == False:
            for i in range(len(lbl_teach)):
                if obj == lbl_teach[i]:
                    if tip == 0:
                        type_click = 3
                        I = i
                    stop = True
                    for j in teach[I].clas:
                        lbl_clas[j.i].setStyleSheet("background-color:" + color2)
                    break

        if type_click == 1:
            i = I
            for t in clas[i].teach:
                try:
                    num = 0
                    if t.hour > 0:
                        for d in range(G.days):
                            if ((urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0)
                                    or (urok[i][d * 2 + 1].teach < 0 and t.prior[d * 2 + 1] > 0)):
                                num += 1
                    lbl_teach_[t.i].setText(str(num) + '/' + str(t.hour) + '/' + str(t.maxHour))
                    lbl_teach[t.i].setStyleSheet("background-color:" + color2)
                    lbl_teach_[t.i].setStyleSheet("background-color:" + color2)
                except:
                    print("Буда")

        elif type_click == 2:
            i = I
            j = J
            for t in clas[i].teach:
                try:
                    lbl_teach_[t.i].setText(str(t.prior[j]))
                    lbl_teach[t.i].setStyleSheet("background-color:" + color2)
                    lbl_teach_[t.i].setStyleSheet("background-color:" + color2)
                except Exception:
                    traceback.format_exc()
                    print("Буда")


def run_script():
    import visual_func
    visual_func.clear_lbl()
    G.run = not G.run
    G.back = False
    G.steps = -1


def step_script():
    import visual_func
    visual_func.clear_lbl()
    G.run = True
    G.back = False
    G.steps = 1

def step100_script():
    import visual_func
    visual_func.clear_lbl()
    G.run = True
    G.back = False
    G.steps = 100

def back_script():
    if G.run == False:
        import visual_func
        visual_func.clear_lbl()
        G.run = True
        G.back = True
        G.steps = 1

def load_clas_widget():

    clas_temp = -1 # текущий номер класса
    for i in range(len(clas)):
        c = clas[i]
        if clas_temp != c.num:
            clas_temp = c.num
            grp_clas.append(QtWidgets.QGroupBox(glob_grp_c))
            glob_lt_c.addWidget(grp_clas[-1], len(grp_clas) - 1, 1, 1, 1)
            layout_clas.append(QtWidgets.QGridLayout(grp_clas[-1]))
            grp_clas[-1].setStyleSheet("QGroupBox"
                           "{"
                           "border : solid black;"
                           "border-width : 1px 1px 1px 1px;"
                           "}")
            layout_clas[-1].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            layout_clas[-1].setContentsMargins(0, 0, 0, 0)
            layout_clas[-1].setSpacing(0)
            ###########
            grp_clas_.append(QtWidgets.QGroupBox(glob_grp_c))
            glob_lt_c.addWidget(grp_clas_[-1], len(grp_clas) - 1, 0, 1, 1)
            layout_clas_.append(QtWidgets.QGridLayout(grp_clas_[-1]))
            grp_clas_[-1].setStyleSheet("QGroupBox"
                           "{"
                           "border : solid black;"
                           "border-width : 1px 1px 1px 1px;"
                           "}")
            layout_clas_[-1].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            layout_clas_[-1].setContentsMargins(0, 0, 0, 0)
            layout_clas_[-1].setSpacing(0)

            grp_clas_u.append([])
            layout_clas_u.append([])
            for d in range(G.days):
                grp_clas_u[-1].append(QtWidgets.QGroupBox(glob_grp_c))
                glob_lt_c.addWidget(grp_clas_u[-1][d], len(grp_clas_u) - 1, d + 2, 1, 1)
                layout_clas_u[-1].append(QtWidgets.QGridLayout(grp_clas_u[-1][d]))
                layout_clas_u[-1][d].setContentsMargins(0, 0, 0, 0)
                layout_clas_u[-1][d].setSpacing(0)
                grp_clas_u[-1][d].setStyleSheet("QGroupBox"
                           "{"
                           "border : solid black;"
                           "border-width : 1px 1px 1px 1px;"
                           "}")

        lbl_clas.append(QtWidgets.QLabel(grp_clas[-1]))
        layout_clas[-1].addWidget(lbl_clas[i], i, 0, 1, 1)
        indicator_lbl_clas.append(0)
        lbl_clas[i].setText(str(c.num) + "-" + str(c.name))
        lbl_clas[i].setMinimumSize(35, 10)
        lbl_clas[i].setAlignment(QtCore.Qt.AlignCenter)

        lbl_clas[i].installEventFilter(ui.tab_3)
        ####
        lbl_clas_.append(QtWidgets.QLabel(grp_clas_[-1]))
        layout_clas_[-1].addWidget(lbl_clas_[i], i, 0, 1, 1)
        lbl_clas_[i].setText(" ")
        lbl_clas_[i].setMinimumSize(40, 10)
        lbl_clas_[i].setAlignment(QtCore.Qt.AlignCenter)

        lbl_clas_u.append([])
        indicator_lbl_clas_u.append([])

        for d in range(G.days):
            for i1 in range(2):
                I = d * 2 + i1
                indicator_lbl_clas_u[i].append(0)
                lbl_clas_u[i].append(QtWidgets.QLabel(grp_clas_u[-1][d]))
                layout_clas_u[-1][d].addWidget(lbl_clas_u[i][I], len(lbl_clas_u) - 1, i1, 1, 1)
                lbl_clas_u[i][I].setObjectName("label" + str(i) + "_" + str(I))
                lbl_clas_u[i][I].setText(_translate("MainWindow", "--"))
                lbl_clas_u[i][I].setMinimumSize(35, 10)

                lbl_clas_u[i][I].setAlignment(QtCore.Qt.AlignCenter)

                lbl_clas_u[i][I].installEventFilter(ui.tab_3)

    spacerItem_c = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    glob_lt_c.addItem(spacerItem_c, len(clas) + 1, 0, 1, G.days * 2 + 1)



def load_teach_widget():

    _translate = QtCore.QCoreApplication.translate
    teach_pred = "" # текущий предмет учителя
    for i in range(len(teach)):
        t = teach[i]
        if teach_pred != t.pred:
            teach_pred = t.pred
            grp_teach.append(QtWidgets.QGroupBox(glob_grp_t))
            glob_lt_t.addWidget(grp_teach[-1], len(grp_teach) - 1, 1, 1, 1)
            layout_teach.append(QtWidgets.QGridLayout(grp_teach[-1]))
            grp_teach[-1].setStyleSheet("QGroupBox"
                           "{"
                           "border : solid black;"
                           "border-width : 1px 1px 1px 1px;"
                           "}")
            layout_teach[-1].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            layout_teach[-1].setContentsMargins(0, 0, 0, 0)
            layout_teach[-1].setSpacing(0)
            ###################
            grp_teach_.append(QtWidgets.QGroupBox(glob_grp_t))
            glob_lt_t.addWidget(grp_teach_[-1], len(grp_teach_) - 1, 0, 1, 1)
            layout_teach_.append(QtWidgets.QGridLayout(grp_teach_[-1]))
            grp_teach_[-1].setStyleSheet("QGroupBox"
                           "{"
                           "border : solid black;"
                           "border-width : 1px 1px 1px 1px;"
                           "}")
            layout_teach_[-1].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            layout_teach_[-1].setContentsMargins(0, 0, 0, 0)
            layout_teach_[-1].setSpacing(0)

            grp_teach_u.append([])
            layout_teach_u.append([])
            for d in range(G.days):
                grp_teach_u[-1].append(QtWidgets.QGroupBox(glob_grp_t))
                glob_lt_t.addWidget(grp_teach_u[-1][d], len(grp_teach_u) - 1, d + 2, 1, 1)
                layout_teach_u[-1].append(QtWidgets.QGridLayout(grp_teach_u[-1][d]))
                layout_teach_u[-1][d].setContentsMargins(0, 0, 0, 0)
                layout_teach_u[-1][d].setSpacing(0)
                grp_teach_u[-1][d].setStyleSheet("QGroupBox"
                           "{"
                           "border : solid black;"
                           "border-width : 1px 1px 1px 1px;"
                           "}")

        lbl_teach.append(QtWidgets.QLabel(grp_teach[-1]))
        layout_teach[-1].addWidget(lbl_teach[i], i, 0, 1, 1)
        indicator_lbl_teach.append(0)

        lbl_teach[i].setText(str(t.i) + '  ' + t.name)
        lbl_teach[i].setAlignment(QtCore.Qt.AlignCenter)

        lbl_teach[i].installEventFilter(ui.tab_3)
        #############
        lbl_teach_.append(QtWidgets.QLabel(grp_teach_[-1]))
        layout_teach_[-1].addWidget(lbl_teach_[i], i, 0, 1, 1)
        lbl_teach_[i].setText(" ")
        lbl_teach_[i].setMinimumSize(40, 10)
        lbl_teach_[i].setAlignment(QtCore.Qt.AlignCenter)

        lbl_teach_u.append([])
        indicator_lbl_teach_u.append([])

        for d in range(G.days):
            for i1 in range(2):
                I = d * 2 + i1
                indicator_lbl_teach_u[i].append(0)
                lbl_teach_u[i].append(QtWidgets.QLabel(grp_teach_u[-1][d]))
                layout_teach_u[-1][d].addWidget(lbl_teach_u[i][I], len(lbl_teach_u) - 1, i1, 1, 1)
                lbl_teach_u[i][I].setObjectName("label" + str(i) + "_" + str(I))
                lbl_teach_u[i][I].setText(_translate("MainWindow", "--"))
                lbl_teach_u[i][I].setMinimumSize(35, 10)

                lbl_teach_u[i][I].setAlignment(QtCore.Qt.AlignCenter)

                lbl_teach_u[i][I].installEventFilter(ui.tab_3)

    spacerItem_t = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    glob_lt_t.addItem(spacerItem_t, len(teach) + 1, 0, 1, G.days * 2 + 1)



def load_pred():
    j = -1
    for i in range(5, 12):
        j = -1
        for p in pred:
            j += 1
            val = 0
            try:
                val = int(ui.tableWidget.item(j, i - 5).text())
            except Exception:
                traceback.format_exc()
                val = 0
            prog[i - 5][p] = val

def load_load():
    for i in range(len(clas)):
        c = clas[i]
        c.i = i
        for p in pred:
            c.prog[p] = prog[c.num - 5][p]

    for i in range(len(teach)):
        t = teach[i]
        t.i = i
        run = True
        I = 0
        t.load += '   '
        try:
            while I <= len(t.load) - 3:
                num_clas = int(t.load[I])
                if (num_clas == 1):
                    num_clas = 10 + int(t.load[I + 1])
                    I += 1
                p = prog[num_clas - 5][t.pred]
                #"""
                solo = False
                checkConnect = False
                if (p == 1):
                    solo = True
                else:
                    if (t.load[I + 1] == '('):
                        solo = False
                        p = int(t.load[I + 2])
                        I += 3
                        checkConnect = True
                #"""
                nice = False
                if checkConnect:
                    for cI, c in enumerate(clas):
                        if c.prog[t.pred] - p >= 0:
                            print("A")
                            for teach1 in c.teach:
                                if t.i == teach1.i:
                                    break
                            else:
                                print("B")
                                nice = True
                                c.prog[t.pred] = c.prog[t.pred] - p
                                c.teach.append(Teach1(t.i, t.pred, p, solo))
                                t.clas.append(Clas1(cI, len(c.teach) - 1))
                                print('HMMM')
                                break
                else:
                    for cI, c in enumerate(clas):
                        if c.num == num_clas and c.prog[t.pred] - p == 0:
                            nice = True
                            c.prog[t.pred] = 0  #c.prog[t.pred] - p
                            c.teach.append(Teach1(t.i, t.pred, p, solo))
                            t.clas.append(Clas1(cI, len(c.teach) - 1))
                            break
                if nice == False:
                    print("БЕДААААААААА!!!!")
                    print(t.name)
                I += 2
        except Exception as e:
            traceback.format_exc()
            print("Беда с", t.name)
    """
        for i in range(len(teach)):
            t = teach[i]
            t.i = i
            t.name = str(i)
            if (i < 10):
                t.name = "0" + t.name
            l = teach[i].load
            last_clas = -1
            for i1 in range(len(l) // 3):
                #   l[+0] - предмет, l[+1] - класс, l[+2] - часы
                if (l[i1 * 3 + 2] == 0):
                    l[i1 * 3 + 2] = get_proga(l[i1 * 3 + 1], l[i1 * 3])
                g.hour += l[i1 * 3 + 2]
                stop = False
                debik = True
                for c in clas:
                    if (stop == False):
                        if (c.num == l[i1 * 3 + 1]) and (last_clas != c.i):
                            for p in c.proga:
                                if (p.pred == l[i1 * 3]) and (p.hour - l[i1 * 3 + 2] >= 0):
                                    c.teach.append(Teach1(i, l[i1 * 3 + 2], l[i1 * 3]))
                                    t.clas.append(Clas1(c.i, len(c.teach) - 1))
                                    teach[i].hour += l[i1 * 3 + 2]
                                    teach[i].maxHour += l[i1 * 3 + 2]
                                    p.hour -= l[i1 * 3 + 2]
                                    stop = True
                                    last_clas = c.i
                                    for i2 in range(len(c.teach) - 1):
                                        if (l[i1 * 3] == c.teach[i2].pred):
                                            c.teach[len(c.teach) - 1].sleep = True
                                            c.teach[i2].friend = len(c.teach) - 1
                                    debik = False
                                    break

                if (debik):
                    print("DEBIK (!)(!)(!)", t.name1)
    """

def load_teach():
    for g in qt_load.group_pred:
        for i in range(len(g.edit)):
            e = g.edit[i]
            e1 = g.edit1[i]
            s = ''
            try:
                s = e.text()
            except:
                s = ''
            s1 = ''
            try:
                s1 = e1.text()
            except:
                s1 = ''
            teach.append(Teach(g.pred, s, s1))

def load_clas():
    for i in range(7):
        l = 0
        try:
            l = int(ui.load_le[i].text())
        except:
            l = 0
        for i1 in range(l):
            clas.append(Clas(i + 5, letter[i1]))

def load_urok():
    for c in clas:

        urok.append([])
        for d in range(G.days * 2):
            urok[-1].append(Urok("N", -1))

        for t in c.teach:
            for d in range(G.days * 2):
                t.prior.append(100)


def run_load():
    load_clas()
    load_teach()
    load_pred()
    load_load()
    load_clas_widget()
    load_teach_widget()
    load_urok()

    import main_script
    main_script.start_func()

    #run_load()





grLt3 = QtWidgets.QGridLayout(ui.tab_3)
grLt3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
grLt3.setContentsMargins(5, 5, 5, 5)
grLt3.setObjectName("grLt")
####
glob_grp_c = QtWidgets.QGroupBox(ui.tab_3)
glob_grp_c.setFlat(False)
glob_grp_c.setCheckable(False)
glob_grp_c.setObjectName("groupBox")

glob_lt_c = QtWidgets.QGridLayout(glob_grp_c)
glob_lt_c.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
glob_lt_c.setContentsMargins(0, 0, 0, 0)
glob_lt_c.setObjectName("grLt")
glob_lt_c.setSpacing(0)
####
glob_grp_t = QtWidgets.QGroupBox(ui.tab_3)
glob_grp_t.setFlat(False)
glob_grp_t.setCheckable(False)
glob_grp_t.setObjectName("groupBox")

glob_lt_t = QtWidgets.QGridLayout(glob_grp_t)
glob_lt_t.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
glob_lt_t.setContentsMargins(0, 0, 0, 0)
glob_lt_t.setObjectName("grLt")
glob_lt_t.setSpacing(0)
####
textEdit_info = QtWidgets.QTextEdit(glob_grp_c)
glob_lt_c.addWidget(textEdit_info, 10, 0, 10, 10)
###

#self.layout.append(QtWidgets.QGridLayout(self.group[i + 1]))

control_grp = QtWidgets.QGroupBox(ui.tab_3)
control_grp.setFlat(False)
control_grp.setCheckable(False)
control_grp.setObjectName("groupBox")

control_lt = QtWidgets.QGridLayout(control_grp)
control_lt.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
control_lt.setContentsMargins(0, 0, 0, 0)
control_lt.setObjectName("grLt")
control_lt.setSpacing(0)


info_grp = QtWidgets.QGroupBox(ui.tab_3)
info_grp.setFlat(False)
info_grp.setCheckable(False)
info_grp.setObjectName("groupBox")

info_lt = QtWidgets.QGridLayout(info_grp)
info_lt.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
info_lt.setContentsMargins(0, 0, 0, 0)
info_lt.setObjectName("grLt")
info_lt.setSpacing(0)

info_edit = []
for i in range(6):
    info_edit.append(QtWidgets.QLineEdit(info_grp))
    info_lt.addWidget(info_edit[i], 0, i, 1, 1)


butonCreate = QtWidgets.QPushButton(control_grp)
butonCreate.setObjectName("pushButt")
butonCreate.clicked.connect(run_load)
butonCreate.setText("Создать")
control_lt.addWidget(butonCreate, 0, 0, 1, 1)

butonRun = QtWidgets.QPushButton(control_grp)
butonRun.setObjectName("pushButt")
butonRun.clicked.connect(run_script)
butonRun.setText("Пуск")
control_lt.addWidget(butonRun, 0, 1, 1, 1)

butonStep = QtWidgets.QPushButton(control_grp)
butonStep.setObjectName("pushButt")
butonStep.clicked.connect(step_script)
butonStep.setText("Шаг")
control_lt.addWidget(butonStep, 0, 2, 1, 1)

butonStep1 = QtWidgets.QPushButton(control_grp)
butonStep1.setObjectName("pushButt")
butonStep1.clicked.connect(step100_script)
butonStep1.setText("Шаг100")
control_lt.addWidget(butonStep1, 0, 3, 1, 1)

butonBack = QtWidgets.QPushButton(control_grp)
butonBack.setObjectName("pushButt")
butonBack.clicked.connect(back_script)
butonBack.setText("Назад")
control_lt.addWidget(butonBack, 0, 4, 1, 1)

def script_error_stop(checked):
    if checked:
        G.error_stop = True
    else:
        G.error_stop = False


def script_visual(checked):
    if checked:
        G.visual = True
    else:
        G.visual = False


checkBox_error_stop = QtWidgets.QCheckBox(control_grp)
checkBox_error_stop.setText( "Стоп ошибка")
checkBox_error_stop.stateChanged.connect(script_error_stop)
control_lt.addWidget(checkBox_error_stop, 0, 5, 1, 1)

checkBox_visual = QtWidgets.QCheckBox(control_grp)
checkBox_visual.setText( "Визуал")
checkBox_visual.stateChanged.connect(script_visual)
control_lt.addWidget(checkBox_visual, 0, 6, 1, 1)

log_box = QtWidgets.QListWidget(ui.tab_3)
log_box.setMinimumSize(430, 500)

grLt3.addWidget(control_grp, 0, 0, 1, 2)
grLt3.addWidget(info_grp, 1, 0, 1, 2)
grLt3.addWidget(glob_grp_c, 2, 0, 1, 1)
grLt3.addWidget(glob_grp_t, 2, 1, 1, 1)
grLt3.addWidget(log_box, 0, 2, 3, 1)

spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
grLt3.addItem(spacerItem, 2, 0, 1, 2)