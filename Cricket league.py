# Initialise arrays
Clubs = []
Statistics = []
Points = []

# Input and validate the number of matches played
Matches = int(input("Enter the number of matches played (max 22): "))
while Matches < 1 or Matches > 22:
    Matches = int(input("Enter the number of matches played (max 22): "))

# Input club names
for i in range(3):
    club_name = input("Enter name of cricket club: ")
    Clubs.append(club_name)
    Statistics.append([0, 0, 0])  # Initialise wins, draws, losses
    Points.append(0)  # Initialize points to 0

# Input match statistics
for i in range(3):
    print("\nEntering data for", Clubs[i])
    valid = False

    while not valid:
        wins = int(input("Enter number of matches won: "))
        draws = int(input("Enter number of matches drawn: "))
        losses = int(input("Enter number of matches lost: "))

        total = wins + draws + losses

        if total == Matches:
            valid = True
        else:
            print("Error: Total matches must equal", Matches, ". Please re-enter.")

    # Store statistics
    Statistics[i][0] = wins
    Statistics[i][1] = draws
    Statistics[i][2] = losses

    # Calculate and store points
    Points[i] = (wins * 12) + (draws * 5)

# Find the highest points
highest_points = Points[0]
for i in range(12):
    if Points[i] > highest_points:
        highest_points = Points[i]

# Find all teams with the highest points
print("\nWinning club(s):")
for i in range(12):
    if Points[i] == highest_points:
        print(Clubs[i], "- Wins:", Statistics[i][0], "- Total Points:", Points[i])
