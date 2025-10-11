
w_str=input("Your Weight (kg): ")
w_float=float(w_str)
h_str=input("Your Height (m): ")
h_float=float(h_str)

def calculate_bmi(w_float,h_float):
    return(w_float/(h_float**2))
result= calculate_bmi(w_float,h_float)
print(result)