#!/usr/bin/python
#~/workspace/Child-Age-Calculator_cli.py
# by Shon Garrison
# Created on June 16, 2025

import datetime, os

def get_birthdate():

    #get today's date:
    today = datetime.date.today()
    
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
        
    print ("This application will calculate how a child is")
    print ('\n')
    print ("Today is " + today.strftime("%m/%d/%y"))
    print ('\n')

    #get user input for each part of date variable and convert it's part to integer:
    year = input("Please enter the birth year:  ")
    year = int(year)
    month = input("Please enter the birth month:  ")
    month = int(month)
    day = input("Please enter the day the child was born:  ")
    day = int(day)

    #convert input variables to date
    birth_date = datetime.date(year,month,day)

    strBirth_Date = birth_date.strftime("%m/%d/%y")
    print ('\n')
    print ("You entered " + strBirth_Date)
    print ('\n')

    yearDays = 365.25

    #calculate age
    age = int((today - birth_date).days/yearDays)

    #convert to string and display
    print ("The child is " + str(age) + " years old")
    print ('\n')

#today = today.strftime("%m/%d/%y")
# Start Program --------------------------------------------------

def main():
    print ('\n')
    get_birthdate()
    print ('\n')
    

if __name__ == "__main__":
    main()
