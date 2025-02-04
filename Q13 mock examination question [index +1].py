Companies = ["Company1", "Company2", "Company3"]
StockPrices = [
    [10, 98, 95, 110, 120, 130, 900],  # Example prices for Company1
    [200, 190, 185, 210, 220, 230, 180],  # Example prices for Company2
    [50, 55, 45, 60, 70, 75, 40]  # Example prices for Company3
]  # Replace with actual stock prices (30 companies, 365 days each)

# Get user input for the company name
company_name = input("Enter the company name: ")

# Perform a linear search for the company index
index = -1  # Initialise index to -1 to check if the company is found
for i in range(len(Companies)):
    if Companies[i] == company_name:
        index = i
        break

# If company is not found, display an appropriate message
if index == -1:
    print("Company not found.")
else:
    # Retrieve stock prices for the found company
    prices = StockPrices[index]
    buy_day = 0  # Initialise the best buy day
    sell_day = 1  # Initialise sell day to 1 to ensure a valid sale happens after the buy day
    min_price_day = 0  # Track the day with the lowest price

    # Iterate through stock prices to find the best buy and sell days
    for j in range(1, len(prices)):
        if prices[j] < prices[min_price_day]:
            min_price_day = j  # Update the lowest price day
        if prices[j] - prices[min_price_day] > prices[sell_day] - prices[buy_day]:
            buy_day = min_price_day  # Update the best buy day
            sell_day = j  # Update the best sell day

    # Calculate the maximum profit
    max_profit = prices[sell_day] - prices[buy_day]

    # Display results with adjusted day indices
    print("Best day to buy: Day", buy_day + 1)
    print("Best day to sell: Day", sell_day + 1)
    print("Maximum profit:", max_profit)
