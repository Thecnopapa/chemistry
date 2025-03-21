




H =1


def get_ion_charge(peak1, peak2):

    n= int(round((peak2-H) / (peak1-peak2),0))
    print("The charges of the peaks are:", n, n+1)
    return n, n+1
    
    

def get_ion_mass(peak, charge):

    
    
    mass =peak*charge - charge*H

    return mass


peaks = (808.28, 771.75)

charges = get_ion_charge(*peaks)

masses = [get_ion_mass(p,c) for p, c in zip(peaks, charges)]
print("Peaks:", peaks)
print("Charges:", charges)
print("Masses:", masses)
print("Average mass:", sum(masses)/2)


