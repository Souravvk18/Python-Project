# The Body Mass Index or BMI is calculated from weight and height of a Person.


Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:("enter valid details")

'''
Enter your height in centimeters: 175
Enter your Weight in Kg: 56
your Body Mass Index is:  18.285714285714285
you are underweight

Enter your height in centimeters: 170
Enter your Weight in Kg: 60
your Body Mass Index is:  20.761245674740486
you are Healthy

'''