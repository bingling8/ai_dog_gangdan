import snowboydecoder
import multiProcess
import status



def listen(event):
    global e
    e=event
    detector = snowboydecoder.HotwordDetector('resources/gangdan.pmdl', sensitivity=0.5)
    detector.start(detected_callback=myCallback)
    
def myCallback():
    print('中文唤醒')
    status.setLanguageZh()
    e.set()
    
