import requests
import sys
import camera_api
# import opencv_client_api

_BASE_URL = 'http://101.34.206.191:9898/'
# _BASE_URL = 'http://127.0.0.1:9898/'


def classify_book_image(file_path=None):
    # classify_books
    url = f'{_BASE_URL}classify_book'  # 服务端的URL
    # print(url)
    if file_path is None:
        file = open(camera_api.capturePhoto(), 'rb')
    else:
        file = open(file_path, 'rb')
    # 构建请求数据
    files = {'image': file}
    # 发送请求
    response = requests.post(url, files=files)
    # 解析响应数据
    result = response.json()

    return result

def classify_people_image(file_path=None):
    # classify_books
    url = f'{_BASE_URL}classify_people'  # 服务端的URL
    # print(url)
    # file = open(file_path, 'rb')
    if file_path is None:
        file = open(camera_api.capturePhoto(), 'rb')
    else:
        file = open(file_path, 'rb')
    # 构建请求数据
    files = {'image': file}
    # 发送请求
    response = requests.post(url, files=files)
    # 解析响应数据
    result = response.json()

    return result

if __name__ == '__main__':
    # file_path = sys.argv[1]
    book_path = './opencv/test_books/book_7_2.jpg'
    people_path = './opencv/test_people/tnxlbt_0.jpg'
    #print(classify_book_image())
    print(classify_people_image())

