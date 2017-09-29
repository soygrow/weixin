# -*- coding: utf-8 -*-
# filename: handle.py

import web
import model

class Index(object):
    def GET(self):
	print "##################### index"
	render = model.('html/')
	return render.index()

