#!/usr/bin/env/python3
# File name   : status.py
# Description : status interfaces.

import os

status_file = '/home/pi/Workspace/led_status/audio_status'

def write0():
    with open(status_file, 'w') as f:
        f.write('0')

def write1():
    with open(status_file, 'w') as f:
        f.write('1')

def write2():
    with open(status_file, 'w') as f:
        f.write('2')


move_status_file = '/home/pi/Workspace/move_status/forward_status'


def startOA():
    with open(move_status_file, 'w') as f:
        pass
        

def stopOA():
    os.remove(move_status_file)


language_status_file = '/home/pi/Workspace/language_status/zh_status'

def setLanguage(lan):
    if lan=='en':
        setLanguageEn()
    elif lan=='zh':
        setLanguageZh()

def setLanguageZh():
    with open(language_status_file,'w') as f:
        f.write('zh')
        
def setLanguageEn():
    with open(language_status_file,'w') as f:
        f.write('en')

def getLanguage():
    with open(language_status_file,'r') as f:
        language=f.readline()
    return language

process_status_file = '/home/pi/Workspace/process_status'


def setProcessStatus(mode,status):
    with open(process_status_file,'w') as f:
        f.write(mode+'-'+str(status))
        
def getProcessStatus():
    with open(process_status_file,'r') as f:
        process=f.readline()
    return process
    

if __name__ == '__main__':
    write0()



