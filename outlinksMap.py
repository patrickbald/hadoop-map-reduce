#!/usr/bin/env python3

import sys
import io
import re
import os
import urllib.parse

def main():

	stream = io.TextIOWrapper(sys.stdin.buffer, encoding = "iso-8859-1")
	# current_file = os.environ['mapreduce_map_input_file']
	# curr_host = re.sub(r'hdfs://disc01.crc.nd.edu:8020/public/www.2021/', '', current_file)
	
	''' 
	for line in stream:
		# hrefs = re.findall(r'<a (?:class="link")?\s?href=[\'"]?(https?[^\'">]+)', line)
		hrefs = re.findall(r'href="([^"]+)"', line)
		for link in hrefs:
			url = urllib.parse.urlparse(link)
			if url.netloc: 
				print(f"{curr_host} {url.netloc}")

	'''

	for line in stream:
		host, link = line.split()[0], line.split()[1]
		print(f"{host} {link}")
		
if __name__ == '__main__':
	main()
