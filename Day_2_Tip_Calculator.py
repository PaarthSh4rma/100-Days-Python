"""
100 Days of Code - Python
Day 2 - Tip Calculator
"""
print("Welcome to the Tip Calculator!")

# get input from user
bill = float(input("What was the total bill? $"))
percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

# display amount per person
print(f"Each person will be paying ${round(((bill * (1 + (percent/100))) / people), 2)}")

