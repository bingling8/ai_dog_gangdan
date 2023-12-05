#!/usr/bin/env/python3
# File name   : bookRecommendation.py
# Description : book Recommendation interfaces.
import requests

bookRecommend_url = "http://103.200.29.147:6688/"

def health_check():
    global bookRecommend_url
    try:
        response = requests.get(bookRecommend_url)
        if response.status_code == 200:
            print('book recommendation service is up')
            return response
        else:
            print(f"The URL {url} is accessible but returns a status code {response.status_code}.")
            return None
    except requests.RequestException as e:
        print('book recommendation service is down')
        return None

def check_url(url, params):
    try:
        response = requests.get(url, params)
        if response.status_code == 200:
            return response
        else:
            print(f"The URL {url} is accessible but returns a status code {response.status_code}.")
            return None
    except requests.RequestException as e:
        print(f"The URL {url} is not accessible. Error: {e}")
        

def get_recommendation(query):
    params = {'query': query}
    print(params)
    bookRecommend_url="http://103.200.29.147:6688/recommendation"
    response = requests.post(bookRecommend_url, json=params) 
    if response.status_code == 200:
        parsed_data = response.json()
        return parsed_data["message"]
    return "no content"


def get_next_recommendation():
    bookRecommend_url="http://103.200.29.147:6688/next_recommendation"
    response = check_url(bookRecommend_url, None)
    if response:
        parsed_data = response.json()
        return parsed_data["message"]
    return "no content"

if __name__ == '__main__':
    print(health_check())
    print(get_recommendation("J.K. Rowling"))
    print(get_next_recommendation())
