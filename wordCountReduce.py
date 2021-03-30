#!/usr/bin/env python3

import sys
import io

def main():

	count = dict()	

	for line in sys.stdin:
		word  = line.split()[0]
		if word not in count:
			count[word] = 1
		else:
			count[word] += 1

	orderedTuples = sorted(count.items(), key=lambda item: (item[1], item[0]))
	sortedCount = {k: v for k, v in orderedTuples}

	for word, count in sortedCount.items():
		print(count, word)

if __name__ == '__main__':
	main()


