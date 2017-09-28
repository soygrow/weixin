#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
  
import json 
import urllib 
import urllib2
import redis

def getToken():
    r = redis.Redis(host='localhost', port=6379, db=0)
    token = r.get('token')
    if token:
	print token
	return token
    else:
        print "Token is invalid"
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx3f6eea3b9495226e&secret=d63f4a340e16332826fbc91824c66095'
    	req = urllib2.Request(url)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	data = json.loads(res)
	tokenStr = data['access_token']
	expireTime = data['expires_in']

	r.set('token', tokenStr, expireTime)
	print tokenStr
	return tokenStr
    

