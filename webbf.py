#!/usr/bin/env python
# -*- coding: utf-8 -*-

from options import *
from utils import *
import sys
import json

class WebBf():
    def __init__(self):
        opt = ParseOpt()
        self.input_file = opt.args.input_file
        self.nb_threads = opt.args.threads
        self.data = self.getWebIntToBf()
        self.process()

    def getWebIntToBf(self):
        try:
            file = open(self.input_file, 'r')
            content = file.read().replace('\n', '')
        except Exception as e:
            print_error("Unexpected error: %s" % e)
            sys.exit(0)
        print_info("Loading JSON content from '"+self.input_file+"'")
        return json.loads(content)

    def import_class(self, cl):
        d = cl.rfind(".")
        classname = cl[d+1:len(cl)]
        m = __import__(cl[0:d], globals(), locals(), [classname])
        return getattr(m, classname)

    def process(self):
        for key, value in self.data.items():
            if value:
                print_info("Loading "+key.capitalize()+"Module")
                c = self.import_class("modules."+key.lower()+"."+key.capitalize()+"Module")
                c(value, self.nb_threads)
a = WebBf()