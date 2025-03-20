# Initialise arrays
PickerName = []
PickedWeight = []
PickerCertificate = []

# Input number of members (must be at least 2)
Number = int(input("Enter number of members: "))
while Number < 2:
    Number = int(input("Enter number of members (must be at least 2): "))

# Input names and validated pick weights
for i in range(Number):
    name = input("Enter member's name: ")
    weight = float(input("Enter weight picked (kg): "))

    while weight < 0:  # Ensure no negative weights
        print("Weight cannot be negative.")
        weight = float(input("Enter weight picked (kg): "))

    PickerName.append(name)
    PickedWeight.append(weight)

# Sort both arrays in descending order based on PickedWeight
for i in range(Number - 1):
    for j in range(i + 1, Number):
        if PickedWeight[i] < PickedWeight[j]:  # Swap if necessary
            PickedWeight[i], PickedWeight[j] = PickedWeight[j], PickedWeight[i]
            PickerName[i], PickerName[j] = PickerName[j], PickerName[i]

# Output the best two members
print("\nBest in Group:", PickerName[0], "with", PickedWeight[0], "kg")
print("Second Best in Group:", PickerName[1], "with", PickedWeight[1], "kg")

# Identify certificate recipients
for i in range(Number):
    if PickedWeight[i] > 3:
        PickerCertificate.append(PickerName[i])

# Output the number of certificates
print("\nNumber of certificates to be printed:", len(PickerCertificate))
