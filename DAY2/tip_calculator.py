print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

final_op = ((bill * (tip/100)) + bill)/people
print(f"The cost per person is: {round(final_op,2)}")