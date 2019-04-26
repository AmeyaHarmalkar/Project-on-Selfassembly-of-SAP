import pyrosetta
from pyrosetta import *
init()

import math
import numpy as np
import os

from CoM_filter import *


# Define the name of your directory

directory = '/Users/aharmal1/Ameya/Spring_2019/Project/prediction/4aq1/domains/all_domains/sap6/floppy_output'

output = open("actual_output.txt", "w")

for file in os.listdir(directory) :
	
	if file.endswith(".pdb") :
		filepath = os.path.join(directory, file)
		pose = pose_from_pdb(filepath)
		
		d1 = centre_of_mass_calc(pose, 190, 297)
		d2 = centre_of_mass_calc(pose, 301, 424)
		d3 = centre_of_mass_calc(pose, 1, 90)
		d4 = centre_of_mass_calc(pose, 539, 721)

		is_planar = planarity_checker(d1,d2,d3,d4)

		if is_planar:
			output.write(file+"\n")

		
		continue
	
	#else :
		#continue