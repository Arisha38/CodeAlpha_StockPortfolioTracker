"""
CodeAlpha Python Internship - Task 2
Stock Portfolio Tracker (Simplified Version)

Calculates total investment based on hardcoded stock prices.
"""

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420,
    "NFLX": 650,
}

print("=" * 40)
print("STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable stocks:")
for symbol, price in STOCK_PRICES.items():
    print(symbol + " - $" + str(price))

portfolio = {}

print("\nEnter stock symbol and quantity.")
print("Type 'done' when finished.\n")

while True:
    symbol = input("Stock symbol: ")
    symbol = symbol.upper()
    symbol = symbol.strip()

    if symbol == "DONE":
        break

    if symbol not in STOCK_PRICES:
        print("Sorry, that stock is not in our list. Try again.\n")
        continue

    quantity_input = input("Quantity: ")
    quantity_input = quantity_input.strip()

    if quantity_input.isdigit() == False:
        print("Please enter a valid number.\n")
        continue

    quantity = int(quantity_input)

    if symbol in portfolio:
        portfolio[symbol] = portfolio[symbol] + quantity
    else:
        portfolio[symbol] = quantity

    print("Added " + str(quantity) + " share(s) of " + symbol + ".\n")

# Calculate total
total = 0
print("\n" + "=" * 40)
print("PORTFOLIO SUMMARY")
print("=" * 40)

if len(portfolio) == 0:
    print("No stocks were added.")
else:
    for symbol in portfolio:
        quantity = portfolio[symbol]
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total = total + value
        print(symbol + ": " + str(quantity) + " shares x $" + str(price) + " = $" + str(value))

    print("-" * 40)
    print("TOTAL INVESTMENT: $" + str(total))
    print("=" * 40)

    # Ask to save
    save_choice = input("\nSave summary to a text file? (y/n): ")
    save_choice = save_choice.strip().lower()

    if save_choice == "y":
        file = open("portfolio_summary.txt", "w")
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 40 + "\n")
        for symbol in portfolio:
            quantity = portfolio[symbol]
            price = STOCK_PRICES[symbol]
            value = price * quantity
            file.write(symbol + ": " + str(quantity) + " shares x $" + str(price) + " = $" + str(value) + "\n")
        file.write("-" * 40 + "\n")
        file.write("TOTAL INVESTMENT: $" + str(total) + "\n")
        file.close()
        print("Saved to portfolio_summary.txt")

print("\nThank you for using the Stock Portfolio Tracker!")
