#!/usr/bin/env/python3
# File name   : weather.py
# Description : weather interfaces.
import requests
import translate

forecast_url = "https://restapi.amap.com/v3/weather/weatherInfo?key=e6c9ec78796472a05e4c70303fb42ba2&city=310115&extensions=all&output=JSON"

def getWeatherInfoToday(language):
    try:
        response = requests.get(forecast_url)
        rep_json = response.json()
        if rep_json['status'] == '1':
            print(1)
            res=rep_json['forecasts'][0]['province'] + rep_json['forecasts'][0]['city'] +'，今天天气' +rep_json['forecasts'][0]['casts'][0]['dayweather'] + ',最高气温:'+rep_json['forecasts'][0]['casts'][0]['daytemp'] + '度，最低气温:'+rep_json['forecasts'][0]['casts'][0]['nighttemp']+'度'
            if language=="zh":
                return res
            elif language=="en":
                return  translate.translate(res)      
    except:
        return '目前无法获取天气情况哦'

def getWeatherInfoTomorrow(language):
    try:
        response = requests.get(forecast_url)
        rep_json = response.json()
        if rep_json['status'] == '1':
            print(1)
            res=rep_json['forecasts'][0]['province'] + rep_json['forecasts'][0]['city'] +'，明天天天气' +rep_json['forecasts'][0]['casts'][1]['dayweather'] + ',最高气温:'+rep_json['forecasts'][0]['casts'][1]['daytemp'] + '度，最低气温:'+rep_json['forecasts'][0]['casts'][1]['nighttemp']+'度'
            if language=="zh":
                return res
            elif language=="en":
                return  translate.translate(res) 
    except:
        return '目前无法获取天气情况哦'

if __name__ == '__main__':
    print(getWeatherInfoToday('en'))
    print(getWeatherInfoTomorrow('en'))
