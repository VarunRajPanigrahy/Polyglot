import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from translation_file import translate_text_to_english, translate_text_to_foreign
from language_to_code import return_code , print_lang_names
import text_to_speech
from  main_window import App
from Pronunication_window import Pronunciation_Window
from Translation_window import Translation_Window
from Common_words_window import Common_Window
from Quiz_window import Quiz_Window_English


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
        self.common = Common_Window(text)
        self.quizeng = Quiz_Window_English(text)
        self.trans.show()
        if(direction == 1):
            self.trans.close()
            self.pronun.show()

        elif(direction == 2):
            self.trans.close()
            self.common.show()

        elif(direction == 3):
            self.trans.close()
            self.quizeng.show()
           
    
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    controller = Controller()
    controller.show_main()
    
    sys.exit(app.exec_())