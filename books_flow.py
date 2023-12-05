import time
import sys
sys.path.append('./ImagesRecognition')
import client
import common
import params
import robot
import VoiceSdk
import vadSound
import contantZhAndEn
import json
import status
from book import *
from face import *


def process_borrow_return_respone(book_type, respone):
    json_respone = respone
    if json_respone["is_success"] == "True":
        if VoiceSdk.text2sound(contantZhAndEn.word_book_flow_success):
            print(contantZhAndEn.word_book_flow_success)
            vadSound.play_sound()
    else:
        if VoiceSdk.text2sound(contantZhAndEn.word_book_flow_fail):
            print(contantZhAndEn.word_book_flow_fail)
            vadSound.play_sound()
        error_message = json_respone["error_message"]
        print(f"借还书图书流程有问题， 请检查错误, 错误信息如下: \n{error_message}")


def get_borrow_return_book_name():
    language = status.getLanguage()
    if language == 'zh':
        result = "或者".join([ i for i in client.classify_book_image()])
    else:
        result = " or ".join(BookTool().zh_to_en([ i for i in client.classify_book_image()]))
    return result
    

def borrow_return_flow(book_type):
    book = get_borrow_return_book_name()
    #询问是否分类准确
    if VoiceSdk.text2sound(contantZhAndEn.word_book_is.format(book)):
        print(contantZhAndEn.word_book_is.format(book))
        vadSound.play_sound()
        if vadSound.record_sound():
            ret, content = VoiceSdk.sound2text()
            content = content.replace('。', '')
            print(f'borrow flow: {content}')
            #如果识别错误
            if content == contantZhAndEn.word_recongnition_false or content == contantZhAndEn.word_recongnition_false_2:
                print("图书识别错误！")
                #询问正确分类
                if VoiceSdk.text2sound(contantZhAndEn.word_book_true_is):
                    print(contantZhAndEn.word_book_true_is)
                    vadSound.play_sound()
                    if vadSound.record_sound():
                        ret, content = VoiceSdk.sound2text()
                        content = content.replace('。', '')
                        print(f'{book_type} flow user say correct book name: {content}')
                        if VoiceSdk.text2sound(contantZhAndEn.word_book_people_capture):
                            print(contantZhAndEn.word_book_people_capture)
                            vadSound.play_sound()
                        #返回用户说的书名
                        respone = client.flow_borrow_return_book(book_type, content)
                        process_borrow_return_respone(book_type, respone)
                        
            else:
                print("图书识别正确！")
                if VoiceSdk.text2sound(contantZhAndEn.word_book_people_capture):
                    print(contantZhAndEn.word_book_people_capture)
                    vadSound.play_sound()
                #返回用户说的书名
                respone = client.flow_borrow_return_book(book_type, book)
                process_borrow_return_respone(book_type, respone)
                    


def add_flow():
    if VoiceSdk.text2sound(contantZhAndEn.word_book_add_request_two):
        print(contantZhAndEn.word_book_add_request_two)
        vadSound.play_sound()
        if vadSound.record_sound():
            ret, content = VoiceSdk.sound2text()
            isbn = content.replace('。', '')
            print(f'isbn : {content}')
            if VoiceSdk.text2sound(contantZhAndEn.word_book_add_request):
                print(contantZhAndEn.word_book_add_request)
                vadSound.play_sound()
                respone = client.flow_add_book(isbn=isbn)
                print(f'flow message: {respone}')
                if VoiceSdk.text2sound(contantZhAndEn.word_book_flow_success):
                    print(contantZhAndEn.word_book_flow_success)
                    vadSound.play_sound()
                json_respone = respone
                if json_respone["is_success"] == "True":
                    if VoiceSdk.text2sound(contantZhAndEn.word_book_flow_success):
                        print(contantZhAndEn.word_book_flow_success)
                        vadSound.play_sound()
                else:
                    if VoiceSdk.text2sound(contantZhAndEn.word_book_flow_fail):
                            print(contantZhAndEn.word_book_flow_fail)
                            vadSound.play_sound()
                    error_message = json_respone["error_message"]
                    print(f"添加图书流程有问题， 请检查错误, 错误信息如下: \n{error_message}")
            

def classfiy_book_flow():
    book = get_borrow_return_book_name()
    if VoiceSdk.text2sound(contantZhAndEn.word_book_recognition.format(book)):
        print(contantZhAndEn.word_book_recognition.format(book))
        vadSound.play_sound()


def get_face_names():
    language = status.getLanguage()
    if language == 'zh':
        result = ", ".join([ i for i in client.classify_people_image()])
    else:
        result = ", ".join(FaceTool().zh_to_pinyin([ i for i in client.classify_people_image()]))
    return result
    

def classfiy_face_flow():
    people = get_face_names()
    if people != '':
        if VoiceSdk.text2sound(contantZhAndEn.word_face_recogniton.format(people)):
            print(contantZhAndEn.word_face_recogniton.format(people))
            vadSound.play_sound()
    else:
        if VoiceSdk.text2sound(contantZhAndEn.word_face_recogniton_failed):
            vadSound.play_sound()


def flow_books(book_type):
    if book_type == 'return' or book_type == 'borrow':
        borrow_return_flow(book_type)
    elif book_type == 'add':
        add_flow()
    elif book_type == 'classify':
        classfiy_book_flow()
    
    
def flow_faces(face_type):
    if face_type == 'classify':
        classfiy_face_flow()


