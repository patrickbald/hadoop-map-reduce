#!/usr/bin/env python3


import sys

def main():

	hostLinks = dict()

	for line in sys.stdin:
		host, link = line.split()[0], line.split()[1]
		
		if host not in hostLinks:
			hostLinks[host] = [link]
		else:
			if link not in hostLinks[host]:
				hostLinks[host].append(link)

	for host, links in hostLinks.items():
		print(f"{host}")
		if links:
			for l in links:
				print(f"\t{l}")

if __name__ == '__main__':
	main()
