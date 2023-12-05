import snowboydecoder
import multiProcess
import status


def listen(event):
    global e
    e=event
    detector = snowboydecoder.HotwordDetector('resources/gangdan_en.pmdl', sensitivity=0.5)
    detector.start(detected_callback=myCallback)
    
def myCallback():
    print('English wake')
    status.setLanguageEn()
    e.set()