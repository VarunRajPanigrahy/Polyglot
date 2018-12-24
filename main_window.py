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
        self.pronun_button = QPushButton("Switch to pronunciation section",self)
        self.pronun_button.clicked.connect(self.switch_to_pronun)
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
        

       
    

class Controller:

    def __init__(self):
        pass
    
    def show_main(self):
        self.app = App()
        self.app.switch_window.connect(self.show_translate)
       
        self.app.show()

    def show_pronunciation(self,text):
        self.pronun = Pronunciation_Window(text)
        self.pronun.show()
        

    def show_translate(self,text,direction):
        self.trans = Translation_Window(text)
        self.pronun = Pronunciation_Window(text)
        self.trans.show()
        if(direction==1):
            self.trans.close()
            self.pronun.show()
    
    
        
    
 
if __name__ == '__main__':
    app = QApplication(sys.argv)

    controller = Controller()
    controller.show_main()
    
    sys.exit(app.exec_())
