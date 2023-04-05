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


# def compute_offset(month, year):
#     amount_days = 0
#     for i in range(1753, year):
#         if is_leap_year(year):
#             amount_days += 366
#         else: amount_days += 365
#     for i in range(month):
#         amount_days = number_days_in_month(month)
#     dow = amount_days % 7


# def number_days_in_month(month):
#     pass
# def is_leap_year(year):
#     pass

# dow = 8560 % 7
# print(dow)

# def compute_tax(income):
#     ''' Compute federal income tax based on income. '''
#     # incomes under $61,300 first
#     if income < 61300.00:

#         # 15% tax bracket.
#         if income >= 15100.00:
#             return round(1510.00 + 0.15 * (income - 15100.00), 2)
#         # 0% tax bracket.
#         elif income <= 0.00:
#             return 0.00
#         # 10% tax bracket.
#         else:
#             return round(income * 0.10, 2)

#     # incomes over $61,300 next
#     else:
#         # 25% tax bracket.
#         if income < 123700.00:
#             return round(8440.00 + 0.25 * (income - 61300.00), 2)
#         # 28% tax bracket.
#         elif income < 188450.00:
#             return round(24040.00 + 0.28 * (income - 123700.00), 2)
#         # 33% tax bracket.
#         elif income < 336550.00:
#             return round(42170.00 + 0.33 * (income - 188450.00), 2)
#         # 35% tax bracket.
#         else:
#             return round(91043.00 + 0.35 * (income - 336550.00), 2)
#     assert(False)

# def driver_compute_tax():
#     while True:
#         income = float(input('Please enter income: '))
#         tax = compute_tax(income)
#         print(f'Your tax for your income of ${income} is ${tax}')

# driver_compute_tax()

# def sort_list(u_list):
    
#     d_list = list(u_list)
#     sub_list_1 = 0
#     sub_list_2 = 0
#     not_sorted = True
#     while not_sorted:
#         for i in range(0, len(u_list)):
#             if u_list[i] < u_list[i+1]:
#                 sub_list_1 += 1
#             else:
#                 break
#         sub_list_2 = sub_list_1+1
#         for x in range(sub_list_1+1, len(u_list)):
#             if u_list[x] < u_list[x+1]:
#                 sub_list_2 +=1
#             else:
#                 break
#         for i in range(sub_list_1,sub_list_2+1):
#             if u_list[i] < u_list[sub_list_1+(i+1)]:
#                 d_list[i] = u_list[i]
#             else:
#                 d_list[i] = u_list[sub_list_1+(i+1)]


#     print(d_list)
#     # return sorted_list

# unsorted_list = [86,59,89,6,99,67,38,19,85,3]
# sort_list(unsorted_list)

# def sum_powers_of_two(num_pow):
#     if num_pow == 0:
#         return 1
#     else:
#         return (2**num_pow), sum_powers_of_two(num_pow-1)
    
# print(sum_powers_of_two(3))

# def display_names(names, i=0):
#     if i == len(names):
#         return
#     else:
#         print(names[i])
#         i+=1
#         display_names(names, i)

# display_names(['George', 'Jerry', 'Kramer', 'Elaine'])

# def sumTheDigits(number):
#    if number == 0:
#       return 0
#    else:
#       return number % 10 + sumTheDigits(number / 10)
   
# print(sumTheDigits(11))

# def sum_digits(number):
#    new_num = 0
#    while number != 0:
#       new_num += (number % 10)
#       number = number / 10
#    return new_num
# print(sum_digits(11))

# def compute_tax(cost):
#    tax = cost * 0.078
#    cost += tax
#    return round(cost,2)

# print(compute_tax(5))
# print(compute_tax(0))
# print(compute_tax(1.005))

# def prompt():
#    '''Prompt the user for a decimal number'''
#    number = -1
#    while number < 0:
#       try:
#          number = int(input('Please enter a whole number: '))
#       except ValueError:
#          print('Only enter whole numbers.')
#    return number

# print(prompt())
from itertools import zip_longest

# Define a list with items of different lengths
shopping_list = [('Bib Shorts', 'Clothing', '$92.50'), ('Roubaix', 'Bicycle', '$3,599.99'), ('Cycling Computer', 'Accessories', '$394.99'),
               ('Helmet', 'Accessories', '$299.99'), ('Road Shoes', 'Shoes', '$144.99'), ('700c presta tube', 'Accessories', '$5.25'),
               ('Jersey', 'Clothing', '$25.99'), ('Mult-Function Tool', 'Accessories', '$22.99'), ('Gloves', 'Accessories', '$8.99'), 
               ('Cleats', 'Shoes', '$15.99'), ('Power Pedals', 'Accessories', '$999.99'), ('Socks', 'Clothing', '$8.50')]

# Determine the maximum length of any item in the list
# max_length = max(len(item) for item in shopping_list)

# # Use zip_longest to iterate over the items in the list
# # and pad shorter items with spaces to make them the same length
# for item in zip_longest(*shopping_list, fillvalue=' ' * max_length):
#     for i in range(3):
#     # Use string formatting to print each item with a fixed width
#          print("{:<{}}".format(item[0][i], max_length), end=' ')
#          # print("{:<{}}".format(item[1], max_length), end=' ')
#          # print("{:<{}}".format(item[2], max_length), end=' ')
#          # print("{:<{}}".format(item[3], max_length), end=' ')
#          # print("{:<{}}".format(item[4], max_length), end=' ')



# for i in range(len(shopping_list)):
#     print()
#     for x in range(3):
        
#       print(shopping_list[i][x], end="   ")
# def is_accessory(item):
#      for i in item:
#           if i == 'Accessories':
#                return True
     
# new_list = filter(lambda x: x == 'Accessories', shopping_list)
# print(list(new_list))
# from functools import reduce

# def price_adjust(item):
#      for i in item:
#           if i.count('$') > 0:
#                i = i.replace('$', '')
#                i = i.replace(',', '')
#                num = round(float(i) - (float(i) * .2), 2)
#                i = '$' + str(num)
#                return i
               
# adjusted_list = map(price_adjust, shopping_list)
# print(list(adjusted_list))

from functools import reduce

def price_adjust(item1, item2):
      
      for x in item2:
            if x.count('$') > 0:
               x = x.replace('$', '')
               x = x.replace(',', '')
               num2 = float(x)
      return item1 + num2
               
result = reduce(price_adjust, shopping_list, 0)
print(round(result,2))