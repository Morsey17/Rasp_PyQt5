import time
from qt_run import *

# Переменные для дисплея
cI = 0
tI = 0
ctI = 0
les = 0


def check_solo_prior():
    global cI
    global tI
    global ctI
    global les
    for i, c in enumerate(clas):
        for d in range(G.days * 2):
            if urok[i][d].teach < 0:
                num = 0
                for j, t in enumerate(c.teach):
                    if t.prior[d] > 0:
                        num += 1
                        ctI = j
                if i == 2 and d == 1:
                    info_edit[3].setText(str(num))
                if num == 1:
                    cI = i
                    tI = clas[cI].teach[ctI].i
                    les = d
                    info_edit[1].setText("type check: 2")
                    info_edit[2].setText(
                        "cI: " + str(cI) + ', ctI: ' + str(ctI) + ', tI: ' + str(tI) + ', les: ' + str(les))
                    return True
                elif num == 0:
                    print("Error 0")
                    G.error = True
                    return True
    return False

def start_func():
    msg.start = False
    clear_lbl()

    for i, c in enumerate(clas):
        for d in range(G.days * 2):
            urok[i][d].num_teach = 0

        for j, t in enumerate(c.teach):
            prior = 100
            for d in range(G.days * 2):
                t.prior[d] = prior
                urok[i][d].num_teach += 1


def check_prior():
    global les
    global cI
    global ctI
    global tI
    check = False
    les = -1
    try:
        for i, c in enumerate(clas):
            for j, t in enumerate(c.teach):
                if t.hour > 0 and t.need == False:
                    num = 0
                    for d in range(G.days):
                        if ((urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0)
                        or (urok[i][d * 2 + 1].teach < 0 and t.prior[d * 2 + 1] > 0)):
                            num += 1
                    if num == t.hour:
                        log.append(Log(2, [i, j]))
                        t.need = True
                        for d in range(G.days):
                            if ((urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0)
                            or (urok[i][d * 2 + 1].teach < 0 and t.prior[d * 2 + 1] > 0)):
                                if ((urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0)
                                and (urok[i][d * 2 + 1].teach < 0 and t.prior[d * 2 + 1] > 0)):
                                    log.append(Log(0, [i, j, d * 2, t.prior[d * 2]]))
                                    log.append(Log(0, [i, j, d * 2 + 1, t.prior[d * 2 + 1]]))
                                    t.prior[d * 2] += 500
                                    t.prior[d * 2 + 1] += 500
                                else:
                                    if (urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0):
                                        log.append(Log(0, [i, j, d * 2, t.prior[d * 2]]))
                                        t.prior[d * 2] += 1000
                                    else:
                                        log.append(Log(0, [i, j, d * 2 + 1, t.prior[d * 2 + 1]]))
                                        t.prior[d * 2 + 1] += 1000
                    elif num < t.hour:
                        G.error = True
                        print("(!) Error 1")

        for t in teach:
            if t.hour > 0 and t.need == False:
                num = 0
                for d in range(G.days * 2):
                    for c in t.clas:
                        if urok[c.i][d].teach < 0 and clas[c.i].teach[c.i1].prior[d] > 0:
                            num += 1
                            break
                if num == t.hour:
                    log.append(Log(3, t.i))
                    t.need = True
                if num < t.hour:
                    # eror
                    print("УИААААА")
            if t.need:
                for d in range(G.days * 2):
                    num = 0
                    for c in t.clas:
                        if urok[c.i][d].teach < 0 and clas[c.i].teach[c.i1].prior[d] > 0:
                            num += 1
                            cI = c.i
                            ctI = c.i1
                            les = d
                    if num == 1:
                        clas[cI].teach[ctI].prior[d] += 1000



        ################3

        for i, c in enumerate(clas):
            for j, t in enumerate(c.teach):
                if t.hour == 1:
                    num = 0
                    for d in range(G.days * 2):
                        if urok[i][d].teach < 0 and t.prior[d] > 0:
                            num += 1
                            cI = i
                            ctI = j
                            tI = teach[t.i].i
                            les = d
                    if num != 1:
                        les = -1
                    else:
                        check = True
                        info_edit[1].setText("type check: 1")
                        info_edit[2].setText(
                            "cI: " + str(cI) + ', ctI: ' + str(ctI) + ', tI: ' + str(tI) + ', les: ' + str(les))
                        break
                    if num < 0:
                        G.error = True
                        print("Беда 3 (часы есть, а некуда ставить)")



            else:
                continue
            break

        if check == False:
            check = check_solo_prior()

    except Exception as e:
        G.error = True
        print(e)
        print("Беда-с")
    return check

def set_urok():

    global cI
    global ctI
    global tI
    global les

    try:
        lbl_clas_u[cI][les].setStyleSheet("background-color:" + color0)
        lbl_clas_[cI].setStyleSheet("background-color:" + color0)
        lbl_clas[cI].setStyleSheet("background-color:" + color0)
        lbl_teach_u[tI][les].setStyleSheet("background-color:" + color0)
        lbl_teach_[tI].setStyleSheet("background-color:" + color0)
        lbl_teach[tI].setStyleSheet("background-color:" + color0)
    except:
        print("Беда 1 (очистка)")

    check = check_prior()
    info_edit[0].setText(str(check))

    max = 1
    if check == False:
        max = 0
        for d in range(G.days * 2):
            for i, c in enumerate(clas):
                if urok[i][d].teach < 0:
                    for j, t in enumerate(c.teach):
                        if t.hour > 0 and t.prior[d] > max:
                            cI = i
                            ctI = j
                            tI = t.i
                            les = d
                            max = t.prior[d]
    if max > 0:

        try:
            for t in teach:
                lbl_teach_[t.i].setText('')
                lbl_teach[t.i].setStyleSheet("background-color:" + color0)
                lbl_teach_[t.i].setStyleSheet("background-color:" + color0)
            for t in clas[cI].teach:
                lbl_teach[t.i].setStyleSheet("background-color:" + color1)
                lbl_teach_[t.i].setStyleSheet("background-color:" + color1)
                lbl_teach_[t.i].setText(str(t.prior[les]) + '  ' + str(t.need))
        except:
            print("Ни могу 1")

        i = les + 1
        if les % 2 == 1:
            i -= 2
        t = clas[cI].teach[ctI]
        urok[cI][les].teach = t.i

        log.append(Log(1, [cI, ctI, les]))

        for j, t1 in enumerate(clas[cI].teach):
            if t1.pred == t.pred:
                log.append(Log(0, [cI, j, i, t1.prior[i]]))
                t1.prior[i] = -100
            else:
                if t1.need and t1.prior[i] > 0:
                    log.append(Log(0, [cI, j, i, t1.prior[i]]))
                    t1.prior[i] += 1000

        t.hour -= 1
        teach[t.i].hour -= 1

        for c in teach[t.i].clas:
            if clas[c.i].teach[c.i1].prior[les] > 0: # Для оптимизации потом можно убрать if
                log.append(Log(0, [c.i, c.i1, les, clas[c.i].teach[c.i1].prior[les]]))
                clas[c.i].teach[c.i1].prior[les] = -101
        if clas[cI].teach[ctI].hour == 0:
            for d in range(G.days * 2):
                if clas[cI].teach[ctI].prior[d] > 0:
                    log.append(Log(0, [cI, ctI, d, clas[cI].teach[ctI].prior[d]]))
                    clas[cI].teach[ctI].prior[d] = -102

    else:
        G.error = True
        print("Беда 4")

    if G.error:
        msg.run = False

    try:
        t = teach[tI]
        lbl_clas_u[cI][les].setText(t.pred + ' ' + str(t.i))
        lbl_clas_u[cI][les].setStyleSheet("background-color:" + color2)
        lbl_clas_[cI].setStyleSheet("background-color:" + color2)
        lbl_clas[cI].setStyleSheet("background-color:" + color2)
        lbl_teach_u[tI][les].setText(str(clas[cI].num) + '-' + clas[cI].name)
        lbl_teach_u[tI][les].setStyleSheet("background-color:" + color2)
        lbl_teach_[tI].setStyleSheet("background-color:" + color2)
        lbl_teach[tI].setStyleSheet("background-color:" + color2)

    except:
        print("Беда 2 (заполнение)")




class Main_script(QThread):
    def __init__(self):
        super().__init__()
        self.value = 0

    def run(self):
        while True:
            if msg.run:
                if G.steps > 0:
                    G.steps -= 1
                    set_urok()
                    if G.steps <= 1:
                        time.sleep(0.5)
                else:
                    msg.run = False
            else:
                time.sleep(0.5)


main_script = Main_script()
main_script.start()