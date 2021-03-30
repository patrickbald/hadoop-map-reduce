#!/usr/bin/env python3

import sys
import io

def main():

	stream = io.TextIOWrapper(sys.stdin.buffer, encoding = 'iso-8859-1')

	for line in stream:
		host, link = line.split()[0], line.split()[1]
		print(f"{link} {host}")

if __name__ == '__main__':
	main()
