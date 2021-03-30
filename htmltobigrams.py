#!/usr/bin/env python3

import sys
import io
import re


def main():
	
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	current, prev = '', ''

	for line in stream:
		line = line.strip()

		words = re.findall(r'(?<=>)[^<]+', line)

		for word in words:
			res = re.sub(r'[^\w\s]', '', word)
			for string in res.split():

				if not string.isalpha(): continue
				if string.isnumeric(): continue
				if len(string) < 3: continue

				current = string.lower()

				if prev:
					print(f"{prev} {current}")
				
				prev = current

			prev = ''

if __name__ == '__main__':
	main()
