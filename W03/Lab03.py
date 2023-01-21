def main():
    month = get_month()
    year = get_year()
    display(month, year)

def get_month():
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
    valid = False

    while not valid:
        year_txt = input("Please enter the year (1753+): ")
        valid = True
    
        if year_txt.isnumeric():
            year_num = int(year_txt)
        else:
            valid = False
        if year_num < 1753:
            valid = False
    else:
        return year_num

def display(month, year):
    offset = compute_offset(month, year)
    num_days_month = days_month(month, year)
    display_table(num_days_month, offset)
    

def display_table(num_days, offset):
    print("SU MO TU WE TH FR SA")
    for i in range(0, offset):
        print("    ")
    for dom in range(1, num_days):
        print(dom)
        offset +=1
        if offset % 7 == 0:
            print('\n')
    if offset % 7 != 0:
        print('\n')


def compute_offset(month, year):
    num_days = 0
    for year_count in range(1753, year):
        num_days += days_year(year_count)
    for month_count in range(1, month):
        num_days += days_month(month_count, year)
    return(num_days + 1) % 7


def days_year(year):
    leap = is_leap_year(year)
    if leap:
        return 366
    else:
        return 365

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

def days_month(month, year):
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