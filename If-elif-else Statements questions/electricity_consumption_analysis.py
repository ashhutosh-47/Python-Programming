# Q2. Electricity Consumption Analysis (K3)
# An electricity company calculates bills using slab-wise rates.
# Write a program that accepts units consumed, calculates the bill and alerts if usage is 300 units.
# Electricity units	   Rate
# First 100	         ₹5/unit
# Next 100	         ₹7/unit
# Above 200	         ₹10/unit

unit_consumed = float(input("Enter Consumed Units = "))

if unit_consumed >= 300:
    print("Alerts")
elif unit_consumed <= 100:
    Rate = unit_consumed * 5
    print("Total Bill = ", Rate)
elif unit_consumed <= 200:
    Rate = 100 * 5 + (unit_consumed - 100) * 7
    print("Total Bill = ", Rate)
else:
    Rate = 100 * 5 + 100 * 7 + (unit_consumed - 200) * 10
    print("Total Bill = ", Rate)
