import os
#!usr/bin/env python

'''
Diverse code selector code

Author : Ameya Harmalkar

'''

import sys

filename = "sort_file"
#sys.argv[1]


file = open(filename, 'r')
#lines = file.readlines()

out = open('output.txt', 'w')



low_a = 0
for line in file :
	values = line.rstrip("\n").split("\t")[1]
	a = float(values)

	if int(a-low_a) > 0:
		low_a = a
		if a < 10 :
			out.write(line)
			print(line)

out.close()

