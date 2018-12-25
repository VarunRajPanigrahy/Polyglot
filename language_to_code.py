


def return_code(lang_name):
        language_name_full=lang_name.lower()
        f=open('language_list.txt','r')
        language_codes = dict()
        #print(language_name_full)
        for line in f:
                language_code = (line[0:2]).lower()
                language_name = (line[3:].strip()).lower()

                language_codes[language_name] = language_code

        
        if(language_name_full in language_codes):
                return language_codes[language_name_full]

        return "es"


def print_lang_names(lang_codes):
    
    for language in lang_codes.keys():
        print(language)

#print_lang_names(language_codes)
#print(return_code("Afrikaans"))
