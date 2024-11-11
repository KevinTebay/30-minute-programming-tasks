# Define arrays to store team names, statistics, and points
Teams = []
Statistics = []
Points = []

# Input the number of games played (maximum 25)
total_games = int(input("Enter the number of games each team has played (maximum 25): "))
while total_games > 25 or total_games < 1:
    total_games = int(input("Invalid input. Enter the number of games each team has played (maximum 25): "))

# Input the names of the basketball teams
for i in range(3):
    team_name = input("Enter the name of team " + str(i+1) + ": ")
    Teams.append(team_name)
    Statistics.append([0, 0, 0])  # Initialise [won, lost, tied] for each team

# Input the statistics for each team and calculate points
for i in range(3):
    print("Enter the statistics for " + Teams[i] + ":")

    # Input wins, losses, and ties, with validation
    won = int(input("Number of games won: "))
    lost = int(input("Number of games lost: "))
    tied = int(input("Number of games tied: "))

    # Validate the total number of games played
    while won + lost + tied != total_games:
        print("The total number of games does not match. Please re-enter the statistics.")
        won = int(input("Number of games won: "))
        lost = int(input("Number of games lost: "))
        tied = int(input("Number of games tied: "))

    # Store the validated statistics
    Statistics[i] = [won, lost, tied]

    # Calculate and store the points
    team_points = (won * 3) + (tied * 1)
    Points.append(team_points)

# Find the team(s) with the highest points
max_points = max(Points)
winners = []

for i in range(3):
    if Points[i] == max_points:
        winners.append(Teams[i])

# Output the results
print("Team(s) with the highest points:")
for winner in winners:
    index = Teams.index(winner)
    print("Team: " + winner + ", Wins: " + str(Statistics[index][0]) + ", Points: " + str(Points[index]))
