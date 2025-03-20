import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.listdir("/storage/emulated/0/Download"))
monoisotopic = pd.read_csv("monoisotopic_masses.csv",
                           names=["atom", "symbol", "mass", "abundance"])

print(monoisotopic)

mass_dict = {}
for unique_atom in set(monoisotopic["atom"]):
    subset = monoisotopic[monoisotopic["atom"] == unique_atom]
    subset = subset.sort_values(by=["abundance"], ascending=False)
    # print(subset)
    symbol = subset["symbol"].values[0].split("(")[0]
    #print(symbol)

    # symbol = list(subset.iterrows())[0]["symbol"].split("(")[0]

    # mass_dict[symbol] = {"abundant":subset.iloc[:,0]["mass"]}
    mass_dict[symbol] = {}
    for i, isotope in enumerate(subset.itertuples()):
        #print(isotope)
        #print(isotope.symbol)
        s = isotope.symbol.split("(")[1].split(")")[0]
        if i == 0:
            mass_dict[symbol]["abundant"] = float(isotope.mass)
            mass_dict[symbol]["average"] = float(isotope.mass)*float(isotope.abundance)/100
        else:
            mass_dict[symbol]["average"] += float(isotope.mass) * float(isotope.abundance) / 100
        mass_dict[symbol][s] = float(isotope.mass)
#print(mass_dict.items())


def calculate_monoisotopic_mass(molecule="", mode = "abundant"):
    mass = 0
    for i, a in enumerate(molecule):
        if a.isalpha() and a.upper() == a:
            atom = a
            number = ""

            for n in molecule[i + 1:]:
                if n.isdigit():
                    number += n
                elif n.lower() == n:
                    atom += n
                else:

                    break
            if number == "":
                number = 1
            number = int(number)
            mass += mass_dict[atom][mode] * int(number)
            print(atom, number, mass_dict[atom][mode], mass_dict[atom]["abundant"] * int(number))
    print("Mass of {}: {}".format(molecule, mass))
    return mass


calculate_monoisotopic_mass("C8H10N4O2")




while True:
    m = input().split(" ")
    print(m)
    if len(m) > 1:
        mode = m[1]
    else:
        mode = "abundant"
    calculate_monoisotopic_mass(m[0], mode = mode)



