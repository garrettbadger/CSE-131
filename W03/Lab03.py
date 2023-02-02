# 1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program will display the calendar for a given year and month. It works
#      with any year since 1753 when the gregorian calendar was adopted. 
# 4. What was the hardest part? Be as specific as possible.
#      Making sure all of the functions were working properly and sending/receiving all the data they need.
# 5. How long did it take for you to complete the assignment?
#      3.5
def main():
    month = get_month()
    year = get_year()
    display(month, year)

def get_month():
    #Gets the month from the user and validates it is a valid month.
    valid = False
    while not valid:
        month_txt = input("Please enter the month (1-12): ")
        valid = True
        if month_txt.isnumeric():
            month_num = int(month_txt)
        else:
            valid = False
        if month_num != 0 and month_num < 13:
            valid = True
        else:
            valid = False
    else:
        return month_num
    
def get_year():
    #Gets the year from the user and validates it is a valid year.
    valid = False
    while not valid:
        year_txt = input("Please enter the year (1753+): ")
        valid = True
    
        if year_txt.isnumeric():
            year_num = int(year_txt)
            if year_num < 1753:
                valid = False
        else:
            valid = False
        
    else:
        return year_num

def display(month, year):
    #Calls offset and days_month to pass to display table.
    offset = compute_offset(month, year)
    num_days_month = days_month(month, year)
    display_table(offset, num_days_month)
    

def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline


def compute_offset(month, year):
    #Using only math we figure out what the first day of a given month is.
    num_days = 0
    for year_count in range(1753, year):
        num_days += days_year(year_count)
    for month_count in range(1, month):
        num_days += days_month(month_count, year)
    return(num_days + 1) % 7


def days_year(year):
    #Returns how many days are in the given year.
    leap = is_leap_year(year)
    if leap:
        return 366
    else:
        return 365

def is_leap_year(year):
    #Determines if given year is a leap year.
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

def days_month(month, year):
    #Determines how many days are in a given month in a given year.
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    if month in thirty_one:
        return 31
    if month in thirty:
        return 30
    else:
        leap = is_leap_year(year)
        if leap:
            return 29
        else:
            return 28

if __name__ == "__main__":
    main()