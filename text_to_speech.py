from gtts import gTTS
import os

class TextToSpeech:

    def __init__(self,text,language):
        self.text=text
        self.language=language
    def speech(self):
        text_to_be_translated=self.text
        lang_code=self.language
        
        tts = gTTS(text=text_to_be_translated, lang=lang_code)
        tts.save("good.mp3")
        os.system("play good.mp3 ")
        os.system("rm good.mp3")
    


