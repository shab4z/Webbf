#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import subprocess
import re

from multiprocessing.dummy import Pool as ThreadPool
from utils import *

class JenkinsModule():
	def __init__(self, lst, nb_threads):
		self.urls = lst
		self.urn = '/j_acegi_security_check'
		self.wordlistPath = 'modules/config/jenkins.txt'
		self.regex = r"200.*?\|(.*?)\|"
		self.urls = check_up_services(lst)
		with ThreadPool(nb_threads) as pool:
			pool.map(self.tryDefaultCredsPatator, self.urls)

	def tryDefaultCredsPatator(self, url):
		print_info("Trying default credentials on "+url)
		output = subprocess.getoutput("python3 patator/patator.py http_fuzz url='"+url+self.urn+\
			"' method=POST body='j_username=COMBO00&j_password=COMBO01&from=%2F&Submit=Sign+in' user_pass=COMBO00:COMBO01 0='"\
			+self.wordlistPath+"' follow=1 accept_cookie=1 -x ignore:code=401 auto_urlencode=1")
		if output.find("HTTP/1.1 200") > 0:
			matches = re.search(self.regex, output)
			if matches:
				print_success("[%s] : (%s)" % (url, matches.group(1).strip()))
