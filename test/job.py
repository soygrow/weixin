#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  

import urllib
import urllib2

import weather  
import time
import schedule
import threading

import gettoken

from datetime import datetime, timedelta
from time import sleep

def job():
    print "@@@@@@@@@@@@@@@@@"
    content = weather.get_weather()
    print content

    tokenStr = gettoken.getToken()
    url = 'https://api.weixin.qq.com/cgi-bin/message/mass/send?access_token='+tokenStr
    data = {"filter": {"is_to_all": False, "tag_id": 2}, "text": {"content": content}, "msgtype": "text"}
    print data
    data_encode = urllib.urlencode(data)
    req = urllib2.Request(url = url, data = data_encode)
    print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res

def thread():
    schedule.every().day.at("18:56").do(job)

    while True:
	schedule.run_pending();
	sleep(1)

def schedJob():
    job_thread = threading.Thread(target=thread)
    job_thread.start() 
