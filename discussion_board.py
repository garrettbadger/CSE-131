# def main():
#     fahrenheit = getTemperature()
#     celsius = convert(fahrenheit)
#     display(celsius)

# def getTemperature():
#     return 68 #Or this could be input from user

# def convert(fahrenheit):
#     celsius = (fahrenheit - 32) / 1.8
#     return celsius

# def display(celsius):
#     print(f'The temperature in celsius is {celsius} degrees.')

# if __name__ == "__main__":
#     main()


def compute_offset(month, year):
    amount_days = 0
    for i in range(1753, year):
        if is_leap_year(year):
            amount_days += 366
        else: amount_days += 365
    for i in range(month):
        amount_days = number_days_in_month(month)
    dow = amount_days % 7


def number_days_in_month(month):
    pass
def is_leap_year(year):
    pass

dow = 8560 % 7
print(dow)