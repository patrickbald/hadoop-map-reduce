#!/usr/bin/env python3

import sys
from collections import defaultdict

def main():

	outlinks = dict()

	for line in sys.stdin:
		target, source = line.split()[0], line.split()[1]

		if target not in outlinks:
			outlinks[target] = [source]
		else:
			if source not in outlinks[target]:
				outlinks[target].append(source)

	inlinks = defaultdict(set)

	for source, targets in outlinks.items():
		for t in targets:
			if t in outlinks.keys():
				inlinks[t].add(source)
				if t in inlinks[t]:
					inlinks[t].remove(t)
				

	for host, inlinks in inlinks.items():
		if inlinks:
			print(f"{host}")
			for link in inlinks:
				print(f"\t{link}")

if __name__ == '__main__':
	main()
