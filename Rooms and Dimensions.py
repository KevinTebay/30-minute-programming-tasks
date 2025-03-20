# Initialise empty lists to store room names and their dimensions
Rooms = []
Dimensions = []

# Populate the lists with default values for up to 20 rooms
for i in range(20):
    Rooms.append("")  # Empty string for room names
    Dimensions.append([0.0, 0.0, 0.0])  # List to store length, width, and area


# Prompt user to enter the number of rooms, ensuring it's between 3 and 20
Number = int(input("Enter number of rooms (3-20): "))
while Number < 3 or Number > 20:
    Number = int(input("Enter number of rooms (3-20): "))

# Input room details and calculate area
for i in range(Number):
    Rooms[i] = input("Room name: ")  # Store room name
    length = float(input("Length: "))  # Get length
    width = float(input("Width: "))  # Get width
    area = round(length * width, 2)  # Calculate and round area

    # Store dimensions in the Dimensions list
    Dimensions[i][0] = length
    Dimensions[i][1] = width
    Dimensions[i][2] = area

# Initialise variables for total area, largest and smallest room tracking
total_area = 0
largest_area = Dimensions[0][2]
smallest_area = Dimensions[0][2]
largest_room = Rooms[0]
smallest_room = Rooms[0]

# Loop through entered room data to calculate total area, largest and smallest rooms
for i in range(Number):
    total_area += Dimensions[i][2]  # Accumulate total area

    # Check for largest room
    if Dimensions[i][2] > largest_area:
        largest_area = Dimensions[i][2]
        largest_room = Rooms[i]

    # Check for smallest room
    if Dimensions[i][2] < smallest_area:
        smallest_area = Dimensions[i][2]
        smallest_room = Rooms[i]

# Calculate average area of the rooms
average_area = round(total_area / Number, 2)

# Output details of each room
for i in range(Number):
    print(Rooms[i], "- Length:", Dimensions[i][0], "m, Width:", Dimensions[i][1], "m, Area:", Dimensions[i][2], "m²")

# Output summary statistics
print("\nLargest Room:", largest_room, "with area", largest_area, "m²")
print("Smallest Room:", smallest_room, "with area", smallest_area, "m²")
print("Total Area:", total_area, "m²")
print("Average Room Size:", average_area, "m²")
