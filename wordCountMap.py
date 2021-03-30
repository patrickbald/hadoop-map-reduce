#!/usr/bin/env python3

import sys
import io

def main():
	stream = io.TextIOWrapper(sys.stdin.buffer, encoding='iso-8859-1')

	for line in stream:
		word = line.split()[0]
		print(f"{word.strip()} 1")

if __name__ == "__main__":
	main()
