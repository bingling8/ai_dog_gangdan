#!/usr/bin/env/python3
# File name   : translate.py
# Description : translate interfaces.
import requests
import json

bookRecommend_url = "http://103.200.29.147:6689/"

def health_check():
    global bookRecommend_url
    try:
        response = requests.get(bookRecommend_url)
        if response.status_code == 200:
            print('translate service is up')
            return response
        else:
            print(f"The URL {bookRecommend_url} is accessible but returns a status code {response.status_code}.")
            return None
    except requests.RequestException as e:
        print('translate service is down')
        return None


def translate(content):
    params = {'content': content}
    print(params)
    chatgpt_url="http://103.200.29.147:6689/chatGPT"
    response = requests.post(chatgpt_url, json=params) 
    if response.status_code == 200:
        print(response.text)
        return json.loads(response.text)['result']
    return "no content"


if __name__ == '__main__':
    print(translate("英文转中文翻译。J.K. Rowling"))
