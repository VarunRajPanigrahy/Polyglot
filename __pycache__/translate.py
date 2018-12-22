import requests

def translate_text(text,language):

    key="trnsl.1.1.20181220T181821Z.a672b052bee36df0.0e3e2018f7fde9d7889b3d46e0162ab18744f91f"
    lang="en-es"
    Format="plain"
    webpage=("https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&text=%s&lang=%s")%(key,text,lang)
    response = requests.get(webpage)
    data=response.json()
    translation=data["text"][0]
    return translation