#!/usr/bin/env python
# -*- coding: utf-8 -*-

#./xxxx.py --help
#./xxxx.py --file paparrazi.out -c config.yml

import argparse

class ParseOpt():
	def __init__(self):
		p = argparse.ArgumentParser(description = 'Webbf - Default admin credential finder')
		p.add_argument('input_file', action='store', help='Paparazzi output file (contains targets in a specific format)')
		p.add_argument('-t', '--threads', help="How many threads to use ? (default=8)", type=int, default=8)
		self.args = p.parse_args()
