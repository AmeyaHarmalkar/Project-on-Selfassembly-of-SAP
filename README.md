# Project on Selfassembly of SAP

# Step 1 : 
Creation of individual domain files using PyMol and characterizing the domains and the linkers for each of those files.

# Step 2 : 
Selection of the domain that we want to initiate our algorithm with. Determine a node. 

## Selection rules for determination of node :
 1. Check for the length of the linker residues between 2 domains. Choose the domains which have the shortest linker length.
 2. Check if the domain is in the centre of the multi-domain residue or not. Select the domain at the centre if the 
	   len(linker) < 4, accept that

# Step 3 : docking of the respective domains. 

## Preparation of the input pdbs 
 1. Obtain just the atom records and rename the chain name of receptor to A and ligand to B
 2. Concatenate the files together to create a combined protAB file.
 3. Perturb the unbound receptor and domains to generate a randomized structure before you could initiate global and/or local docking on them. Use the command :
    
    ```
    ~/Rosetta/main/source/bin/rosetta_scripts.default.macosclangrelease\
                -parser:protocol ~/Rosetta/demos/protocol_capture/replica_docking/rosetta_inputs/randomize_infile.xml \
                -in:file:s protAB.pdb \
                -database ~/Rosetta/main/database
            

 
