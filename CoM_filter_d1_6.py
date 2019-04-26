import pyrosetta
from pyrosetta import *
init()

import math
import numpy as np

def centre_of_mass_calc(pose, start, end):
    '''
    This function calculates the center of mass of the domain using PyRosetta inbuilt functions
    '''
    CenoMass = pyrosetta.rosetta.core.pose.center_of_mass(pose,start,end)
    #CoM = CenoMass(pose, start, end)
    
    return np.array(CenoMass)


def planarity_checker(d1, d2, d3, d4, Value = "True"):
    '''
    This function checks whether the 4 atoms which are given as the input are in the same plane or not.
    If they are in the same plane, it returns a boolean True, else it returns a False.
    
    **Parameters**
        
        d1 : *array,float*
            Denotes the atom that will supposedly be the origin. Must be one of the root protein domains.
        d2 : *array,float*
            Denotes the other atom from the root protein domains.
        d3 : *array,float*
        d4 : *array,float*
        
    **Returns**
        
        *boolean*
    '''
    
    AB = d2 - d1
    AC = d3 - d1
    AD = d4 - d1
    
    AE = np.cross(AC, AB)
    # getting the cross product of the first 2 vector directions
    
    norm = np.linalg.norm(np.cross(AC, AB))
    
    AF = AE / norm
    
    value = np.dot((AD/ np.linalg.norm(AD)), (np.cross(AC,AB) / np.linalg.norm(np.cross(AC,AB))))
    
    Angle = math.degrees(math.acos(value))
    
    if 70 < Angle < 110 :
        
        if Value == True :
            
            print(Angle)
        return True
    
    else :
        return False
        