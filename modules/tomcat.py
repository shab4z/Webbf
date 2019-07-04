#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import subprocess
import re

from multiprocessing.dummy import Pool as ThreadPool
from utils import *

class TomcatModule():
	def __init__(self, lst, nb_threads):
		self.urls = lst
		self.urn = '/manager/html'
		self.wordlistPath = 'modules/config/tomcat.txt'
		self.regex = r"200.*?\|(.*?)\|"
		self.urls = check_up_services(lst)
		with ThreadPool(nb_threads) as pool:
			pool.map(self.tryDefaultCredsPatator, self.urls)

	def tryDefaultCredsPatator(self, url):
		print_info("Trying default credentials on "+url)
		output = subprocess.getoutput("python3 patator/patator.py http_fuzz url='"+url+self.urn+\
			"' auth_type=basic method=GET user_pass=COMBO00:COMBO01 0='"+self.wordlistPath+\
			"' -x ignore:code=401 auto_urlencode=1")
		if output.find("HTTP/1.1 200") > 0:
			matches = re.search(self.regex, output)
			if matches:
				print_success("[%s] : (%s)" % (url, matches.group(1).strip()))
