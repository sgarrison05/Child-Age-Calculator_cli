#!/usr/bin/python3
# by Shon Garrison
# Created on: Aug 21, 2025
# Updated on: Aug 2025

from datetime import date
import os

def get_birthdate():
   # Calculate a person's birthdate 
    today = date.today()

    # Clear the console screen for better readability
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    
    print ("\nThis application will calculate how old you are")
    print ('\n')
    print ("Today is " + today.strftime("%m/%d/%y"))
    print ('\n')

    #get user input for each part of date variable and convert it's part to integer:
    try:
        year = input("Please enter your birth year:  ")
        year = int(year)
        month = input("Please enter your birth month:  ")
        month = int(month)
        day = input("Please enter the day you were born:  ")
        day = int(day)
    except ValueError:
        print("\nInvalid input. Please enter numeric values for year, month, and day.")
        return  

    #convert input variables to date
    birth_date = date(year,month,day)

    strBirth_Date = birth_date.strftime("%m/%d/%Y")
    print ('\n')
    print ("You entered --> " + strBirth_Date)
    print ('\n')

    yearDays = 365.25

    #calculate age
    age = int((today - birth_date).days/yearDays)

    #convert to string and display
    print ("You are " + str(age) + " years old")


# Run Application ===========================================================

get_birthdate()

print("\nNow Exiting the Application...\nGoodbye")
