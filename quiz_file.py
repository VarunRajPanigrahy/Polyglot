import random
import requests
from translation_file import translate_text_to_english,translate_text_to_foreign
#from translate import translate_text




def quiz(language_full,language):
    print("Welcome to the quiz section. You will be asked 10 questions.")
    print(("Translate the first five words from %s to english.   Translate the next five words from english to %s")%(language_full,language_full))
    score=0
    question=1
    random_indices=[]
    for i in range(10):
        random_indices.append(random.randint(1,3001))
    eng=[]
    esp=[]
    f=open('data.txt','r')
    line_number=1
    for line in f:
        if(line_number in random_indices):
            eng.append(line)
            esp.append(translate_text_to_foreign(line,language))
        line_number+=1
    #print(len(eng))
    for i in range(5):
        print(esp[i])
        ans=input("What is its english translation? ")
        if(eng[i].lower().strip()==ans.lower().strip()):
            print("Thats right!! Well done")
            score+=1
        else:
            print("Sorry thats the wrong answer.")
            print("The right answer is %s"%(eng[i]))

    for i in range(5,10):
        print(eng[i])
        ans=input("What its spanish translation? ")
        if(esp[i].lower().strip()==ans.lower().strip()):
            print("Thats right!! Well done")
            score+=1
        else:
            print("Sorry thats the wrong answer.")
            print("The right answer is %s"%(esp[i]))

    if(score>=8): print("Well done!! You scored %d out of 10 which is outstanding!!"%(score))
    elif(score>=5):print("Well done. You scored %d out of 10 which is average.Practice makes a man perfect."%(score))
    else: print("You scored %d out of 10.Although you have lots to learn dont lose hope. Rome wasnt built in a day!"%(score))



def return_questions(lang):
    random_indices=[]
    for i in range(10):
        random_indices.append(random.randint(1,3001))
    eng_to_for = dict()
    f=open('data.txt','r')
    line_number=1
    for line in f:
        if(line_number in random_indices):
            eng_to_for[line] = translate_text_to_foreign(line,lang)
          
        line_number+=1
    return eng_to_for
