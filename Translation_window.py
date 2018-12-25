import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from translation_file import translate_text_to_english, translate_text_to_foreign
from language_to_code import return_code , print_lang_names
import text_to_speech


class Translation_Window(QWidget):

    switch_window = QtCore.pyqtSignal()
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
        self.isEnglish = False
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.welcome_label = QLabel("Welcome to the translation section",self)
        self.vbox.addWidget(self.welcome_label)
       
        self.text_to_be_translated = QLineEdit(self)
 
        self.vbox.addWidget(self.text_to_be_translated)
        self.vbox.addStretch(1)
        

        self.translate_foreign_button = QPushButton(("Translate into %s!")%(self.foreign_language),self)
        self.translate_english_button = QPushButton(("Translate into english!"),self)
        self.translate_foreign_button.clicked.connect(self.translate_to_foreign)
        self.translate_english_button.clicked.connect(self.translate_to_english)


        self.hbox.addWidget(self.translate_foreign_button)
        self.hbox.addWidget(self.translate_english_button)
        self.vbox.addLayout(self.hbox)
        self.hbox2 = QHBoxLayout()
        self.labl2 = QLabel("The translated text is: ",self)
        self.translated_text = QLineEdit(self)
        self.hbox2.addWidget(self.labl2)
        self.hbox2.addWidget(self.translated_text)
        self.vbox.addLayout(self.hbox2)

        self.sound_button = QPushButton("Listen!",self)
        self.sound_button.clicked.connect(self.listen_to_word)
        self.vbox.addWidget(self.sound_button)
        
        self.vbox.addStretch(10)

        self.back_button = QPushButton("Back",self)
        self.hbox3 = QHBoxLayout()
        self.hbox3.addStretch(5)
        self.hbox3.addWidget(self.back_button)
        self.back_button.clicked.connect(self.switch_to_home)
        self.vbox.addLayout(self.hbox3)
        
        self.setLayout(self.vbox)

    def translate_to_foreign(self):
        txt_to_translate = self.text_to_be_translated.text()
        txt_to_be_set = translate_text_to_foreign(txt_to_translate,self.foreign_language_code)
        self.translated_text.setText(txt_to_be_set)
    def translate_to_english(self):
        txt_to_translate = self.text_to_be_translated.text()
        txt_to_be_set = translate_text_to_english(txt_to_translate,self.foreign_language_code)
        self.translated_text.setText(txt_to_be_set)
        self.isEnglish = True
    def listen_to_word(self):
        lang = self.foreign_language_code
        if(self.isEnglish):
            lang = "en"
        speech_object = text_to_speech.TextToSpeech(self.translated_text.text(),lang)
        speech_object.speech()

    def switch_to_home(self):
        self.switch_window.emit()