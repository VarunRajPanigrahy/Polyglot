import requests
import json
import gtts
from  text_to_speech import TextToSpeech
from common_words import common_words_method
from quiz_file import quiz
from language_to_code import return_code, print_lang_names
from translation_file import translate_text_to_english, translate_text_to_foreign




f=open('language_list.txt','r')
language_codes = dict()

for line in f:
    language_code = line[0:2]
    language_name = line[3:].strip()

    language_codes[language_name] = language_code


print("Welcome to language-learn!")
print(" ")
yesorno=input("Today we are going to learn a new language! To see the list of available languages, enter y else enter n: ")
if(yesorno.lower()=="y"):
    print_lang_names(language_codes)

language_full_name=input("Select the language to learn: ")

print(("The language is %s")%(language_full_name))
print(" ")
language_to_be_learnt = return_code(language_full_name,language_codes)
print("language code is %s"%(language_to_be_learnt))
print("How do you want to learn today?")
print(" ")
selector=input(("Enter 1 for translation help. Enter 2 to see the most used words translated for you. Enter 3 for a fun quiz. Enter 4 to hear %s pronunciation of  specific words: ")%(language_full_name))

if(selector=="1"):
    fine_selector=input(("Enter 0 to translate from english to %s. Enter 1 to translate from %s to english: ")%(language_full_name,language_full_name))
    if(fine_selector=="0"):
        times=int(input("Number of sentences to be translated: "))
        for i in range(times):
            text=(input(("Enter text to be translated to %s: ")%(language_full_name)))

        
            translation =translate_text_to_foreign(text,language_to_be_learnt)
            print("The translation is %s"%(translation))
            speech_object = TextToSpeech(translation,language_to_be_learnt)
            speech_object.speech()
            print(" ")
            if(i==times-1):
                print("Thanks!!")
               

    else:
        times=int(input("Number of sentences to be translated: "))
        for i in range(times):
            text=(input("Enter text to be translated to english: "))

            #language_to_be_learnt="English"
            translation =translate_text_to_english(text,language_to_be_learnt)
            print("The translation is %s"%(translation))
            speech_object = TextToSpeech(translation,"en")
            speech_object.speech()
            print(" ")
            if(i==times-1):
                print("Thanks!!")
                



if(selector=="2"):
    common_words_method(language_full_name,language_to_be_learnt)

if(selector=="3"):
    quiz(language_full_name,language_to_be_learnt)

if(selector=="4"):

    times = input("How many pronunciations do you want to hear? ")
    
    for i in range(int(times)):
        word = input(("Enter the %s word to hear its pronunciation: ")%(language_full_name))
        lang_obj = TextToSpeech(word,language_to_be_learnt)
        lang_obj.speech()
    
    
print("Thanks for using Language Learner! Hope you enjoyed the experience and most importantly, learnt something new!")



