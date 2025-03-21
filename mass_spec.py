import os
import pandas as pd
from  masses import *




def find_peak_components(molecule, peak, charge=1):
    mass, atom_dict = calculate_mass(molecule, "mono")
    if mass is None:
        return None
    if "." in str(peak):
        decimals = len(str(peak).split(".")[1])-1
    else:
        decimals = 0
    print("Decimals:", decimals)
    print(peak)
    peak*=charge
    peak -= charge*1.007276
    print(peak)
    #print(atom_dict)
    try:
        float(peak)
        #print(peak)
    except:
        print("Peak is not a number", peak)
        return None






    atom_list= [[k]*v for k,v in sorted(atom_dict.items(), key = lambda item: mass_dict[item[0]]["average"], reverse = True)]
    unpacked = []
    for i in atom_list:
        unpacked.extend(i)
    print(unpacked)
    m = 0
    switch = [1] * len(unpacked)
    best_guess = None
    best_guess = combinatorial(unpacked, peak, decimals)
    print(best_guess)

    if best_guess[0]:
        unique = set(best_guess[1])
        result = {}
        for u in unique:
            result[u] = best_guess[1].count(u)
        print("Peak composition:")
        [print("{}: {}".format(k,v)) for k,v in result.items()]
        print("Mass:",calculate_mass("".join(best_guess[1]), "mono")[0])

    else:
        print("Peak not identified")



def combinatorial(unpacked, peak, decimals):
    import itertools
    # combinations('ABCD', 2) → AB AC AD BC BD CD
    # combinations(range(4), 3) → 012 013 023 123
    for combination in itertools.product([1,0], repeat=len(unpacked)):
        #print(combination)

        atoms = list(itertools.compress(unpacked, combination))
        mass = calculate_mass("".join([a for a in atoms]))[0]
        #print(round(mass, decimals),  round(peak, decimals))
        if round(mass, decimals) == round(peak, decimals):
            return True, atoms
    return False, None


# 1 -> m > peak
# 2 -> end of list
def try_next(m, i, unpacked, switch, peak, decimals):
    atom = unpacked[i]
    print(i, atom, m)
    m += mass_dict[atom]["mono"]
    if round(m, decimals) == peak:
        return True, [atom]
    if m > peak:
        return False, 1
    if m < peak:

        r = try_next(m,i+1, unpacked[1:], switch, peak, decimals)
        print(r)
        if r[0]:
            return True, r[1]+[atom]
        else:
            return False, None
    return False, None





def try_all_combinations(atom_list):
    atom_list = []
    pass







find_peak_components("C19H28N4O5", 393.21, 1)
find_peak_components("CH12", 2, 1)

while True:


    m = input("\nInput [MOLECULE] [peak]: \n>>").split(" ")
    if len(m) < 2:
        print("Missing molecule or peak value")
        continue
    #print(m)
    charge = 0
    find_peak_components(m[0], m[1], charge)
    quit()


