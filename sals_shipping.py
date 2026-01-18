#Migitron
#Sal's Shipping project -codecademy

#defining variables
weight = 4.8
ground_price = 20
ground_premium = 125
drone_price = 0
cheapest = ""


#Ground Shipping
if weight == 0:
  ground_price = 0
  ground_premium = 0
elif weight <= 2:
  ground_price  += 1.50 * weight
elif (weight > 2) and (weight <= 6):
  ground_price  += 3.00 * weight
elif (weight > 6) and (weight <= 10):
  ground_price  += 4.00 * weight
else:
  ground_price  += 4.75 * weight

#Drone shipping
if weight == 0:
  drone_price = 0
elif weight <= 2:
  drone_price  += 4.50 * weight
elif (weight > 2) and (weight <= 6):
  drone_price  += 9.00 * weight
elif (weight > 6) and (weight <= 10):
  drone_price  += 12.00 * weight
else:
  drone_price  += 14.25 * weight

#figuring out which is the cheapest option
if weight == 0:
  #error for when 0lbs is entered
  cheapest += "ERROR cannot ship 0lb"
elif (ground_price < ground_premium) and (ground_price < drone_price):
  cheapest += "Ground Shipping"
elif (ground_premium < ground_price) and (ground_premium < drone_price):
  cheapest += "Ground Premium"
else:
  cheapest += "Drone Shipping"
#would want to expand this for all cases where two option could be equal
  
#print statments 
print("Ground Shipping:", ground_price)
print("Ground Shipping Premium:", ground_premium)
print("Drone Shipping:", drone_price)
print("Your cheapest option is:", cheapest)
