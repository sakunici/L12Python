# Interest Calculate - Year
principle_int=100
interestrate_float=2
year_float=3

yield_float=(principle_int*(interestrate_float/100)*year_float)
total_float=principle_int+yield_float
print(total_float)

# Interest Calculate - Day
principle1_int=2000
interestrate1_float=5
day1_float=90

yield1_float=principle1_int*(interestrate1_float/100)*(day1_float/365)
total1_float=yield1_float+principle1_int
print(total1_float)

# Interest Calculate - Month
p_str=input("Your Deposit Money ")
p_float=float(p_str)
int_str=input("Interest Rate is ")
int_float=float(int_str)/100
month_dep_str=input("You have been deposit (Month)  ")
month_dep_float=float(month_dep_str)/12

your_int=(p_float*int_float)*(month_dep_float)
total_money=p_float+your_int
print(f"Your Total money is: {total_money}")
print(f"You earn the interest from your deposit: {your_int}")