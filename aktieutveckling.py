import yfinance as yf
import matplotlib.pyplot as plt

#Step 1: Choose a stock
tickers = ["NVDA", "GOOG", "MSFT"]
start_date = "2020-01-01"
end_date = "2025-01-01"

plt.figure(figsize=(10, 6))

#Step 2: Fetch historical stock-course
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)

    if "Adj Close" in data.columns:
        data = data["Adj Close"]

    else:
        print("Error: Adj Close column not found, using Close instead.")
        data = data["Close"]

    plt.plot(data.index, data.values, label=ticker)

#Step 3: Visualize the stock-course

plt.title(f'{ticker} Stock Development')
plt.xlabel("Datum")
plt.ylabel("Pris (USD)")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45) #Rotates the date for better readability
plt.tight_layout()
plt.show()
