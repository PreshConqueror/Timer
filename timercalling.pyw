#CALLING SOURCE CODE

#IMPORT FROM PYQT5
import sys 
from timer import * 
from PyQt5.QtWidgets import * 
 
           
class MyForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
       
    # create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
ui_dialog = Ui_Dialog()
  
# start the app
sys.exit(App.exec())
