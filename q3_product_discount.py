prices = [500, 1200, 2500, 800, 1500]

# a) A pure function returns a result without changing the input.
def discounted_price(price):
    if price > 1000:
        return price * 0.80
    return price

# c) Identify products costing more than ₹1,000.
eligible_prices = list(filter(lambda price: price > 1000, prices))

# b) Apply the discount to each product price.
revised_prices = list(map(discounted_price, prices))

print("Original prices:", prices)
print("Products costing more than ₹1,000:", eligible_prices)
print("Prices after discount:", [round(price, 2) for price in revised_prices])

# d) The function only calculates and returns a value. It never edits the
# original list, so the original prices remain unchanged.
