# Calculate Tip and share bills
print(" Welcome to Northern Resturant")

invoice_str=input("How much is the bill? ")
invoice_float=float(invoice_str)
tip_str=input("How many percent for Tip?")
tip_float=float(tip_str)
people_str=input("How many people?")
people_float=int(people_str)

pay=(invoice_float-(tip_float/100))/people_float

print(f"invoice : {invoice_float}, + tip : {tip_float}%, we have {people_float} people")
print(f"So We pay {pay}  per person")