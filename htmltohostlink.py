#!/usr/bin/env python3

import sys
import io
import re
import urllib.parse
import os

def main():
	# Create input stream
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf8')

	for line in stream:
		hrefs = re.findall(r'href="([^"]+)"', line)
		for link in hrefs:
			url = urllib.parse.urlparse(link)
			if url.netloc: 
				print(f"{curr_host} {url.netloc}")


if __name__ == '__main__':
	main()
