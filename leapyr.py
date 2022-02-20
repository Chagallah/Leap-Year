def LeapYear():
    year = int(input("Enter the year: "))

    #Divide the year by 400

    if year % 400 == 0:
        print("Year is a leap year")
    elif year % 4 and year % 100!=0:
        print("Year is a leap year")
    else:
        print("Year is not a leap year")
LeapYear()
