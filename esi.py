




H =1.007276


def get_ion_charge(peak1, peak2, charge=1):

    n= int(round(charge*(peak2-H) / (peak1-peak2),0))
    print("The charges of the peaks are:", n, n+1)
    return n, n+1
    
    

def get_ion_mass(peak, charge):

    
    
    mass =peak*charge - charge*H

    return mass


peaks = (808.28, 739.20, 2)

charges = get_ion_charge(*peaks)

masses = [get_ion_mass(p,c) for p, c in zip(peaks, charges)]
print("Peaks:", peaks)
print("Charges:", charges)
print("Masses:", masses)
print("Average mass:", sum(masses)/2)

while True:
    p= input("\n[Peak1 (-charge)], [Peak2 (+charge)]\n>>")
    p = p.split(" ")
    if len(p) >=3:
        c=int(p[2])
    else:
        c=1

    peaks = (float(p[0]), float(p[1]))
    charges = get_ion_charge(*peaks, c)
    masses = [get_ion_mass(p,c) for p,c in zip(peaks, charges)]
    print("Peaks:", peaks)
    print("Charges:", charges)
    print("Masses:", masses)
    print("Average mass:", sum(masses)/2)
