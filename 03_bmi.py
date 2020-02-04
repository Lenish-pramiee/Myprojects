class Mybmi:
  height=float(input("Enter the height in metres"))
  weight=int(input("Enter the weight in kilograms"))
  bmi=weight/(height*height)
  print("The BMI of the user",bmi)
  if bmi<=15:
    print("The user is under weight")
  elif (bmi>15 and bmi<=20):
    print("The user is normal")
  else:
     print("obese")
if __name__ == '__main__':
    a = Mybmi()