#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import subprocess
import re

from multiprocessing.dummy import Pool as ThreadPool
from utils import *

class BmcdiscoveryModule():
	def __init__(self, lst, nb_threads):
		self.urls = lst
		self.urn = '/ui/'
		self.wordlistPath = 'modules/config/bmcdiscovery.txt'
		self.regex = r"200.*?\|(.*?)\|"
		self.urls = check_up_services(lst)
		with ThreadPool(nb_threads) as pool:
			pool.map(self.tryDefaultCredsPatator, self.urls)

	def tryDefaultCredsPatator(self, url):
		print_info("Trying default credentials on "+url)
		output = subprocess.getoutput("python3 patator/patator.py http_fuzz url='"+url+self.urn+\
			"' method=POST body='tw_login_username=COMBO00&tw_login_password=COMBO01&tw_login_button=&tw_login_method=GET' user_pass=COMBO00:COMBO01 0='"\
			+self.wordlistPath+"' follow=1 accept_cookie=1 -x ignore:code=403 auto_urlencode=1")
		if output.find("HTTP/1.1 200") > 0:
			matches = re.search(self.regex, output)
			if matches:
				print_success("[%s] : (%s)" % (url, matches.group(1).strip()))
