import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from translation_file import translate_text_to_english, translate_text_to_foreign
from language_to_code import return_code , print_lang_names
import text_to_speech
from common_words import return_common_words


class Common_Window(QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, text):
        QWidget.__init__(self)
        self.setWindowTitle('Common Words Window')
        self.left = 1100
        self.top = 100
        self.width = 600
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.foreign_language = text
        self.foreign_language_code = return_code(self.foreign_language)
        self.input_dict = return_common_words(self.foreign_language_code)
        self.keys = []
        self.values = []
        for i in self.input_dict:
            self.keys.append(i)
            self.values.append(self.input_dict[i])
        self.vbox2 = QVBoxLayout()
        self.count = 0

        self.hbox0 = QHBoxLayout()
        self.english_0 = QPushButton(self.keys[0],self)
        self.foreign_0 = QPushButton(self.values[0],self)
        self.hbox0.addWidget(self.english_0)
        self.hbox0.addWidget(self.foreign_0)
        self.vbox2.addLayout(self.hbox0)
        self.english_0.clicked.connect(self.pronun_in_eng0)
        self.foreign_0.clicked.connect(self.pronun_in_for0)


        self.hbox1 = QHBoxLayout()
        self.english_1 = QPushButton(self.keys[1],self)
        self.foreign_1 = QPushButton(self.values[1],self)
        self.hbox1.addWidget(self.english_1)
        self.hbox1.addWidget(self.foreign_1)
        self.vbox2.addLayout(self.hbox1)
        self.english_1.clicked.connect(self.pronun_in_eng1)
        self.foreign_1.clicked.connect(self.pronun_in_for1)

        self.hbox2 = QHBoxLayout()
        self.english_2 = QPushButton(self.keys[2],self)
        self.foreign_2 = QPushButton(self.values[2],self)
        self.hbox2.addWidget(self.english_2)
        self.hbox2.addWidget(self.foreign_2)
        self.vbox2.addLayout(self.hbox2)
        self.english_2.clicked.connect(self.pronun_in_eng2)
        self.foreign_2.clicked.connect(self.pronun_in_for2)

        self.hbox3 = QHBoxLayout()
        self.english_3 = QPushButton(self.keys[3],self)
        self.foreign_3 = QPushButton(self.values[3],self)
        self.hbox3.addWidget(self.english_3)
        self.hbox3.addWidget(self.foreign_3)
        self.vbox2.addLayout(self.hbox3)
        self.english_3.clicked.connect(self.pronun_in_eng3)
        self.foreign_3.clicked.connect(self.pronun_in_for3)

        self.hbox4 = QHBoxLayout()
        self.english_4 = QPushButton(self.keys[4],self)
        self.foreign_4 = QPushButton(self.values[4],self)
        self.hbox4.addWidget(self.english_4)
        self.hbox4.addWidget(self.foreign_4)
        self.vbox2.addLayout(self.hbox4)
        self.english_4.clicked.connect(self.pronun_in_eng4)
        self.foreign_4.clicked.connect(self.pronun_in_for4)

       
        
        
        
        self.setLayout(self.vbox2)



    def pronun_in_eng0(self):
        
        speech_object = text_to_speech.TextToSpeech(self.english_0.text(),"en")
        speech_object.speech()

    def pronun_in_for0(self):
        
        lang = self.foreign_language_code
        speech_object = text_to_speech.TextToSpeech(self.foreign_0.text(),lang)
        speech_object.speech()

    def pronun_in_eng1(self):
        
        speech_object = text_to_speech.TextToSpeech(self.english_1.text(),"en")
        speech_object.speech()

    def pronun_in_for1(self):
        
        lang = self.foreign_language_code
        speech_object = text_to_speech.TextToSpeech(self.foreign_1.text(),lang)
        speech_object.speech()

    def pronun_in_eng2(self):
        
        speech_object = text_to_speech.TextToSpeech(self.english_2.text(),"en")
        speech_object.speech()

    def pronun_in_for2(self):
        
        lang = self.foreign_language_code
        speech_object = text_to_speech.TextToSpeech(self.foreign_2.text(),lang)
        speech_object.speech()

    def pronun_in_eng3(self):
        
        speech_object = text_to_speech.TextToSpeech(self.english_3.text(),"en")
        speech_object.speech()

    def pronun_in_for3(self):
        
        lang = self.foreign_language_code
        speech_object = text_to_speech.TextToSpeech(self.foreign_3.text(),lang)
        speech_object.speech()

    def pronun_in_eng4(self):
        
        speech_object = text_to_speech.TextToSpeech(self.english_4.text(),"en")
        speech_object.speech()

    def pronun_in_for4(self):
        
        lang = self.foreign_language_code
        speech_object = text_to_speech.TextToSpeech(self.foreign_4.text(),lang)
        speech_object.speech()