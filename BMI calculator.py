def get_height():
    get_unit = str(input("height in ft or metres : "))
    get_height = float(input("height : "))
    if get_unit == 'ft':
        get_height *= 0.3048
    return get_height

def get_weight():
    get_unit = str(input("weight in ibs or kg : "))
    get_weight = float(input("weight : "))
    if get_unit == 'ibs':
        get_weight *= 0.453592
    return get_weight

def get_BMI(height, weight):
    BMI = weight/(height**2)
    return BMI

def get_BMI_status(BMI):
    if BMI < 18.5: print("you are underweight")
    elif BMI >= 18.5 and BMI <= 24.9: print("you are moderate weight")
    elif BMI >= 25 and BMI <= 29.9: print("you are overweight")
    elif BMI >= 30: print("you are obese")

h = get_height()
w = get_weight()
BMI = get_BMI(h,w)
print(BMI)
print(get_BMI_status(BMI))