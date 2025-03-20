# Initialise 2D array with sample temperature data (7 days, 24 readings each)
Temperatures = [
    [12.5, 13.0, 11.8, 10.5, 9.2, 8.8, 9.0, 11.0, 14.5, 16.0, 18.2, 19.0, 20.1, 21.5, 22.3, 21.0, 19.8, 18.2, 17.1, 15.5, 14.2, 13.0, 12.2, 11.5],  # Monday
    [11.0, 11.5, 10.8, 9.5, 8.2, 7.8, 8.0, 10.0, 13.5, 15.0, 17.2, 18.0, 19.1, 20.5, 21.3, 20.0, 18.8, 17.2, 16.1, 14.5, 13.2, 12.0, 11.2, 10.5],  # Tuesday
    [10.5, 11.0, 9.8, 8.5, 7.2, 6.8, 7.0, 9.0, 12.5, 14.0, 16.2, 17.0, 18.1, 19.5, 20.3, 19.0, 17.8, 16.2, 15.1, 13.5, 12.2, 11.0, 10.2, 9.5],  # Wednesday
    [13.0, 13.5, 12.8, 11.5, 10.2, 9.8, 10.0, 12.0, 15.5, 17.0, 19.2, 20.0, 21.1, 22.5, 23.3, 22.0, 20.8, 19.2, 18.1, 16.5, 15.2, 14.0, 13.2, 12.5],  # Thursday
    [14.5, 15.0, 14.2, 13.5, 12.2, 11.8, 12.0, 14.0, 17.5, 19.0, 21.2, 22.0, 23.1, 24.5, 25.3, 24.0, 22.8, 21.2, 20.1, 18.5, 17.2, 16.0, 15.2, 14.5],  # Friday
    [15.0, 15.5, 14.8, 13.5, 12.2, 11.8, 12.0, 14.0, 17.5, 19.0, 21.2, 22.0, 23.1, 24.5, 25.3, 24.0, 22.8, 21.2, 20.1, 18.5, 17.2, 16.0, 15.2, 14.5],  # Saturday
    [16.0, 16.5, 15.8, 14.5, 13.2, 12.8, 13.0, 15.0, 18.5, 20.0, 22.2, 23.0, 24.1, 25.5, 26.3, 25.0, 23.8, 22.2, 21.1, 19.5, 18.2, 17.0, 16.2, 15.5]   # Sunday
]

# Array of day names for reference
Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Initialise weekly statistics
MaxWeek = Temperatures[0][0]  # Assume first temperature is max
MinWeek = Temperatures[0][0]  # Assume first temperature is min
TotalWeek = 0  # Sum of all temperatures in the week
CountWeek = 0  # Count of all temperature readings

# Process each day
for i in range(7):
    MaxDay = Temperatures[i][0]  # Assume first temperature of the day is max
    MinDay = Temperatures[i][0]  # Assume first temperature of the day is min
    TotalDay = 0  # Sum of temperatures for the day

    # Process each hour in the day
    for j in range(24):
        temp = Temperatures[i][j]
        TotalDay += temp  # Add to daily total

        # Update max and min for the day
        if temp > MaxDay:
            MaxDay = temp
        if temp < MinDay:
            MinDay = temp

    # Calculate daily average and round to two decimal places
    AvDay = round(TotalDay / 24, 2)

    # Output daily statistics
    print(Days[i], "- Max Temp:", MaxDay, "Min Temp:", MinDay, "Avg Temp:", AvDay)

    # Update weekly max and min temperatures
    if MaxDay > MaxWeek:
        MaxWeek = MaxDay
    if MinDay < MinWeek:
        MinWeek = MinDay

    # Add daily total to weekly total
    TotalWeek += TotalDay
    CountWeek += 24  # 24 readings per day

# Calculate weekly average and round to two decimal places
AvWeek = round(TotalWeek / CountWeek, 2)

# Output weekly statistics
print("\nMax Temperature for the Week:", MaxWeek)
print("Min Temperature for the Week:", MinWeek)
print("Avg Temperature for the Week:", AvWeek)
