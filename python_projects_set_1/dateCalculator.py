#Rohit Jaisinghani
#Date Calculator
#v1.1
#This is a project I worked on during a udacity course. I decided to take it
#a little further and implement user input in the program. I also intend to allow
#the program to count days going forward or backward on the gregorian calander
#for my next version

def daysInMonth(year,month):
#This function determines how many days are in the inputted month. It accounts
#for leap years as well.
    if month == 2:
        if isLeapYear(year) != False:
            days = 29
        else:
            days = 28
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        days = 31
    else:
       days = 30
    return days

def nextDay(year, month, day):# This function starts at a date and then returns the next
#date. i.e. if the input was 1999,11,27, the output would be 1999,11,28

    if day < daysInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def isLeapYear(year):#This function checks if the given year is a leap year
#I had to look up the formula for leap year calculation to be precise
    if year % 4 == 0:
        return True
    else:
        return False

def dateIsBefore(year1, month1, day1, year2, month2, day2):
#This helper function is used to make sure date 1 is before date 2

    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#This function utilizes the previous functions to count the days in between
#the two dates. It uses an assert to assure that our output is valid otherwise
#we would get a failure as a result. This avoids outputs that do not make sense
#with the current conditions.

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def main():#Main function to get inputs for date and output the result.
    y1 = int(input("Enter year for date 1: \n"))
    m1 = int(input("Enter month for date 1: \n"))
    d1 = int(input("Enter day for date 1: \n"))
    y2 = int(input("Enter year for date 2: \n"))
    m2 = int(input("Enter month for date 2: \n"))
    d2 = int(input("Enter day for date 2: \n"))
    print("Days between date and date two: " + str(daysBetweenDates(y1,m1,d1,y2,m2,d2)) + " day(s)")
main()#Call to main 
