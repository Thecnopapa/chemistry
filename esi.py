### Author: Iain Visa ###

# Script to calculate the charges and masses of two peaks from an ESI spectra.


# Define the mass of a proton
H =1.007276


# Function to determine the charge of the peaks
def get_ion_charge(peak1, peak2, charge=1):
    # Determine the charge of the least charged peak
    n= int(round(charge*(peak2-H) / (peak1-peak2),0))
    print("The charges of the peaks are:", n, n+1)
    return n, n+1
    
    

def get_ion_mass(peak, charge):
    # Determine the mass of an ion of charge n
    mass =peak*charge - charge*H
    return mass

# Example run
peaks = (808.28, 739.20, 2) # This the required input to calculate the charges
charges = get_ion_charge(*peaks)
# Calculate the masses for each of the peaks calculated
masses = [get_ion_mass(p,c) for p, c in zip(peaks, charges)]
# Print the results
print("Peaks:", peaks)
print("Charges:", charges)
print("Masses:", masses)
print("Average mass:", sum(masses)/2)


# Run the calculation from user input indefinitely 
while True:
    # Get user input
    p= input("\n[Peak1 (-charge)], [Peak2 (+charge)]\n>>")
    p = p.split(" ")
    # Determine whether the user provides the number of peaks between the provided peaks
    if len(p) >=3:
        c=int(p[2])
    else:
        c=1
    # Set up input for the functions
    peaks = (float(p[0]), float(p[1]))
    # Calculate the charges
    charges = get_ion_charge(*peaks, c)
    # Calculate the masses
    masses = [get_ion_mass(p,c) for p,c in zip(peaks, charges)]
    
    # Print results
    print("Peaks:", peaks)
    print("Charges:", charges)
    print("Masses:", masses)
    print("Average mass:", sum(masses)/2)
