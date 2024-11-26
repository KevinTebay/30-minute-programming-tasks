# Initialise arrays
runners = []       # 1D array to store participant names
results = []       # 2D array to store [name, time] for each participant

# Number of participants
num_runners = int(input("Enter the number of participants: "))

# Loop to collect data
for i in range(num_runners):
    name = input("Enter the runner's name: ")
    runners.append(name)  # Add name to 1D array 'runners'

    # Validate that distance is exactly 25KM
    distance = int(input("Enter the distance completed (must be 25 KM): "))
    while distance != 25:
        print("Invalid distance. This race is only for 25 KM. Please try again.")
        distance = int(input("Enter the distance completed (must be 25 KM): "))

    # Collect and round time
    time = float(input("Enter the time taken (in hours): "))
    time = round(time, 2)

    # Add name and time to 2D array 'results'
    results.append([name, time])

podium = []        # 2D array to store the top 3 runners as [name, time]
visited = []       # List to track runners already added to the podium

for rank in range(3):  # Loop 3 times to find the top 3 runners
    fastest = None
    for result in results:  # Find the runner with the fastest time not in 'visited'
        if result not in visited:  # Check if the runner is not already on the podium
            if fastest is None or result[1] < fastest[1]:  # Update the fastest
                fastest = result
    if fastest:
        podium.append(fastest)  # Add the fastest runner to 'podium'
        visited.append(fastest)  # Mark them as visited

# Display all runners and their times
print("\nResults:")
for result in results:  # Display all participants from 'results'
    print(result[0], ":", result[1], "hours")

# Display the top 3 runners
print("\nTop 3 Runners:")
for i in range(len(podium)):
    print("Rank", i + 1, ":", podium[i][0], "with a time of", podium[i][1], "hours")

