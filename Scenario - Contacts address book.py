Contacts = []
for i in range(20):
    row = []
    for j in range(2):
        row.append("")
    Contacts.append(row)

CurrentSize = 0

while True:
    print("\nMenu:")
    print("1. Enter new contact details")
    print("2. Display all contact details")
    print("3. Delete all contact details")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if CurrentSize >= 20:
            print("The contact list is full. Cannot add more contacts.")
        else:
            num_contacts = int(input("How many contacts do you want to add (1-5)? "))
            if num_contacts < 1 or num_contacts > 5:
                print("Invalid number. You can only add between 1 and 5 contacts at a time.")
            elif CurrentSize + num_contacts > 20:
                print("Adding these contacts would exceed the maximum limit of 20.")
            else:
                for i in range(num_contacts):
                    name = input("Enter contact name (last name, first name): ")
                    phone = input("Enter contact phone number: ")
                    Contacts[CurrentSize][0] = name
                    Contacts[CurrentSize][1] = phone
                    CurrentSize += 1
                if CurrentSize > 1:
                    # Bubble sort to sort the contacts by name
                    for i in range(CurrentSize - 1):
                        for j in range(CurrentSize - i - 1):
                            if Contacts[j][0] > Contacts[j + 1][0]:
                                Contacts[j], Contacts[j + 1] = Contacts[j + 1], Contacts[j]
                print("Contacts added successfully.")

    elif choice == "2":
        if CurrentSize == 0:
            print("The contact list is empty.")
        else:
            print("\nContacts:")
            for i in range(CurrentSize):
                print(Contacts[i][0], Contacts[i][1])

    elif choice == "3":
        if CurrentSize == 0:
            print("The contact list is already empty.")
        else:
            for i in range(CurrentSize):
                Contacts[i][0] = ""
                Contacts[i][1] = ""
            CurrentSize = 0
            print("All contacts have been deleted.")

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
