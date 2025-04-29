from qt_run import *


def clear_lbl():
    for i in range(len(lbl_clas)):
        indicator_lbl_clas[i] = 0
        lbl_clas[i].setStyleSheet("background-color:" + color0)
        lbl_clas_[i].setText("")
        lbl_clas_[i].setStyleSheet("background-color:" + color0)
        for j in range(len(indicator_lbl_clas_u[i])):
            indicator_lbl_clas_u[i][j] = 0
            lbl_clas_u[i][j].setStyleSheet("background-color:" + color0)
    for i in range(len(lbl_teach)):
        lbl_teach[i].setStyleSheet("background-color:" + color0)
        lbl_teach_[i].setText(" ")
        lbl_teach_[i].setStyleSheet("background-color:" + color0)
        for j in range(len(indicator_lbl_teach_u[i])):
            indicator_lbl_teach_u[i][j] = 0
            lbl_teach_u[i][j].setStyleSheet("background-color:" + color0)



def check_error():
    if (G.error_type == 0):
        i1 = G.error_info[0]
        i2 = G.error_info[1]
        lbl_clas_u[i1][i2].setStyleSheet("background-color:" + color_error1)
        for t in clas[i1].teach:
            lbl_teach[t.i].setStyleSheet("background-color:" + color_error1)

def set_color():
    clear_lbl()