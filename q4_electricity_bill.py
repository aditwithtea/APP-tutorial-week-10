from functools import reduce

consumption = [8, 12, 9, 15, 11, 7]
RATE_PER_UNIT = 6

# a) Identify days when consumption exceeded 10 units.
high_consumption_days = list(filter(lambda units: units > 10, consumption))

# b) Calculate the electricity cost for each day's consumption.
daily_costs = list(map(lambda units: units * RATE_PER_UNIT, consumption))

# c) Calculate total electricity consumption.
total_consumption = reduce(lambda total, units: total + units, consumption, 0)

# d) Pure function: calculate the bill without modifying the input data.
def electricity_bill(units_list, rate=RATE_PER_UNIT):
    return sum(map(lambda units: units * rate, units_list))

print("Consumption above 10 units:", high_consumption_days)
print("Daily costs:", daily_costs)
print("Total electricity consumption:", total_consumption, "units")
print("Total electricity bill: ₹", electricity_bill(consumption))
print("Original consumption data:", consumption)
