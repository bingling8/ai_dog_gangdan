# coding=utf-8
import vadSound
from aip import AipSpeech
import status
import edge_tts
import asyncio
import os
from pydub import AudioSegment

APP_ID = '41317840'  # 百度AI平台申请后换为自己的，下同
API_KEY = 'zMLnNAdjDuuuBGxIc9UeHnYo'
SECRET_KEY = 'wlPkymwoKur7l4nqQZp0IRzkYe9ofPcy'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
dev_pid = 1537

def initLanguage(language):
    global dev_pid
    if language=="en":
        dev_pid=1737
    elif language=="zh":
        dev_pid=1537

def text2sound(words='sorry'):
    if dev_pid==1537:
        print('text2sound: baidu')
        return text2soundByBaiDu(words)
    elif dev_pid==1737:
        print('text2sound: baidu')
        # asyncio.run(text2soundEnByEdgeTTS(words))
        # return True
        return text2soundByBaiDu(words)

def text2soundByBaiDu(words='sorry'):
    status.write2()
    # text to sound function
    result = client.synthesis(words, 'zh', 1, {
        'vol': 5, 'aue': 6, 'per': 1
    })

    if not isinstance(result, dict):
        with open('temp.wav', 'wb') as f:
            f.write(result)
        return True
    else:
        return False
    
    
async def text2soundEnByEdgeTTS(words='sorry') -> None:
    communicate = edge_tts.Communicate(words, 'en-US-EricNeural')  
    await communicate.save('./temp.mp3')
    # os.system("ffmpeg -y -i temp.mp3 -ac 1 -ar 16000 temp.wav")
    song = AudioSegment.from_mp3("./temp.mp3")
    song.set_frame_rate(16000).set_channels(1).export("./temp.wav", format="wav")
    return True

async def text2soundZhByEdgeTTS(words='sorry') -> None:
    communicate = edge_tts.Communicate(words, 'zh-CN-YunjianNeural')  
    await communicate.save('./temp.mp3')
    # os.system("ffmpeg -y -i temp.mp3 -ac 1 -ar 16000 temp.wav")
    print('text2soundzh: mp3 done')
    song = AudioSegment.from_mp3("./temp.mp3")
    song.set_frame_rate(16000).set_channels(1).export("./temp.wav", format="wav")
    print('text2soundzh: wav done')
    return True


def sound2text(file_path='temp.wav'):
    print('sound2text: ')
    status.write2()
    # sound to text function
    with open(file_path, 'rb') as fp:
        recog = client.asr(fp.read(), 'wav', 16000, {'dev_pid': dev_pid})
        
        if recog['err_no'] not in [0, 3301]:
            return False, recog['err_no']
        elif recog['err_no'] == 3301:
            return True, ''
        return True, recog['result'][0]

# the followings are used to debug
# text2sound('语音合成出错')
# result = sound2text()
# print(result)

'''
错误码	用户输入/服务端	含义	一般解决方法
3300	用户输入错误	输入参数不正确	请仔细核对文档及参照demo，核对输入参数
3301	用户输入错误	音频质量过差	请上传清晰的音频
3302	用户输入错误	鉴权失败	token字段校验失败。请用appkey 和 app secret生成
3303	原始音频或者服务端问题	转pcm失败	如下2个原因 1. wav amr音频转码失败，即音频有问题。2. 服务端问题，请将api返回结果反馈至论坛或者QQ群
3304	用户请求超限	用户的请求QPS超限	请降低识别api请求频率 （qps以appId计算，移动端如果共用则累计）
3305	用户请求超限	用户的日pv（日请求量）超限	请“申请提高配额”，如果暂未通过，请降低日请求量
3307	服务端问题	语音服务器后端识别出错问题	请将api返回结果反馈至论坛或者QQ群
3308	用户输入错误	音频过长	音频时长不超过60s，请将音频时长截取为60s以下
3309	用户输入错误	音频数据问题	服务端无法将音频转为pcm格式，可能是长度问题，音频格式问题等。 请将输入的音频时长截取为60s以下，并核对下音频的编码，是否是8K或者16K， 16bits，单声道。
3310	用户输入错误	输入的音频文件过大	语音文件共有3种输入方式： json 里的speech 参数（base64后）； 直接post 二进制数据，及callback参数里url。 分别对应三种情况：json超过10M；直接post的语音文件超过10M；callback里回调url的音频文件超过10M
3311	用户输入错误	采样率rate参数不在选项里	目前rate参数仅提供8000,16000两种，填写4000即会有此错误
3312	用户输入错误	音频格式format参数不在选项里	目前格式仅仅支持pcm，wav或amr，如填写mp3即会有此错误
'''
