#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
  
import json 
import urllib 
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
def get_weather(location):
    url = 'https://api.seniverse.com/v3/weather/now.json?key=voi0ipcq4x9168rq&location='+location+'&language=zh-Hans&unit=c'
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()

    data = json.loads(res)
    for item in data['results']:
	text = item['now']['text']
	temp = item['now']['temperature']
	textStr = json.dumps(text, ensure_ascii=False)
	tempStr = json.dumps(temp, ensure_ascii=False)
    	content = u"今天天气是:" + textStr + u" \n温度是：" + tempStr
    print content
    return content

