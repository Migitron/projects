hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#setting a variable to store total price
total_price = 0 

#for loop to add all prices prior to getting an average
for price in prices:
  total_price += price

#variable to store the average price
average_price = total_price / len(prices)

#printing out the average prices of haircuts
print('Average Haircut Price:', average_price)

#reducing the prices by $5 each
new_prices = [price -5 for price in prices]
print("New Prices:",new_prices)

#setting variable for the total revenue 
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print('Total Revenue:', total_revenue)

average_daily_revenue = total_revenue/7
print('Average Daily Revenue:', average_daily_revenue)

#using list comprehension to create a new list that only has hairstyles that are less than 30 
cuts_under_30 =[hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print('Cuts Under 30:', cuts_under_30)
