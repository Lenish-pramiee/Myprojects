#Calculate the body,mass and index of the user
height=float(input("Enter the height in metres"))
weight=int(input("Enter the weight in kilograms"))
bmi=weight/(height*height)
print("The BMI of the user",bmi)
"""              
We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters

Exercise 1:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user 
        comes in underweight ,normal weight , overweight or obesity.
            i)Get user weight in kg 
            ii)Get user height in meter
            iii) Use this formula to calculate the bmi
                    BMI = weight_of_the_user/(height_of_the_user * height_of_the_user) 
                         
"""

height=float(input("Enter the height in metres"))
weight=int(input("Enter the weight in kilograms"))
bmi=weight/(height*height)
print(bmi)
