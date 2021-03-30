#!/usr/bin/env python3

import sys
from collections import defaultdict
from pprint import pprint

def main():

	host_outlinks = defaultdict(set)

	# Generate outlinks for each host
	for line in sys.stdin:
		host, outlink = line.split()[0], line.split()[1]
		host_outlinks[host].add(outlink)

	next_hop = set()
	next_hop.add('www.nd.edu')
	current_hop_outlinks = prev_outlinks = set()
	hop_links = defaultdict(set)
	curr_hop = 0

	# Breadth First Search through outlinks
	while len(next_hop):

		current_hop_outlinks = next_hop
		next_hop = set()

		for link in current_hop_outlinks:
			prev_outlinks.add(link)
			for ref in host_outlinks[link]:
				if ref not in prev_outlinks:
					hop_links[curr_hop].add(ref)
					next_hop.add(ref)

		curr_hop += 1

	for hop, links in hop_links.items():
		print(f"{hop} {len(links)}")

if __name__ == '__main__':
	main()
