# PART A

"""
The part A calculates the number of months one need 
to save for making a down payment for their dream house.
The user inputs annual salary, portion to save every month and total cost of the dream house.
"""
annual_salary = int(input("Enter you annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

# portion_saved = 0.10
# total_cost = 1000000.0
# annual_salary = 120000.0
# portion_saved = 0.15
# total_cost = 500000
# annual_salary = 80000

portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary / 12
current_savings = 0
months = 0
while current_savings <= portion_down_payment:
    current_savings += monthly_salary * portion_saved + (current_savings * 0.04) / 12
    months += 1
print ("Number of months:", months)
current_savings = current_savings - portion_down_payment


"""
The part B calculates the number of months one need 
to save for making a down payment for their dream house.
The condition is that after every 6 month the monthly salary raises
by semi_annual_raise given by the user.
The user inputs annual salary, portion to save every month, semi annual raise and total cost of the dream house.
"""
# #PART B
annual_salary = int(input("Enter you annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# annual_salary = 120000
# portion_saved = 0.05
# total_cost = 500000
# semi_annual_raise = 0.03

# annual_salary = 80000
# portion_saved = 0.1
# total_cost = 800000
# semi_annual_raise = 0.03

portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary / 12
current_savings = 0
months = 0

while current_savings < portion_down_payment:
	current_savings += monthly_salary * portion_saved + (current_savings * 0.04 / 12)
	if months % 6 == 0 and months > 1:
		monthly_salary += monthly_salary * semi_annual_raise
	months += 1
print ("Number of months:", months)



#PART C



