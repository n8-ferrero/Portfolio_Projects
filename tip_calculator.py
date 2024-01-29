
'''Tip calculator to split bill
written by Nate Ferrero - 1/12/2024'''

print("Welcome to the tip calculator\n")

# Input validation function
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

bill = get_float_input("What is the final bill? $")
tip_percentage = get_float_input("What % tip would you like to leave? ")
people = get_float_input("How many people will this be divided between? ")

# Calculate total bill and split bill
corrected_tip = tip_percentage / 100
total_bill = (bill * corrected_tip) + bill
split_bill = total_bill / people

# Display results
print(f"The total bill with tip included is ${total_bill:,.2f}")
print(f"Each person needs to pay ${split_bill:,.2f}")
