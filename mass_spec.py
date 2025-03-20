import os
import pandas as pd
from  masses import *




def find_peak_components(molecule, peak):
    mass, atom_list = calculate_mass(molecule, "abundant")
    if mass is None:
        return None
    print(atom_list)
    try:
        float(peak)
        print(peak)
    except:
        print("Peak is not a number", peak)
        return None

    best_guess = {}

    for atm in atom_list:


def try_all_combinations(atom_list):
    atom_list = []
    pass









while True:


    m = input("\nInput [MOLECULE] [peak]: \n>>").split(" ")
    if len(m) < 2:
        print("Missing molecule or peak value")
        continue
    #print(m)
    find_peak_components(m[0], m[1])


