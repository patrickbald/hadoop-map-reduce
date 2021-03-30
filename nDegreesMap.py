#!/usr/bin/env python3

import sys
import io
import os
import re
import urllib.parse

def main():

	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')
	
	for line in stream:
		print(line.rstrip())

if __name__ == '__main__':
	main()
