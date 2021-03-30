#!/usr/bin/env python3

import sys
import io
import re
import os

def main():

	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	current_file = os.environ['mapreduce_map_input_file']
	curr_host = re.sub(r'hdfs://disc01.crc.nd.edu:8020/public/www.2021/', '', current_file)

	for line in stream:
		line = line.strip()

		words = re.findall(r'(?<=>)[^<]+', line)

		for word in words:
			res = re.sub(r'[^\w\s]', '', word)
			for string in res.split():

				if not string.isalpha(): continue
				if string.isnumeric(): continue
				if len(string) < 3: continue

				print(f"{string.lower()} {curr_host}")


if __name__ == '__main__':
	main()
