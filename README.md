# Leap-Year
Overview 
-This Python script works by checking if an entered input (Year)  is a leap year or not. 

Python script 
"""
The goal of the project is to create a function using "nested if" which the user inputs a year to check whether it's a leap year or not. 

"""
#Declaring the function 
def Leapyear():
 year=int(input("Enter year"))
if year%4==0 and year%100!=0:
    print(year,"is a leap year")
elif year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
#/Call the function /
Leapyear () 
