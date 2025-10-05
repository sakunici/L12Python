# How old are you?
year_str=input("When were you born?")
year_int=int(year_str) #Convert String to Integer
age=2025-year_int
retired_age=65
retire=retired_age-age
print("Now you are "+str(age)+" years old")
print(f"You still have {retire} years to go for the retirement")