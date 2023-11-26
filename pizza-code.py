print("Thank you for choosing Python Pizza Deliveries!")

bill = 0
size = input("What size pizza do you want? S, M, or L \n")

if size == "S":
  bill = 15
elif size == "M":
  bill = 20
else:
  bill = 25

add_pepperoni = input("Do you want pepperoni? Y or N \n")
if add_pepperoni == "Y":
  bill += 3


extra_cheese = input("Do you want extra cheese? Y or N \n")
if extra_cheese == "Y":
  bill += 1

print(f"your final bill is {bill} ")