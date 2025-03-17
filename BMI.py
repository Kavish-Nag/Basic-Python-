#BMI = weight(kg)/height(m)^2
def body():
    weight=float(input("Emter your weight (in kg):"))
    height=float(input("Enter your height (in m):"))
    bmi=weight/(height**2)
    if bmi<=0:
        print("Invalid data, please re-enter the data")
        body()
    elif bmi<18.5:
        print("Underweight")
    elif bmi>=18.5 and bmi<24.9:
        print("Normal Weight")
    elif bmi>=24.9 and bmi<29.9:
        print("Overwight")
    else:
        print("Obese")
body()

