import sys
from stress import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
con = sqlite3.connect('sleepqual1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues) 

   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        pid = str(self.ui.lineEdit_9.text())
        s1 = str(self.ui.lineEdit_3.text())
        s2 = str(self.ui.lineEdit_4.text())
        s3 = str(self.ui.lineEdit_5.text())
        s4 = str(self.ui.lineEdit_6.text())	
        s5 = str(self.ui.lineEdit_2.text())
        s6 = str(self.ui.lineEdit_6.text())	
        s7 = str(self.ui.lineEdit_2.text())
        cur.execute('INSERT INTO stress VALUES(?,?,?,?,?,?,?,?)',(pid,s1,s2,s3,s4,s5,s6,s7))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


