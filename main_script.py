import base_class
from qt_run import *
from visual_func import *

# Переменные для дисплея


def fix_error():
    for l in reversed(log):
        log_box.takeItem(len(log) - 1)
        match l.tip:
            case 0:
                a = l.info
                clas[a[0]].teach[a[1]].prior[a[2]] = a[3]
            case 5:
                a = l.info
                clas[a[0]].teach[a[1]].prior[a[2]] = a[3]
            case 1:
                a = l.info
                t = clas[a[0]].teach[a[1]]
                urok[a[0]][a[2]].teach = -1
                t.hour += 1
                teach[t.i].hour += 1
                clas[a[0]].teach[a[1]].prior_log(a[0], a[1], a[2], -117)
                lbl_clas_u[a[0]][a[2]].setText('--')
                #if G.steps < 1:
                #    lbl_clas_u[a[0]][a[2]].setStyleSheet("background-color:" + color2)
                G.error = False
                G.back = False
                log.remove(log[-1])
                break
            case 2:
                a = l.info
                clas[a[0]].teach[a[1]].need = False
            case 3:
                teach[l.info[0]].need = False
            case 4:
                a = l.info
                t = clas[a[0]].teach[a[1]]
                urok[a[0]][a[2]].teach = -1
                lbl_clas_u[a[0]][a[2]].setText('--')
                if G.steps < 1:
                    lbl_clas_u[a[0]][a[2]].setStyleSheet("background-color:" + color2)
                t.hour += 1
                teach[t.i].hour += 1
        log.remove(log[-1])


def check_solo_prior():
    global cI
    global ctI
    global les
    for i, c in enumerate(clas):
        for d in range(G.days * 2):
            if urok[i][d].teach < 0:
                num = 0
                for j, t in enumerate(c.teach):
                    if t.prior[d] > 0:
                        num += 1
                        G.ctI = j
                if i == 2 and d == 1:
                    info_edit[3].setText(str(num))
                if num == 1:
                    G.cI = i
                    G.les = d
                    info_edit[1].setText("type check: 2")
                    return True
                elif num == 0:
                    print("Error 0")
                    G.error = True
                    G.error_type = 0
                    G.error_info[0] = i
                    G.error_info[1] = d
                    return True
    return False

def start_func():
    G.start = False
    clear_lbl()

    for i, c in enumerate(clas):
        for d in range(G.days * 2):
            urok[i][d].num_teach = 0

        for j, t in enumerate(c.teach):
            prior = 100
            for d in range(G.days * 2):
                t.prior[d] = prior #+ random.randint(0, 10)
                urok[i][d].num_teach += 1


def check_prior():
    check = False
    G.les = -1
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
                        #print(1)
                        t.need_log(i, j)
                        for d in range(G.days):
                            if ((urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0)
                            or (urok[i][d * 2 + 1].teach < 0 and t.prior[d * 2 + 1] > 0)):
                                if ((urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0)
                                and (urok[i][d * 2 + 1].teach < 0 and t.prior[d * 2 + 1] > 0)):
                                    t.prior_log(i, j, d * 2, t.prior[d * 2] + 500)
                                    t.prior_log(i, j, d * 2 + 1, t.prior[d * 2 + 1] + 500)
                                else:
                                    if (urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0):
                                        t.prior_log(i, j, d * 2, 1000)
                                    else:
                                        t.prior_log(i, j, d * 2 + 1, 1000)
                    elif num < t.hour:
                        G.error = True
                        print("(!) Error 1")
                        print()

        for t in teach:
            if t.hour > 0 and t.need == False:
                num = 0
                for d in range(G.days * 2):
                    for c in t.clas:
                        if urok[c.i][d].teach < 0 and clas[c.i].teach[c.i1].prior[d] > 0:
                            num += 1
                            break
                if num == t.hour:
                    t.need_log()
                if num < t.hour:
                    G.error = True
                    print("УИААААА")
                    print(t.name)
            if t.need:
                for d in range(G.days * 2):
                    num = 0
                    for c in t.clas:
                        if urok[c.i][d].teach < 0 and clas[c.i].teach[c.i1].prior[d] > 0:
                            num += 1
                            G.cI = c.i
                            G.ctI = c.i1
                            G.les = d
                    if num == 1:
                        #clas[cI].teach[ctI].prior[d] += 1000
                        clas[cI].teach[ctI].prior_log(G.cI, G.ctI, d, 1000)



        ################3

        for i, c in enumerate(clas):
            for j, t in enumerate(c.teach):
                if t.hour == 1:
                    num = 0
                    for d in range(G.days * 2):
                        if urok[i][d].teach < 0 and t.prior[d] > 0:
                            num += 1
                            G.cI = i
                            G.ctI = j
                            G.les = d
                    if num != 1:
                        G.les = -1
                    else:
                        check = True
                        info_edit[1].setText("type check: 1")
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
    global les
    cI_last = cI
    ctI_last = ctI
    les_last = les

    check = check_prior()

    max = 1
    if check == False and G.error == False:
        max = 0
        for d in range(G.days * 2):
            for i, c in enumerate(clas):
                if urok[i][d].teach < 0:
                    for j, t in enumerate(c.teach):
                        if t.hour > 0 and t.prior[d] > max:
                            G.cI = i
                            G.ctI = j
                            G.les = d
                            max = t.prior[d]
    tI = clas[cI].teach[ctI]
    info_edit[2].setText(
        "cI: " + str(G.cI) + ', ctI: ' + str(G.ctI) + ', tI: ' + str(tI) + ', les: ' + str(G.les))
    info_edit[1].setText(info_edit[1].text() + '; Check: ' + str(check))

    #print(len(log), check, G.error, "cI: " + str(cI) + ', ctI: ' + str(ctI) + ', tI: ' + str(tI) + ', les: ' + str(les))

    if max <= 0:
        G.error = True
        print("Беда 4")

    if G.error == False:
        G.cI = cI
        G.ctI = ctI
        G.les = les

        i = les + 1
        if les % 2 == 1:
            i -= 2
        t = clas[cI].teach[ctI]

        urok[cI][les].set(cI, ctI, les)

        for j, t1 in enumerate(clas[cI].teach):
            if t1.pred == t.pred:
                t1.prior_log(cI, j, i, -100)
            else:
                if t1.need and t1.prior[i] > 0:
                    t1.prior_log(cI, j, i, 1000)

        for c in teach[t.i].clas:
            if clas[c.i].teach[c.i1].prior[les] > 0: # Для оптимизации потом можно убрать if
                clas[c.i].teach[c.i1].prior_log(c.i, c.i1, les, -101)
        if clas[cI].teach[ctI].hour == 0:
            for d in range(G.days * 2):
                if clas[cI].teach[ctI].prior[d] > 0:
                    clas[cI].teach[ctI].prior_log(cI, ctI, d, -102)

        tI = clas[cI].teach[ctI].i
        t = teach[tI]
        lbl_clas_u[cI][les].setText(t.pred + str(tI))
        lbl_teach_u[tI][les].setText(str(clas[cI].num) + '-' + clas[cI].name)

    else:
        check_error()


def main_script():
    a = 0


"""
class Main_script(QThread):
    def __init__(self):
        super().__init__()
        self.value = 0

    def run(self):
        while True:

            if G.run:

                G.steps_num += 1
                G.steps -= 1

                if G.error:
                    fix_error()
                else:
                    set_urok()

                if G.steps < 1:
                    G.visual = True
                    time.sleep(0.3)
                    G.run = False

                if G.visual:
                    set_color()
            else:
                time.sleep(0.5)


main_script = Main_script()
main_script.start()
"""