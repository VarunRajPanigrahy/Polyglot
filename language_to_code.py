f=open('language_list.txt','r')
language_codes = dict()

for line in f:
    language_code = (line[0:2]).lower()
    language_name = (line[3:].strip()).lower()

    language_codes[language_name] = language_code



def return_code(lang_name,lang_codes):
    if(lang_name in language_codes):
        return language_codes[lang_name]

    return "es"


def print_lang_names(lang_codes):
    
    for language in lang_codes.keys():
        print(language)

#print_lang_names(language_codes)
