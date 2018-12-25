import random
import requests
from text_to_speech import TextToSpeech
from translation_file import translate_text_to_english,translate_text_to_foreign




def common_words_method(language_full,language):
    welcome=("Welcome to the common words section. We are going to learn the %s translation of ten most common english words")%(language_full)
    print(welcome)
    
    f=open('data.txt','r')
    random_indices=[]
    for i in range(5):
        random_indices.append(random.randint(1,3001))
    #print(f[0],f[1])
    line_number=1
    eng=[]
    esp=[]
    for line in f:
        if(line_number in random_indices):
            eng.append(line)
            tran=translate_text_to_foreign(line,language)
            esp.append(tran)
            print(line + "->" + tran )
            line_object_english = TextToSpeech(line,"en")
            line_object = TextToSpeech(tran,language)
            line_object_english.speech()
            line_object.speech()
            print(" ")
        line_number+=1

    print("Finally the words with their translations are- ")
    for i in range(len(eng)):
        print(eng[i],esp[i])

def return_common_words(lang_code):
    f=open('data.txt','r')
    random_indices=[]
    for i in range(5):
        random_indices.append(random.randint(1,3001))
    
    line_number=1
    eng_to_for = dict()

    for line in f:
        if(line_number in random_indices):
            tran = translate_text_to_foreign(line,lang_code)
            eng_to_for[line] = tran
        line_number+=1

    return eng_to_for


        


#common_words_method("spanish")