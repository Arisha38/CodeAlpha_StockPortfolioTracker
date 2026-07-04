# CodeAlpha_StockPortfolioTracker
A command-line stock portfolio tracker that calculates total investment using hardcoded stock prices. Built as part of the CodeAlpha Python Programming Internship.

## 📌 Goal

A simple command-line stock tracker that calculates total investment value based on manually defined (hardcoded) stock prices, built as part of the **CodeAlpha Python Programming Internship**.


## 📁 Project Files

| File | Purpose |
|------|---------|
| `stock_tracker.py` | Main script — stock portfolio tracker |
| `portfolio_summary.txt` | Optional auto-generated output file with the portfolio summary |


## ▶ How to Run

Uses only built-in Python modules — no installation needed.

```
python stock_tracker.py
```


## 🎮 How to Use

1. The program displays the list of available stocks and their hardcoded prices.
2. Enter a **stock symbol** (e.g. `AAPL`) and press Enter.
3. Enter the **quantity** of shares you want to add.
4. Repeat for as many stocks as you like.
5. Type `done` when you are finished entering stocks.
6. The program displays a full portfolio summary with the total investment value.
7. You can choose to save the summary to a `portfolio_summary.txt` file.


## 📊 Available Stocks (Hardcoded Prices)

| Symbol | Price ($) |
|--------|-----------|
| AAPL   | 180       |
| TSLA   | 250       |
| GOOGL  | 140       |
| AMZN   | 175       |
| MSFT   | 420       |
| NFLX   | 650       |

## 🔍 Sample Output

```
========================================
STOCK PORTFOLIO TRACKER
========================================

Available stocks:
AAPL - $180
TSLA - $250
GOOGL - $140
AMZN - $175
MSFT - $420
NFLX - $650

Enter stock symbol and quantity.
Type 'done' when finished.

Stock symbol: AAPL
Quantity: 5
Added 5 share(s) of AAPL.

Stock symbol: TSLA
Quantity: 2
Added 2 share(s) of TSLA.

Stock symbol: done

========================================
PORTFOLIO SUMMARY
========================================
AAPL: 5 shares x $180 = $900
TSLA: 2 shares x $250 = $500
----------------------------------------
TOTAL INVESTMENT: $1400
========================================

Save summary to a text file? (y/n): y
Saved to portfolio_summary.txt

Thank you for using the Stock Portfolio Tracker!
```

 

## 💡 Key Concepts Used

- **dictionary** — hardcoded stock prices
- **input/output** — user enters stock symbol and quantity
- **basic arithmetic** — total investment calculation
- **file handling** — saves the portfolio summary to a `.txt` file


## 👤 Author

Arisha Khan
CodeAlpha Python Programming Intern

