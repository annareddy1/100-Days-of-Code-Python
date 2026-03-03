print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Convert tip percentage to decimal multiplier:
# 12% -> 0.12, so total multiplier = 1 + 0.12 = 1.12
tip_multiplier = 1 + (tip_percent / 100)

# Total bill including tip
total_bill = bill * tip_multiplier

# Split per person
bill_per_person = total_bill / people

# Format to exactly 2 decimal places when printing (this guarantees 33.60)
print(f"Each person should pay: ${bill_per_person:.2f}")