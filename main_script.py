import base_class
import qt_run
from qt_run import *
from visual_func import *

# Переменные для дисплея


def otkat():
    for i in range(len(log) - 1, -1, -1):
        l = log[i]
        log_box.takeItem(len(log) - 1)

        if l.tip == 'SET_PRIOR' or l.tip == 'SET_PRIOR_CRIT':
            a = l.info
            clas[a[0]].teach[a[1]].prior[a[2]] = a[3]
            lbl_clas_u[a[0]][a[2]].setText('--')
            if l.tip == 'SET_PRIOR_CRIT':
                G.error = True
                log.remove(log[-1])
                break

        elif l.tip == 'SET_UROK' or l.tip == 'SET_UROK_REC':
            a = l.info
            t = clas[a[0]].teach[a[1]]
            urok[a[0]][a[2]].teach = -1
            t.hour += 1
            teach[t.i].hour += 1
            lbl_clas_u[a[0]][a[2]].setText('--')
            log.remove(log[-1])
            break
        elif l.tip == 'NEED_CT':
            a = l.info
            clas[a[0]].teach[a[1]].need = False
        elif l.tip == 'NEED_T':
            teach[l.info[0]].need = False

        log.remove(l)



def check_error():
    if G.error_type == 0:
        a = G.error_info
        lbl_clas_u[a[0]][a[1]].setStyleSheet("background-color:" + color_error1)
    elif G.error_type == 1:
        a = G.error_info
        lbl_clas[a[0]].setStyleSheet("background-color:" + color_error1)
        lbl_teach[clas[a[0]].teach[a[1]].i].setStyleSheet("background-color:" + color_error1)


def fix_error():
    for i in range(len(log) - 1, -1, -1):
        l = log[i]
        log_box.takeItem(len(log) - 1)
        if l.tip == 'SET_PRIOR' or l.tip == 'SET_PRIOR_CRIT':
            a = l.info
            clas[a[0]].teach[a[1]].prior[a[2]] = a[3]

        elif l.tip == 'SET_UROK':
            a = [l.info[0], l.info[1], l.info[2]]

            G.error = False
            log.remove(log[-1])

            t = clas[a[0]].teach[a[1]]
            urok[a[0]][a[2]].teach = -1
            t.hour += 1
            teach[t.i].hour += 1
            clas[a[0]].teach[a[1]].prior_log(a[0], a[1], a[2], -117)
            lbl_clas_u[a[0]][a[2]].setText('--')
            break
        elif l.tip == 'SET_UROK_REC':
            a = l.info
            t = clas[a[0]].teach[a[1]]
            urok[a[0]][a[2]].teach = -1
            lbl_clas_u[a[0]][a[2]].setText('--')
            t.hour += 1
            teach[t.i].hour += 1

        elif l.tip == 'NEED_CT':
            a = l.info
            clas[a[0]].teach[a[1]].need = False
        elif l.tip == 'NEED_T':
            teach[l.info[0]].need = False

        log.remove(l)

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


def check_ctI():
    for i, c in enumerate(clas):
        for j, t in enumerate(c.teach):
            if t.hour > 0:
                num = 0
                for d in range(G.days):
                    if ((urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0)
                            or (urok[i][d * 2 + 1].teach < 0 and t.prior[d * 2 + 1] > 0)):
                        num += 1
                if num == t.hour and G.check == False and t.need == False:
                    t.need_log(i, j)
                    for d in range(G.days):
                        if ((urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0)
                                or (urok[i][d * 2 + 1].teach < 0 and t.prior[d * 2 + 1] > 0)):
                            if ((urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0)
                                    and (urok[i][d * 2 + 1].teach < 0 and t.prior[d * 2 + 1] > 0)):
                                t.prior_log(i, j, d * 2, t.prior[d * 2] + 500)
                                t.prior_log(i, j, d * 2 + 1, t.prior[d * 2 + 1] + 500)
                                break
                            else:
                                if (urok[i][d * 2].teach < 0 and t.prior[d * 2] > 0):
                                    G.check = True
                                    G.type_check = 'ct.hour=num'
                                    G.cI = i
                                    G.ctI = j
                                    G.les = d * 2
                                    break
                                    #return True
                                else:
                                    G.check = True
                                    G.type_check = 'ct.hour=num1'
                                    G.cI = i
                                    G.ctI = j
                                    G.les = d * 2 + 1
                                    break
                                    #return True
                elif num < t.hour:
                    G.error = True
                    G.error_type = 1
                    G.error_info[0] = i
                    G.error_info[1] = j
                    print("(!) Error 1")
                    return True

def check_tI():
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
                return True
        if t.need and G.check == False:
            for d in range(G.days * 2):
                num = 0
                if G.check == False:
                    for c in t.clas:
                        if urok[c.i][d].teach < 0 and clas[c.i].teach[c.i1].prior[d]> 0:
                            num += 1
                            G.cI = c.i
                            G.ctI = c.i1
                            G.les = d
                    if num == 1:
                        G.check = True
                        print(G.cI, G.ctI, G.les, 'NEN')
                        G.type_check = 't.need'
                        #return True


def check_solo_prior():
    J = -1
    for i, c in enumerate(clas):
        for d in range(G.days * 2):
            if urok[i][d].teach < 0:
                num = 0
                for j, t in enumerate(c.teach):
                    if t.prior[d] > 0:
                        num += 1
                        J = j
                if num == 1 and G.check == False:
                    G.check = True
                    G.type_check = 'solo prior'
                    G.cI = i
                    G.ctI = J
                    G.les = d
                    return True
                    #must_push.append(Must_push(i, G.ctI, d))
                elif num == 0:
                    print("Error 0")
                    G.error = True
                    G.error_type = 0
                    G.error_info[0] = i
                    G.error_info[1] = d
                    print(i, d)
                    return True


def check_prior():
    G.cI = -1
    G.ctI = -1
    G.les = -1
    G.check = False
    try:
        check_ctI()
        if G.error == False:
            check_tI()
        if G.error == False:
            check_solo_prior()

    except Exception as e:
        G.error = True
        print(e)
        traceback.format_exc()
        print("Беда-с")


def set_urok(cI, ctI, les, rec = False):
    print(G.type_check)
    if G.visual:
        clear_lbl()
    print(cI, ctI, les, rec, G.type_check)
    urok[cI][les].set(cI, ctI, les, rec)
    t = clas[cI].teach[ctI]
    lbl_clas_u[cI][les].setText(t.pred + str(t.i))
    lbl_teach_u[t.i][les].setText(str(clas[cI].num) + '-' + clas[cI].name)
    if G.visual:
        if rec:
            lbl_clas_u[cI][les].setStyleSheet("background-color:" + color3)
            lbl_teach_u[t.i][les].setStyleSheet("background-color:" + color3)
        else:
            lbl_clas_u[cI][les].setStyleSheet("background-color:" + color2)
            lbl_teach_u[t.i][les].setStyleSheet("background-color:" + color2)

    postcalc_prior()

def recalc_prior():
    max = 0
    for d in range(G.days * 2):
        for i, c in enumerate(clas):
            if urok[i][d].teach < 0:
                num_teach = 0
                loc_max = 0
                loc_cI = -1
                loc_ctI = -1
                loc_les = -1
                for j, t in enumerate(c.teach):
                    if t.hour > 0 and t.prior[d] > loc_max:
                        num_teach += 1
                        loc_cI = i
                        loc_ctI = j
                        loc_les = d
                        loc_max = t.prior[d]
                if loc_max / num_teach > max:
                    G.cI = loc_cI
                    G.ctI = loc_ctI
                    G.les = loc_les
                    max = loc_max / num_teach

def postcalc_prior():
    i = G.les + 1
    if G.les % 2 == 1:
        i -= 2

    t = clas[G.cI].teach[G.ctI]
    if urok[G.cI][i].teach < 0:
        for j, t1 in enumerate(clas[G.cI].teach):
            if t1.pred == t.pred:
                t1.prior_log(G.cI, j, i, -100)

    for c in teach[t.i].clas:
        if clas[c.i].teach[c.i1].prior[G.les] > 0 and urok[c.i][G.les].teach < 0:
            clas[c.i].teach[c.i1].prior_log(c.i, c.i1, G.les, -101)
        if clas[c.i].teach[c.i1].prior[i] > 0 and urok[c.i][i].teach < 0:
            clas[c.i].teach[c.i1].prior_log(c.i, c.i1, i, clas[c.i].teach[c.i1].prior[i] + 1)
    if clas[G.cI].teach[G.ctI].hour == 0:
        for d in range(G.days * 2):
            if clas[G.cI].teach[G.ctI].prior[d] > 0 and urok[G.cI][d].teach < 0:
                clas[G.cI].teach[G.ctI].prior_log(G.cI, G.ctI, d, -102)


def main_check():

    if G.check:
        info_edit[0].setText(G.type_check)
        set_urok(G.cI, G.ctI, G.les, True)
    else:
        recalc_prior()
        #tI = clas[G.cI].teach[G.ctI]
        #info_edit[2].setText("cI: " + str(G.cI) + ', ctI: ' + str(G.ctI) + ', tI: ' + str(tI) + ', les: ' + str(G.les))
        set_urok(G.cI, G.ctI, G.les)


#G.error_stop = False
#G.back = False
#G.visual = False

if G.error_stop:
    qt_run.checkBox_error_stop.setChecked(True)
if G.visual:
    qt_run.checkBox_visual.setChecked(True)

def main_script():
    try:
        num_iter = 100
        for i in range(num_iter):
            if G.run:
                G.steps_num += 1
                G.steps -= 1
                if G.error_stop:
                    # Работает в режиме исследования
                    if G.back:
                        # Откат
                        otkat()
                        G.error = False
                    else:
                        # Нормальный код по шагам
                        if G.error:
                            check_error()
                            fix_error()
                            G.run = False
                        else:
                            check_prior()
                            if G.error == False:
                                main_check()
                            else:
                                G.run = False

                else:
                    # Быстрый код
                        check_prior()
                        if G.error == False:
                            main_check()
                        else:
                            if G.visual:
                                check_error()
                            fix_error()


                if G.steps == 0:
                    G.run = False
    except Exception:
        #print(e)
        print('ТУТ')
        print(traceback.format_exc())
        G.run = False

ui.timer.timeout.connect(main_script)
ui.timer.start(0)