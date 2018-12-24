import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Language-Learner'
        self.left = 500
        self.top = 100
        self.width = 600
        self.height = 600
        self.language_selected_name = "Afrikaans"
        self.combo = QComboBox(self)
        self.line = QLineEdit("Afrikaans",self)
        self.translate_button = QPushButton(('Click to translate into %s')%(self.line.text()))
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        welcome=QLabel("Welcome to Language-Learner!",self)
        welcome2=QLabel("Today we are going to learn a new language!",self)
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        self.line.adjustSize()  
        language_select = QLabel("Select the language ")
        hbox1.addWidget(language_select)

       
        f = open("language_list.txt" , "r")

        for line in f:
            language_name = line[3:].strip()
            self.combo.addItem(language_name)

        hbox1.addWidget(self.combo)
        
        
        self.language_selected_name = str(self.combo.currentText())
        self.combo.activated[str].connect(self.onActivated)

        hbox2 = QHBoxLayout()
        label3 = QLabel("The language you have selected is- ")
        hbox2.addWidget(label3)
        hbox2.addWidget(self.line)       

        
        vbox.addWidget(welcome)
        vbox.addWidget(welcome2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.translate_button)


        
        
        vbox.addStretch(1)
        self.setLayout(vbox)    

        
        
        self.show()
    def onActivated(self, text):
      
        self.line.setText(text)
        self.line.adjustSize()  
        self.translate_button.setText(('Click to translate into %s')%(self.line.text()))
       
    


    
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())