weight = input("What is your weight (in lbs)? ")

height = input("What is your height (in inches)? ")

def calcBMI():
    return 703 * weight/pow(height,2)

bmi = calcBMI()

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
