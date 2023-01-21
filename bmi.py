weight = input("What is your weight (in lbs)? ")
w = float(weight)
height = input("What is your height (in inches)? ")
h = float(height)

def calc_bmi():
    return 703 * w/pow(h,2)

bmi = calc_bmi()

def output():
    if bmi > 30:
        print("You are obese")
    elif bmi > 25:
        print("You are overweight")
    elif bmi > 18.5:
        print("You are normal")
    elif bmi < 18.5:
        print("You are underweight")

output()
