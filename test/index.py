# -*- coding: utf-8 -*-
# filename: handle.py

import web

class Index(object):
    def GET(self):
	print "##################### index"
	render = web.template.render('html/')
	return render.index()

