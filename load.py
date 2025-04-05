# Скрипт для распределения нагрузки для учителей и структурирования данных для начала работы главного скрипта

from base_class import *

def start():
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
                                break