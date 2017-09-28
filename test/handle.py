# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive
import weather

class Handle(object):
    def GET(self):
        try:
	    data = web.input()
            print data
	    if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "hello2017" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
		print echostr
		return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
	    if isinstance (recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == "天气":
		toUser = recMsg.FromUserName
		fromUser = recMsg.ToUserName
		content_bj = weather.get_weather('beijing')
		content_sz = weather.get_weather('shenzhen')
		content = "老公提醒你：\n" + "地点：北京\n" + content_bj + "\n地点：深圳\n" + content_sz
		replyMsg = reply.TextMsg(toUser, fromUser, content)
		print replyMsg
		return replyMsg.send()
	    elif isinstance (recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == "老公":
		toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "老公还有几天就看一看见你了，很开心。不要着急，国庆8天我们好好过日子。"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                print replyMsg
                return replyMsg.send()
	    else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment
