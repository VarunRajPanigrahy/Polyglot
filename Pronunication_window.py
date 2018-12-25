import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from translation_file import translate_text_to_english, translate_text_to_foreign
from language_to_code import return_code , print_lang_names
import text_to_speech

class Pronunciation_Window(QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, text):
        QWidget.__init__(self)
        self.setWindowTitle('Pronunciation window')
        self.left = 1100
        self.top = 100
        self.width = 600
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.foreign_language = text
        self.foreign_language_code = return_code(self.foreign_language)
       
        self.vbox1 = QVBoxLayout()
        
        self.welcome_labl = QLabel("Welcome to the pronunciation section! ",self)
        self.vbox1.addWidget(self.welcome_labl)
       
        self.labl = QLabel(("Enter text to listen to %s pronunciation")%(self.foreign_language))
        self.input = QLineEdit(self)
        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(self.labl)
        self.hbox4.addWidget(self.input)
        self.vbox1.addLayout(self.hbox4)

        self.listen_button = QPushButton(("Listen in %s")%(self.foreign_language),self)
        self.listen_button.clicked.connect(self.pronunciation)
        self.vbox1.addWidget(self.listen_button)
        self.vbox1.addStretch(5)
        self.setLayout(self.vbox1)

    def pronunciation(self):
        lang = self.foreign_language_code
        speech_object = text_to_speech.TextToSpeech(self.input.text(),lang)
        speech_object.speech()