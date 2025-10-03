# Hello + Your Name
user_name=input (" What is your name?")
print("Hello " + user_name)

# How old are you?
year_str=input("When were you born?")
year_int=int(year_str) #Convert String to Integer
age=2025-year_int
print("Now you are "+str(age)+" years old")

# What's your Profit?
sales_str=input("How much do you sell?")
sales_float=float(sales_str) #Convert String to Float (number with decimal)
cost_str=input("Your cost?")
cost_float=float(cost_str)
profit=sales_float-cost_float
print(f"Your Profit is {profit} ")
