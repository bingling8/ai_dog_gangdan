# coding=utf-8
import time
import sys
sys.path.append('./ImagesRecognition')
import requests
import json
import VoiceSdk
import client
import common
import params
import vadSound
import robot
import status
import time
import weather
import psutil
import multiprocessing
import obstacle_avoidance
import contantZhAndEn
import bookRecommendation
import translate
import chatGPT
import books_flow
import os


# def tuling(text='I said nothing'):
#     # tuling Robot
#     tuling_url = 'http://www.tuling123.com/openapi/api'
#     tuling_date = {
#         'key': '4527c40***********92cf020847be',
#         'info': text
#     }  # 当你申请了自己的图灵机器人后，请将key换为你自己的
#     r = requests.post(tuling_url, data=tuling_date)
#     # print(r.text)
#     return json.loads(r.text)['text']


def chat(event,language):
    vadSound.end_point_detection_factor_init(0.9,10,248)
    mode="chat"
    
    no_time = 0
    
    initLanguage(language)
    processAndStatus=status.getProcessStatus().split('-')
    print(processAndStatus[1])
    if processAndStatus[1].strip() == "1":
        mode=processAndStatus[0]
        mode_name=contantZhAndEn.word_chatting
        if mode=="command":
            mode_name=contantZhAndEn.word_listen_to_instructions
        elif mode=="chat":
            mode_name=contantZhAndEn.word_chatting
        elif mode=="IELTS":
            mode_name=contantZhAndEn.word_learn_english
        else :
            mode="chat"
        
        if VoiceSdk.text2sound(contantZhAndEn.word_exception_restarted.format(mode_name)):
            vadSound.play_sound()
        status.setProcessStatus(mode,'1')
        status.write1()
    else:
        status.write2()
        status.setProcessStatus("hello",'1')
        print('say :' +str(contantZhAndEn.word_hello))    
        if VoiceSdk.text2sound(contantZhAndEn.word_hello):
            vadSound.play_sound()
        status.write1()   
        
       
    #robot.handShake()   
    

    while True:
        if event.is_set() and no_time >= 4:
            break
        if vadSound.record_sound():
            print('语音识别中。。。')
            ret, content = VoiceSdk.sound2text()
            # people = client.classify_people_image()['face_recognition_label_result']
            print(ret)
            print('you say:'+str(content))
        elif event.is_set():
            break
        else:
            continue

        if not content:
            print('not content')
            no_time += 1
            status.write1()
            continue
        if ret:
            print(mode)
            status.write2()
            content = content.replace('。', '').replace('?','').replace('？', '')
            vadSound.end_point_detection_factor_init(0.9,30,248)
            if content == contantZhAndEn.word_listen_to_instructions:
                mode="command"
                status.setProcessStatus(mode,'1')
                if VoiceSdk.text2sound(contantZhAndEn.word_please_speaking):
                    print('机器人：请讲')
                    vadSound.play_sound()
            elif content == contantZhAndEn.word_chatting:
                mode="chat"
                status.setProcessStatus(mode,'1')
                if VoiceSdk.text2sound(contantZhAndEn.word_gangdan_likes_chatting_the_most):
                    print('机器人：钢蛋最喜欢唠嗑了')
                    vadSound.play_sound()
            elif content == contantZhAndEn.word_learn_english:
                mode="IELTS"
                vadSound.end_point_detection_factor_init(2.0,60,2000) 
                status.setProcessStatus(mode,'1')
                initLanguage("en")
                if VoiceSdk.text2sound(contantZhAndEn.word_i_will_talk_to_you_as_interview):
                    print('机器人：学英语')
                    vadSound.play_sound()
            elif '再见' in content or '拜拜' in content or 'see you' in content or 'bye bye' in content or 'goodbye' in content:
                if VoiceSdk.text2sound(contantZhAndEn.word_goodbye):
                    vadSound.play_sound()
                print('机器人：再见。')
                status.setProcessStatus(mode,'0')
                break
            elif mode=="command":
                status.setProcessStatus(mode,'1')
                if not command(content,language):
                    if not command(chatGPT.command(content),language):
                        if VoiceSdk.text2sound(contantZhAndEn.word_sorry_i_cant_understand):
                            vadSound.play_sound()
                        print('机器人：我现在听不懂哦。')        
            elif mode=="chat":
                status.setProcessStatus(mode,'1')
                res=chatGPT.chat(content)
                print(res)
                if VoiceSdk.text2sound(res):
                    #vadSound.play_sound()
                    os.system("python3 playSound.py")
                print(f'机器人：{res}')
            elif mode=="IELTS":
                status.setProcessStatus(mode,'1')
                vadSound.end_point_detection_factor_init(2.0,60,2000)           
                res=chatGPT.ieltstest(content)
                if VoiceSdk.text2sound(res):
                    vadSound.play_sound()
                    print(f'机器人：{res}')   
            
            
            no_time = 0
            status.write1()
            status.setProcessStatus(mode,'0')
        else:
            VoiceSdk.text2sound(contantZhAndEn.word_speech_recognition_error)
            vadSound.play_sound()
            print('机器人：语音识别出错[{}]'.format(content))
            no_time += 1
            status.write1()
            continue

        

        
    return


def initLanguage(language):
    print('language :' +str(language))
    contantZhAndEn.initLanguage(language)
    VoiceSdk.initLanguage(language)
    chatGPT.initLanguage(language)
    status.setLanguage(language)

def command(content,language):
    
    print('command:'+content+chatGPT.command_url)
    isGot=True
    if content == contantZhAndEn.word_please_switch_to_english:
        print('你说：' + content)
        initLanguage("en")
        if VoiceSdk.text2sound(contantZhAndEn.word_okay):
            vadSound.play_sound()
    elif content == contantZhAndEn.word_please_switch_to_chinese:
        print('你说：' + content)
        initLanguage("zh")
        if VoiceSdk.text2sound(contantZhAndEn.word_okay):
            vadSound.play_sound()
    elif content == contantZhAndEn.word_take_a_break:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_i_sat_down):
            print('机器人：我坐下了')
            vadSound.play_sound()
            robot.rest()
    elif content == contantZhAndEn.word_wnder_around:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_automatic_obstacle_avoidance):
            print('自动避障')
            vadSound.play_sound()
            status.startOA()
            car = multiprocessing.Process(target=obstacle_avoidance.start, args=())
            car.daemon = True
            car.start()
            print('moving...')
    elif content == contantZhAndEn.word_stop:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_okay):
            status.stopOA()
            vadSound.play_sound()
    # 人脸识别
    elif content == contantZhAndEn.word_face_recongnition:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_request_face_recongnition):
            print(contantZhAndEn.word_request_face_recongnition)
            vadSound.play_sound()
            books_flow.flow_faces('classify')
            print('start faces classify daemon...')
    #图书识别
    elif content == contantZhAndEn.word_book_recongnition:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_request_book_recongnition):
            print(contantZhAndEn.word_request_book_recongnition)
            vadSound.play_sound()
            books_flow.flow_books('classify')
            print('start books classify daemon...')
    #借书
    elif content == contantZhAndEn.word_borrow_book_recongnition:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_request_book_recongnition):
            print(contantZhAndEn.word_request_book_recongnition)
            vadSound.play_sound()
            books_flow.flow_books('borrow')
            #book_flow = multiprocessing.Process(target=books_flow.flow_books, args=('borrow',))
            #book_flow.daemon = True
            #book_flow.start()
            print('start books borrow daemon...')
    #还书
    elif content == contantZhAndEn.word_return_book_recongnition:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_request_book_recongnition):
            print(contantZhAndEn.word_request_book_recongnition)
            vadSound.play_sound()
            books_flow.flow_books('return')
            #book_flow = multiprocessing.Process(target=books_flow.flow_books, args=('return',))
            #book_flow.daemon = True
            #book_flow.start()
            print('start books return daemon...')
    #加书
    elif content == contantZhAndEn.word_book_new_one or content == contantZhAndEn.word_book_new_two:
        print('你说：' + content)
        books_flow.flow_books('add')
        print('start books add daemon...')

    elif contantZhAndEn.word_book_recommendation in content:
        print('你说：' + content)
        response=bookRecommendation.health_check()
        if response:
            content=f"中文转英文翻译。{content}"
            print('translate content:' + content)
            message=bookRecommendation.get_recommendation(content)
            message=translate.translate(f"英文转中文翻译。{message}")
            print('translate message: ' + message)
            if VoiceSdk.text2sound(message):
                print(message)
                vadSound.play_sound()
        else:
            if VoiceSdk.text2sound(contantZhAndEn.word_please_turn_on_book_recommendation):
                print('请开启图书推荐服务.')
                vadSound.play_sound()
    elif content == contantZhAndEn.word_recommand_next_boot:
        print('你说：' + content)
        response=bookRecommendation.health_check()
        if response:
            message=bookRecommendation.get_next_recommendation()
            message=translate.translate(f"英文转中文翻译。{message}")
            print('translate message: ' + message)
            if VoiceSdk.text2sound(message):
                print(message)
                vadSound.play_sound()
        else:
            if VoiceSdk.text2sound(contantZhAndEn.word_please_turn_on_book_recommendation):
                print('请开启图书推荐服务.')
                vadSound.play_sound()
    elif content == contantZhAndEn.word_move_forward:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_moving):
            print('机器人：向前走两步')
            vadSound.play_sound()
            robot.forward()
            time.sleep(2)
            robot.stopFB()
    elif content == contantZhAndEn.word_move_backwards:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_moving_back):
            print('机器人：向后走两步')
            vadSound.play_sound()
            robot.backward()
            time.sleep(2)
            robot.stopFB()    
    elif content == contantZhAndEn.word_jump:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_cannot_jump_high):
            print('机器人：我跳了一下')
            vadSound.play_sound()
            robot.jump()
    elif content == contantZhAndEn.word_shake_hands:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_lets_shake_hands):
            print('机器人：来握手啊')
            vadSound.play_sound()
            robot.handShake()
    elif content == '握左手':
        print('你说：' + content)
        if VoiceSdk.text2sound('好嘞，来握左手啊'):
            print('机器人：来握左手啊')
            vadSound.play_sound()
            robot.leftHandShake()
    elif content == contantZhAndEn.word_pee:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_so_embarrassing):
            print('机器人：撒尿了')
            vadSound.play_sound()
            robot.pee()
    elif content == contantZhAndEn.word_time_now:
        time_tup = time.localtime(time.time())
        print('你说：' + content)
        if VoiceSdk.text2sound('你好，当前时间为{}年{}月{}日{}点{}分{}秒'.format(time_tup[0],time_tup[1],time_tup[2],time_tup[3],time_tup[4],time_tup[5])):
            print(f'机器人：报时间')
            vadSound.play_sound()
    elif content == contantZhAndEn.word_weather_today:
        print('你说：' + content)
        today=weather.getWeatherInfoToday(language)
        if VoiceSdk.text2sound(f'{today}'):
            print(f'机器人：今天天气')
            vadSound.play_sound()
    elif content == contantZhAndEn.word_weather_tommorrow:
        tmr=weather.getWeatherInfoTomorrow(language)
        print('你说：' + content)
        if VoiceSdk.text2sound(f'{tmr}'):
            print(f'机器人：明天天气')
            vadSound.play_sound()
    elif content == contantZhAndEn.word_processor_usage:
        print('你说：' + content)
        cpu=psutil.cpu_percent()
        print(cpu)
        if VoiceSdk.text2sound(contantZhAndEn.word_processor_usage_rate.format(cpu)):
            print(f'机器人：cpu')
            vadSound.play_sound()
    elif content == contantZhAndEn.word_memory_usage:
        print('你说：' + content)
        mem=psutil.virtual_memory().percent
        print(mem)
        if VoiceSdk.text2sound(contantZhAndEn.word_memory_usage_rate.format(mem)):
            print(f'机器人：内存')
            vadSound.play_sound()
    elif content == contantZhAndEn.word_space_walk:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_show_a_piece):
            print('机器人：太空步')
            vadSound.play_sound()
            robot.spaceSteps()
    elif content == contantZhAndEn.word_downward_facing_dog_pose:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_okay):
            print('机器人：下犬式')
            vadSound.play_sound()
            robot.DDogPose()
    elif content == contantZhAndEn.word_upward_facing_dog_pose:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_okay):
            print('机器人：上犬式')
            vadSound.play_sound()
            robot.UDogPose()
    elif content == contantZhAndEn.word_dance:
        print('你说：' + content)
        if VoiceSdk.text2sound(contantZhAndEn.word_king_of_dancing):
            print('机器人：跳舞')
            vadSound.play_sound()
            robot.dance()
            time.sleep(1)
            if VoiceSdk.text2sound(contantZhAndEn.word_thanks):  
                vadSound.play_sound()
                robot.thankYou()              
    else:
        isGot=False
        
    if isGot:
        status.write1()
     
    return isGot


    
#the followings are used to debug
# chat()
#result = tuling('hello')
#print(result)




