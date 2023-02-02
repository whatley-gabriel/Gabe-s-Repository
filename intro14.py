totalCost = int(input("Enter the amount due in pennies: "))
customerPaid = int(input("Enter the amount received from the customer in pennies: "))

# Determine change amount
changeAmount = customerPaid - totalCost

dollars = (changeAmount//100)
changeAmount = changeAmount - dollars*100
quarters = (changeAmount//25)
changeAmount = changeAmount - quarters*25
dimes = (changeAmount//10)
changeAmount = changeAmount - dimes*10
nickels = (changeAmount//5)
changeAmount = changeAmount - nickels*5
pennies = (changeAmount)

# Display change due
print("Give the following change to the customer:")
print( dollars, "dollars,", quarters, "quarters,", dimes, "dimes,", nickels, "nickels and", pennies, "pennies")