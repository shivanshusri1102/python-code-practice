a = int(input("Enter the weight of a peron: "))
b = float(input("Enter the height of a person: "))
BMI = a/(b * b)
print(BMI)

if 17 <= BMI <= 18.5:
    print("Mild Thinness")
elif 18.5 <= BMI <= 25 :
    print("Normal Weight")
elif 25 <= BMI <= 30:
    print("OverWeight")
    