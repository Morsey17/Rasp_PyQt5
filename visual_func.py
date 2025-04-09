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
    """
    if G.error == False:
        for t in clas[G.cI].teach:
            lbl_teach[t.i].setStyleSheet("background-color:" + color1)
            lbl_teach_[t.i].setStyleSheet("background-color:" + color1)
            lbl_teach_[t.i].setText(str(t.prior[G.les]))
        tI = clas[G.cI].teach[G.ctI].i
        lbl_clas_u[G.cI][G.les].setStyleSheet("background-color:" + color2)
        lbl_clas_[G.cI].setStyleSheet("background-color:" + color2)
        lbl_clas[G.cI].setStyleSheet("background-color:" + color2)
        lbl_teach_u[tI][G.les].setStyleSheet("background-color:" + color2)
        lbl_teach_[tI].setStyleSheet("background-color:" + color2)
        lbl_teach[tI].setStyleSheet("background-color:" + color2)
    """
    """
    lbl_clas_u[cI_last][les_last].setStyleSheet("background-color:" + color0)
    lbl_clas_[cI_last].setStyleSheet("background-color:" + color0)
    lbl_clas[cI_last].setStyleSheet("background-color:" + color0)
    lbl_teach_u[tI_last][les_last].setStyleSheet("background-color:" + color0)
    lbl_teach_[tI_last].setStyleSheet("background-color:" + color0)
    lbl_teach[tI_last].setStyleSheet("background-color:" + color0)
    for t in teach:
        lbl_teach_[t.i].setText('')
        lbl_teach[t.i].setStyleSheet("background-color:" + color0)
        lbl_teach_[t.i].setStyleSheet("background-color:" + color0)
    for t in clas[cI].teach:
        lbl_teach[t.i].setStyleSheet("background-color:" + color1)
        lbl_teach_[t.i].setStyleSheet("background-color:" + color1)
        lbl_teach_[t.i].setText(str(t.prior[les]) + '  ' + str(t.need))


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
    """
