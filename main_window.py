import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from translation_file import translate_text_to_english, translate_text_to_foreign
from language_to_code import return_code , print_lang_names
import text_to_speech
 
class App(QWidget):
    
    switch_window = QtCore.pyqtSignal(str,int)
 
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
        self.translate_button.clicked.connect(self.switch_to_translate)

        self.pronun_button = QPushButton("Go to pronunciation section! ",self)
        self.pronun_button.clicked.connect(self.switch_to_pronun)
        self.common_button = QPushButton("Go to common words section! ",self)
        self.common_button.clicked.connect(self.switch_to_common)
        self.quiz_button = QPushButton("Go to the Quiz section!",self)
        self.quiz_button.clicked.connect(self.switch_to_quiz)


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

        vbox.addWidget(self.pronun_button)

        vbox.addWidget(self.common_button)
        vbox.addWidget(self.quiz_button)

        
        

        vbox.addStretch(1)
        self.setLayout(vbox)    

        
        
        self.show()
    def onActivated(self, text):
      
        self.line.setText(text)
        self.line.adjustSize()  
        self.translate_button.setText(('Click to translate into %s')%(self.line.text()))

    def switch_to_translate(self):
        
        self.switch_window.emit(self.line.text(),0)

    def switch_to_pronun(self):
       
        self.switch_window.emit(self.line.text(),1)


    def switch_to_common(self):
        self.switch_window.emit(self.line.text(),2)

    def switch_to_quiz(self):
        self.switch_window.emit(self.line.text(),3)
    








        
    


