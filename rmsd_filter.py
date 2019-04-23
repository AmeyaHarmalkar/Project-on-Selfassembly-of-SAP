from pymol import cmd
from glob import glob

#Direct the location of the files
wt_file = "d34_native.pdb"
mut_glob = "floppy_output/d34_new_*.pdb"

#Load the native file
cmd.load(wt_file, "wt")

# Open another python file just to write in
data = open("data.txt", "w")
data.write("Name\tRMSD\n")

for file in glob(mut_glob):
	print(file)
	cmd.load(file, "mut")
	rms = cmd.align("wt", "mut")[0]
	data.write("%s\t%s\n"% (file,rms))
	cmd.delete("mut")

data.close()

