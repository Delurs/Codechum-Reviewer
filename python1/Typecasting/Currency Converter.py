USD = float(input("Enter the amount in USD: "))
rate = float(input("Enter the exchange rate: "))
exchange_rate = int(USD * rate)
print(f"{USD:.2f} USD is equivalent to {exchange_rate} in the foreign currency.")
