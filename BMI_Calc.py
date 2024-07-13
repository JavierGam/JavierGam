height = float(input ("What is your height (in inches): "))
weight = float(input("What is your weight in (in lbs):"))
bmi = weight * 703 / height ** 2 

if bmi < 16: 
    category = "Severely Underweight"
elif bmi < 18.4:
    category = "Undeweight"
elif bmi < 24.9:
   category = "normal"
elif bmi < 29.9:
    category = "DAYMMMMMMMM"
elif bmi < 34.9:
    category = "EXTRA DAYMMMMM"
