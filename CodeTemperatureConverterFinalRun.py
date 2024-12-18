#This program converts Fahrenheit to Celcius and vice versa

print ("Welcome to Mel's Temperature Converter")




#1. Enter the temperature you wish to convert

fTemp = float(input("Enter a Temperature:  "))

#2. Enter if what you like to convert 
sAnswer = input("Is the Temp F for Fahrenheit or C for Celsius?  ").upper()

#3.Calculations with if and else to provide all outcomes for the program.

if sAnswer != 'F' and sAnswer != 'C':
 print("Please enter C or F")
 raise SystemExit

if sAnswer == 'C':
    if fTemp <= 100:
        fConvertF = ((9.0/5.0)* fTemp) + 32
        print(f"The Farhenheit equivalent is:  {fConvertF:.1f}")     
    else:  
        print("Temp can not be > 100")

else: 
    if fTemp <= 212:
        fConvertC = (5.0/9)*(fTemp - 32)
        print(f"The Celcius equivalent is:  {fConvertC:.1f}")     
    else:  
        print("Temp can not be > 212")

