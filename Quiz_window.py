import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from translation_file import translate_text_to_english, translate_text_to_foreign
from language_to_code import return_code , print_lang_names
import text_to_speech
from quiz_file import return_questions


class Quiz_Window_English(QWidget):

    switch_window = QtCore.pyqtSignal(int)
    def __init__(self, text):
        QWidget.__init__(self)
        self.setWindowTitle('Translation window')
        self.left = 1100
        self.top = 100
        self.width = 600
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.foreign_language = text
        self.foreign_language_code = return_code(self.foreign_language)
        self.questions = return_questions(self.foreign_language_code)
        self.vbox = QVBoxLayout()
        self.labl1 = QLabel("Welcome to the quiz section.",self)
        self.labl2 = QLabel(("Translate the first five sentences from %s to english . ")%(self.foreign_language),self)
        self.labl3 = QLabel(("Translate the next five sentences from english to %s.")%(self.foreign_language),self)
        self.vbox.addWidget(self.labl1)
        self.vbox.addWidget(self.labl2)
        self.vbox.addWidget(self.labl3)
        self.setLayout(self.vbox)
        self.keys = list(self.questions.keys())
        self.values = list(self.questions.values())
        print(len(self.values),len(self.keys))
        self.score = 0
        
        self.vbox.addStretch(3)

        self.hbox1 = QHBoxLayout()
        self.ques1 = QLabel(self.keys[0],self)
        self.ans1 = QLineEdit(self)
        self.hbox1.addWidget(self.ques1)
        self.hbox1.addWidget(self.ans1)
        self.vbox.addLayout(self.hbox1)

        self.vbox.addStretch(2)
        
        self.hbox2 = QHBoxLayout()
        self.ques2 = QLabel(self.keys[1],self)
        self.ans2 = QLineEdit(self)
        self.hbox2.addWidget(self.ques2)
        self.hbox2.addWidget(self.ans2)
        self.vbox.addLayout(self.hbox2)

        self.vbox.addStretch(2)
        

        self.hbox3 = QHBoxLayout()
        self.ques3 = QLabel(self.keys[2],self)
        self.ans3 = QLineEdit(self)
        self.hbox3.addWidget(self.ques3)
        self.hbox3.addWidget(self.ans3)
        self.vbox.addLayout(self.hbox3)

        self.vbox.addStretch(2)
        

        self.hbox4 = QHBoxLayout()
        self.ques4 = QLabel(self.keys[3],self)
        self.ans4 = QLineEdit(self)
        self.hbox4.addWidget(self.ques4)
        self.hbox4.addWidget(self.ans4)
        self.vbox.addLayout(self.hbox4)

        self.vbox.addStretch(2)
        

        self.hbox5 = QHBoxLayout()
        self.ques5 = QLabel(self.keys[4],self)
        self.ans5 = QLineEdit(self)
        self.hbox5.addWidget(self.ques5)
        self.hbox5.addWidget(self.ans5)
        self.vbox.addLayout(self.hbox5)

        self.vbox.addStretch(2)


        self.hbox6 = QHBoxLayout()
        self.ques6 = QLabel(self.values[5],self)
        self.ans6 = QLineEdit(self)
        self.hbox6.addWidget(self.ques6)
        self.hbox6.addWidget(self.ans6)
        self.vbox.addLayout(self.hbox6)

        self.vbox.addStretch(2)

        self.hbox7 = QHBoxLayout()
        self.ques7 = QLabel(self.values[6],self)
        self.ans7 = QLineEdit(self)
        self.hbox7.addWidget(self.ques7)
        self.hbox7.addWidget(self.ans7)
        self.vbox.addLayout(self.hbox7)

        self.vbox.addStretch(2)

        self.hbox8 = QHBoxLayout()
        self.ques8 = QLabel(self.values[7],self)
        self.ans8 = QLineEdit(self)
        self.hbox8.addWidget(self.ques8)
        self.hbox8.addWidget(self.ans8)
        self.vbox.addLayout(self.hbox8)

        self.vbox.addStretch(2)

        self.hbox9 = QHBoxLayout()
        self.ques9 = QLabel(self.values[8],self)
        self.ans9 = QLineEdit(self)
        self.hbox9.addWidget(self.ques9)
        self.hbox9.addWidget(self.ans9)
        self.vbox.addLayout(self.hbox9)

        self.vbox.addStretch(2)

        self.hbox0 = QHBoxLayout()
        self.ques0 = QLabel(self.values[9],self)
        self.ans0 = QLineEdit(self)
        self.hbox0.addWidget(self.ques0)
        self.hbox0.addWidget(self.ans0)
        self.vbox.addLayout(self.hbox0)

        self.vbox.addStretch(2)
        
        self.score_box = QLineEdit("Your score is",self)
        
        self.vbox.addWidget(self.score_box)
        
        

        self.next = QPushButton("Next!",self)
        self.next.clicked.connect(self.check)
        self.vbox.addWidget(self.next)
        self.vbox.addStretch(6)


    def check(self):
        self.score = 0
        if((self.ans1.text()).lower().strip() == (self.values[0]).lower().strip()): self.score+=1
        if((self.ans2.text()).lower().strip() == (self.values[1]).lower().strip()): self.score+=1
        if((self.ans3.text()).lower().strip() == (self.values[2]).lower().strip()): self.score+=1
        if((self.ans4.text()).lower().strip() == (self.values[3]).lower().strip()): self.score+=1
        if((self.ans5.text()).lower().strip() == (self.values[4]).lower().strip()): self.score+=1

        if((self.ans6.text()).lower().strip() == (self.keys[5]).lower().strip()): self.score+=1
        if((self.ans7.text()).lower().strip() == (self.keys[6]).lower().strip()): self.score+=1
        if((self.ans8.text()).lower().strip() == (self.keys[7]).lower().strip()): self.score+=1
        if((self.ans9.text()).lower().strip() == (self.keys[8]).lower().strip()): self.score+=1
        if((self.ans0.text()).lower().strip() == (self.keys[9]).lower().strip()): self.score+=1

        self.score_box.setText("Your score is %d"%(self.score))

        

       






        