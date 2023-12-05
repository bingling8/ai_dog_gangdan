#!/usr/bin/env/python3
# File name   : robot.py
# Description : Robot interfaces.
import time
import json
import serial

ser = serial.Serial("/dev/serial0", 115200)
dataCMD = json.dumps({'var': "", 'val': 0, 'ip': ""})
upperGlobalIP = 'UPPER IP'

pitch, roll = 0, 0


def setUpperIP(ipInput):
    global upperGlobalIP
    upperGlobalIP = ipInput


def forward(speed=100):
    dataCMD = json.dumps({'var': "move", 'val': 1})
    ser.write(dataCMD.encode())
    print('robot-forward')


def backward(speed=100):
    dataCMD = json.dumps({'var': "move", 'val': 5})
    ser.write(dataCMD.encode())
    print('robot-backward')


def left(speed=100):
    dataCMD = json.dumps({'var': "move", 'val': 2})
    ser.write(dataCMD.encode())
    print('robot-left')


def right(speed=100):
    dataCMD = json.dumps({'var': "move", 'val': 4})
    ser.write(dataCMD.encode())
    print('robot-right')


def stopLR():
    dataCMD = json.dumps({'var': "move", 'val': 6})
    ser.write(dataCMD.encode())
    print('robot-stop')


def stopFB():
    dataCMD = json.dumps({'var': "move", 'val': 3})
    ser.write(dataCMD.encode())
    print('robot-stop')


def lookUp():
    dataCMD = json.dumps({'var': "ges", 'val': 1})
    ser.write(dataCMD.encode())
    print('robot-lookUp')


def lookDown():
    dataCMD = json.dumps({'var': "ges", 'val': 2})
    ser.write(dataCMD.encode())
    print('robot-lookDown')


def lookStopUD():
    dataCMD = json.dumps({'var': "ges", 'val': 3})
    ser.write(dataCMD.encode())
    print('robot-lookStopUD')


def lookLeft():
    dataCMD = json.dumps({'var': "ges", 'val': 4})
    ser.write(dataCMD.encode())
    print('robot-lookLeft')


def lookRight():
    dataCMD = json.dumps({'var': "ges", 'val': 5})
    ser.write(dataCMD.encode())
    print('robot-lookRight')


def lookStopLR():
    dataCMD = json.dumps({'var': "ges", 'val': 6})
    ser.write(dataCMD.encode())
    print('robot-lookStopLR')


def steadyMode():
    dataCMD = json.dumps({'var': "funcMode", 'val': 1})
    ser.write(dataCMD.encode())
    print('robot-steady')


def stayLowMode():
    dataCMD = json.dumps({'var': "funcMode", 'val': 2})
    ser.write(dataCMD.encode())
    print('robot-stayLow')


def handShake():
    dataCMD = json.dumps({'var': "funcMode", 'val': 3})
    ser.write(dataCMD.encode())
    print('robot-handshake')


def jump():
    dataCMD = json.dumps({'var': "funcMode", 'val': 4})
    ser.write(dataCMD.encode())
    print('robot-jump')


def leftHandShake():
    dataCMD = json.dumps({'var': "funcMode", 'val': 13})
    ser.write(dataCMD.encode())
    print('robot-lefthandshake')


def rest():
    dataCMD = json.dumps({'var': "funcMode", 'val': 10})
    ser.write(dataCMD.encode())
    print('robot-rest')


def yoga():
    dataCMD = json.dumps({'var': "funcMode", 'val': 12})
    ser.write(dataCMD.encode())
    print('robot-yoga')


def squat():
    dataCMD = json.dumps({'var': "funcMode", 'val': 14})
    ser.write(dataCMD.encode())
    print('robot-squat')


def pee():
    dataCMD = json.dumps({'var': "funcMode", 'val': 11})
    ser.write(dataCMD.encode())
    print('robot-pee')

def spaceSteps():
    dataCMD = json.dumps({'var': "funcMode", 'val': 15})
    ser.write(dataCMD.encode())
    print('robot-spaceSteps')

def DDogPose():
    dataCMD = json.dumps({'var': "funcMode", 'val': 16})
    ser.write(dataCMD.encode())
    print('robot-DDogPose')

def UDogPose():
    dataCMD = json.dumps({'var': "funcMode", 'val': 17})
    ser.write(dataCMD.encode())
    print('robot-UDogPose')

def thankYou():
    dataCMD = json.dumps({'var': "funcMode", 'val': 19})
    ser.write(dataCMD.encode())
    print('robot-thankyou')

def dance():
    forward()
    time.sleep(1.5)
    stopFB()
    jump()
    time.sleep(1.5)
    backward()
    time.sleep(1.5)
    stopFB()
    jump()
    time.sleep(1.5)
    dataCMD = json.dumps({'var': "funcMode", 'val': 18})
    ser.write(dataCMD.encode())
    time.sleep(7)
    thankYou()
    print('robot-dance')




def lightCtrl(colorName):
    colorNum = 0
    if colorName == 'off':
        colorNum = 0
    elif colorName == 'blue':
        colorNum = 1
    elif colorName == 'red':
        colorNum = 2
    elif colorName == 'green':
        colorNum = 3
    elif colorName == 'yellow':
        colorNum = 4
    elif colorName == 'cyan':
        colorNum = 5
    elif colorName == 'magenta':
        colorNum = 6
    elif colorName == 'cyber':
        colorNum = 7
    dataCMD = json.dumps({'var': "light", 'val': colorNum})
    ser.write(dataCMD.encode())


def buzzerCtrl(buzzerCtrl, cmdInput):
    dataCMD = json.dumps({'var': "buzzer", 'val': buzzerCtrl})
    ser.write(dataCMD.encode())


if __name__ == '__main__':
    # robotCtrl.moveStart(100, 'forward', 'no', 0)
    # time.sleep(3)
    # robotCtrl.moveStop()
    while 1:
        time.sleep(1)
        pass
