import requests
import json
import contantZhAndEn

command_url='http://103.200.29.147:8888/chatGPT'

def initLanguage(language):
    global command_url
    if language=="en":
        command_url='http://103.200.29.147:8888/insructionen'
    elif language=="zh":
        command_url='http://103.200.29.147:8888/insructionzn'

def command(content):
    return chatGPT(command_url,content,10)


def chat(content):
    url = 'http://103.200.29.147:8888/chat'
    return chatGPT(url,content,60)

def ieltstest(content):
    url = 'http://103.200.29.147:8888/ieltstest'
    return chatGPT(url,content,15)

def chatGPT(url, content, time):
    d = json.dumps({"content": content})
    result = contantZhAndEn.word_sorry_i_cant_understand_this
    try:
        res = requests.post(url, data=d, timeout=time)
        result = json.loads(res.text)['result']
    except Exception as e:
        print(f"The URL {url} is not accessible. Error: {e}")
   
    return result
