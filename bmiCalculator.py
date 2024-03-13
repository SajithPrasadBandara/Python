def bmi_cal(mass,height):
  
 #centimeters convert to meters
    height_in_meter = height/100

  #BMI Calculation
    bmi = mass/(height_in_meter**2)
    
    if bmi > 0:
        print("Your BMI : "+str(bmi))
        if bmi < 18.5:
            print("You are underweight.")
        elif bmi < 24.9:
            print("You are normal weight.")
        elif bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    else:
        print("Enter valid inputs.")
        
        
mass = int(input("Enter your weight(kg) : "))
height = int(input("Enter your height(cm) : "))

bmi_cal(mass,height)
 
