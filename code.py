def dataInput():# a function made to ask the weight,height and age from the user. Hence the name dataInput
    while True:#will run till the condition is matched in the code below, 
        try:#to check if the user has given integer data and not other for of data
            weight=float(input("Enter your weight in Kg: "))
            break
        except:
            print("Enter valid weight.")
    while True:
        try:
            height=float(input("Enter your height in cm: "))
            break
        except:
            print("Enter valid height.")
    while True:
        try:
            age=float(input("Enter your age in years: "))
            break
        except:
            print("Enter valid age.")
    return weight, height, age
def gender():#making a new function to ask gender 
    sex=input("Choose your gender. Type ´m´ for male and ´f´ for female: ")
    if sex=="m" or sex=="M":
        x,y,z=dataInput()
        BMR= (88.362 + 13.397*x + 4.799*y - 5.677*z)
    elif sex=="f" or sex=="F":
        x,y,z=dataInput()
        BMR=  (447.593 + 9.247*x + 3.098*y - 4.330*z)
    else:
        print("Invalid input!!! Please try again.")
        return gender()#recursion if the data input is not between two possible inputs
    return BMR#returning BMR to gain access of BMR to calculate kiCa in the next function 
def levOfExe(BMR):
    print("0-Little to no exercise")
    print("1-Light exercise (1–3 days per week)")
    print("2-Moderate exercise (3–5 days per week)")
    print("3-Heavy exercise (6–7 days per week)")
    print("4-Very heavy exercise (twice per day, extra heavy workouts)")
    print("0,1,2,3,4 are the codes of the level of exercise.")
    while True:
        exe=int(input("Choose your level of execrise through code: "))
        if exe==0:
            kiCa=  BMR*1.2
            break
        elif exe==1:
            kiCa= BMR*1.375
            break
        elif exe==2:
            kiCa= BMR*1.55
            break
        elif exe==3:
            kiCa= BMR*1.725
            break
        elif exe==4:
            kiCa= BMR*1.9
            break
        else:
            print("Invalid data. Please choose from the above")
    return kiCa  
a=gender()#initiating the entire code and stores the BMR in the a
b=levOfExe(a)#calling the levOfExe function and then passes the resultred BMR as a parsmeter and further calculates the kiCa
print("Your Basal Metabolic Rate is: " + str(a))#keeping in str to print entire code as string can not be print with float
print("Your daily required kilocalories intake is: "+ str(b)+" Kilocalories")
    
