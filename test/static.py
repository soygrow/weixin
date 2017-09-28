# -*- coding: utf-8 -*-
# filename: static.py

import web

class Static:
    def GET(self, file):
	print "++@@@@@###++++++++++++++: tatic"
	print file
	#render = web.template.render('Love/js')
	web.seeother('/static/'+file)
