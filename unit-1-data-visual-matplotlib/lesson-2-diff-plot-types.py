# Simple Bar Chart

#import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)
plt.show()

# Simple Bar Chart II

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.show()

# Side-By-Side Bars

def create_x(t, w, n, d):
    return [t * x + w * n for x in range(d)]


drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

# Use create_x to make store1_x
store1_x = create_x(2, 0.8, 1, 6)
print store1_x
plt.bar(store1_x, sales1)

# Use create_x to make store2_x
store2_x = create_x(2, 0.8, 2, 6)
print store2_x
plt.bar(store2_x, sales2)

plt.show()

# Stacked Bars

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(drinks)), sales1)
plt.bar(range(len(drinks)), sales2, bottom=sales1)

plt.legend(["Location 1", "Location 2"])

plt.show()

# Error Bars

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.1*e for e in ounces_of_milk]

# Plot the bar graph here
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)
plt.show()

# Fill Between

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

#your work here
plt.plot(months, revenue)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

y_lower = [i - .1*i for i in revenue]
y_upper = [i + .1*i for i in revenue]
plt.fill_between(months, y_lower, y_upper, alpha=0.2)
plt.show()

# Pie Chart

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here
plt.pie(payment_method_freqs)
plt.axis('equal')
plt.show()

# Pie Chart Labeling

plt.pie(payment_method_freqs, autopct='%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names)
plt.show()

# Histogram

"""
from script import sales_times

plt.hist(sales_times, bins=20)

plt.show()

# Multiple Histograms

from script import sales_times2

plt.hist(sales_times1, bins=20, alpha=0.4, normed=True)
#plot your other histogram here
plt.hist(sales_times2, bins=20, alpha=0.4, normed=True)

plt.show()
"""
