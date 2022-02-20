def LeapYear():
    year = int(input("Enter year"))

    if year % 400 == 0:
        print("Leap year")

    else:
        print("not leap year")

LeapYear()
