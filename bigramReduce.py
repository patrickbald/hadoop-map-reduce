#!/usr/bin/env python3

import sys

def main():
	
	pairs = dict()

	for pair in sys.stdin:

		pair = pair.strip()
			
		if pair not in pairs:
			pairs[pair] = 1
		else:
			pairs[pair] += 1

	orderedTuples = sorted(pairs.items(), key=lambda item: (item[1], item[0]))
	sortedCount = {k: v for k, v in orderedTuples}

	for pair, count in sortedCount.items():
		print(f"{count} {pair}")

if __name__ == "__main__":
	main()
