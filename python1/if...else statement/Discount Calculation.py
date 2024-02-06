price = float(input("Enter the price: "))
if price > 1500:
    discount = (price * 0.15)
    discounted = price - discount
    print(f"Final price: {discounted:.2f}")
else:
    print(f"Final price: {price:.2f}")
