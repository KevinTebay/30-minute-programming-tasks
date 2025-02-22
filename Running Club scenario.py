# Define arrays to store member names, times, and certificate recipients
MemberName = []
MemberTime = []
MemberCertificate = []

# Input the names and times of 200 members
for i in range(4):
    name = input("Enter member name: ")
    MemberName.append(name)

    while True:
        try:
            time1 = int(input("Enter time in seconds for " + name + ": "))
            time2 = int(input("Re-enter time in seconds for verification: "))
            if time1 == time2:
                MemberTime.append(time1)
                break
            else:
                print("Times do not match. Please re-enter.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Sorting using Bubble Sort
for i in range(len(MemberTime) - 1):
    for j in range(len(MemberTime) - 1 - i):
        if MemberTime[j] > MemberTime[j + 1]:
            MemberTime[j], MemberTime[j + 1] = MemberTime[j + 1], MemberTime[j]
            MemberName[j], MemberName[j + 1] = MemberName[j + 1], MemberName[j]

# Output the top three members
print("First: ", MemberName[0], "with time", MemberTime[0], "seconds")
print("Second: ", MemberName[1], "with time", MemberTime[1], "seconds")
print("Third: ", MemberName[2], "with time", MemberTime[2], "seconds")

# Identify members who receive a certificate
for i in range(len(MemberTime)):
    if MemberTime[i] < 240:
        MemberCertificate.append(MemberName[i])

# Output the number of certificates to be printed
print("Number of certificates to be printed:", len(MemberCertificate))
