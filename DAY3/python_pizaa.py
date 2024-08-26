# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and 
# then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == 'S':
    bill += 15
    # print("Your current bill is $15")
elif size == 'M':
    bill += 20
    # print("Your current bill is $20")
elif size == 'L':
    bill += 25
    # print("Your current bill is $25")
else:
    print("You have entered a wrong input")

if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
        # print(f"You bill after adding pepperoni is {bill}")

if extra_cheese == 'Y':
    bill += 1
print(f"Your final bill is: ${bill}.")
