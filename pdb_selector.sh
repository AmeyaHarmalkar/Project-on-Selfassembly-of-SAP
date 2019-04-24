grep ^output data.txt | sort -n -k2 | sed 's/output_d234\///' | awk '{print $1"\t"$NF}' > sort_file
python diverse_file_selector.py sort_file
awk '{print $1}' output.txt | sed 's/^/gunzip /' > sort_file.sh
chmod +x sort_file.sh
./sort_file.sh
mkdir sorted_pdbs
mv *.pdb sorted_pdbs