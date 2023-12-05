import time
import sys
sys.path.append('./ImagesRecognition')
import client
import common
import params
import robot
import voiceSdk
import vadSound
sys.path.append('./ImagesRecognition')
from face import *

def watch(event):
    matchs = FaceTool().all_names
    # face_key_val = {'lt':'李桃', 'cxx':'陈枭雄', 'yyf':'于一飞', 'jbc':'贾博淳'}
    while True:
        people = client.classify_people_image()
        if len(people) >= 1:
            print(f'{people}')
            if people[0] in matchs:
                name = people[0]
                print(f'[EVENT SET] Face recognized! You are {name}.')
                if voiceSdk.text2sound(f'人脸唤醒成功！你好，{name}'):
                    print(f'你好 {name}')
                    vadSound.play_sound()
                robot.handShake()
                event.set()
                break
            else:
                time.sleep(5)

