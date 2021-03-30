#!/usr/bin/env python3

import sys
import io
from pprint import pprint

def main():

	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	for line in stream:
		line = line.strip()
		print(f"{line}")
	
if __name__ == "__main__":
	main()
