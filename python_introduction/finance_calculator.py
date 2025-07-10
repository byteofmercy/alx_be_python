# Let's help the user with money calculations!

# Ask them how much money they earn every month
income = float(input("Enter your monthly income: "))

# Ask them how much they spend
expenses = float(input("Enter your total monthly expenses: "))

# Monthly savings = income - expenses
monthly_savings = income - expenses

# Projected savings in a year = 12 months of saving + 5% interest
yearly_savings = monthly_savings * 12
interest = yearly_savings * 0.05
projected_savings = yearly_savings + interest

# Show them the results!
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_savings) + ".")
