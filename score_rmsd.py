import math
import numpy as np

rmsd_file = "rmsd_file"
score_file = "sort_file"

data_1 = open(rmsd_file, "r")
data_2 = open(score_file, "r")

dict_1 = {}
dict_2 = {}


for line in data_1:
	key = line.split()[0]
	#print(float(line.split()[1]))
	dict_1[key] = float(line.split()[1])

for line in data_2:
	key = line.split()[1]

	dict_2[key] = float(line.split()[0])

output = open("plot.txt", "w")

for k in dict_1.keys():
	if k in dict_2.keys():
		print(dict_1[k],"\t",dict_2[k])
		output.write(str(dict_2[k]))
		output.write("\t")
		output.write(str(dict_1[k]))
		output.write("\n")
	
