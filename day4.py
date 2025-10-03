# BMI Calculation
weight_str=input("Your Weight (kg) ")
weight_float=float(weight_str)
height_str=input("Your Height (cm) ")
height_float=float(height_str)
height_in_m=height_float/100

BMI = weight_float / (height_in_m**2)
(print(f"Your BMI is: {BMI}"))

