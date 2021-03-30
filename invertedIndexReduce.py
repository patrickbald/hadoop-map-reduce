#!/usr/bin/env python3

import sys

def main():
	
	wordIndex = dict()

	for line in sys.stdin:
		try:
			word, host = line.split()[0], line.split()[1]
		except:
			continue

		if word not in wordIndex:
			wordIndex[word] = [host]
		else:
			if host not in wordIndex[word]:
				wordIndex[word].append(host)

	for word, hosts in wordIndex.items():
		print(word)
		for host in hosts:
			print(f"/t{host}")

if __name__ == '__main__':
	main()
