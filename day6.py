# BMI Calculation
weight_str=input("Your Weight (kg) ")
weight_float=float(weight_str)
height_str=input("Your Height (cm) ")
height_float=float(height_str)
height_in_m=height_float/100

BMI1 = weight_float / (height_in_m**2)
(print(f"Your BMI is: {BMI1}"))
# BMI Result
BMI = float(BMI1)
if BMI >=30:
    print("You are FAT!")
elif BMI >=25:
    print("You are getting FAT")
elif BMI >=23:
    print("You are overweight")
else:
    print("You are in Good Shape")

