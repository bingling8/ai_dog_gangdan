# coding=utf-8
import multiprocessing
import tulingRobot
import snowBoy
import time
import faceRecog
import status
import snowBoyEn
import os



def face_chat():
    # when face over, chat will over
    language=status.getLanguage()
    print('face_chat language: '+language)
    
    event = multiprocessing.Event()

    tuling_chat = multiprocessing.Process(target=tulingRobot.chat, args=(event,language,))
    tuling_chat.daemon = False
    tuling_chat.start()
    print('chat begin...')

    tuling_chat.join()
    print('chat over...')
    
    return


def watch_listen():
    # watching and listening
    while True:
        processAndStatus=status.getProcessStatus().split('-')

        if "0"==str(processAndStatus[1]).strip() :
            print('*******************************')
            event = multiprocessing.Event()
            global language
            listen_en = multiprocessing.Process(target=snowBoyEn.listen, args=(event,))
            listen_en.daemon = True
            listen_en.start()
            print('en listening...')

            listen = multiprocessing.Process(target=snowBoy.listen, args=(event,))
            listen.daemon = True
            listen.start()
            print('zh listening...')
            

            watch = multiprocessing.Process(target=faceRecog.watch, args=(event,))
            watch.daemon = True
            watch.start()
            print('watching...')

            status.write0()

            print('waited')
            event.wait()
            
            print(listen.is_alive())
            print(listen_en.is_alive())
            print(watch.is_alive())
            
            listen.terminate()
            listen_en.terminate()
            watch.terminate()
              
        face_chat()
        print('chat over here')
        os.system("sh /home/pi/AI_Dog_Raspberry-pi/restart.sh")
        time.sleep(1.24)

# face_chat()

