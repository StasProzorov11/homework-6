# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.
# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр, список також передається як параметр. Функція повертає новий список, який містить отримані результати.

# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
# try:
#  def product_of_numbers(mass):
#     product_numbers = 1
#     for i in mass:
#      product_numbers *= i
#     return product_numbers

#  mass = [int(s) for s in input("Enter whole numbers separated by spaces : ").split()]
#  print(f"List : {mass}")
#  print(f"Product of numbers : {product_of_numbers(mass)}")
# except ValueError as error:
#     print(error)

# v2
# try:
#  def product_of_numbers(mass):
#     product_numbers = 1
#     for i in mass:
#      product_numbers *= i
#     return product_numbers

#  mass = [1, 2, 3, 4, 5]
#  print(f"List : {mass}")
#  print(f"Product of numbers : {product_of_numbers(mass)}")
# except ValueError as error:
#   print(error)

# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
# try:
#  def find_min(mass):
#     number_min = mass[0]
#     for number in mass:
#         if number < number_min:
#             number_min = number
#     return number_min
#  mass = [int(s) for s in input("Enter whole numbers separated by spaces : ").split()]
#  print(f"List : {mass}")
#  print(f"Minimum in the list of integers : {find_min(mass)}")
# except ValueError as error:
#   print(error)

# v2
# try:
#  def find_min(mass):
#     number_min = mass[0]
#     for number in mass:
#         if number < number_min:
#             number_min = number
#     return number_min
#  mass = [1, 2, 3, 4, 5]
#  print(f"List : {mass}")
#  print(f"Minimum in the list of integers : {find_min(mass)}")
# except ValueError as error:
#   print(error)

# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
# try:
#  def prime_numbers(mass):
#      count = 0
#      for num in mass:
#          if num < 2:
#              continue
#          else:
#              for i in range(2, num):
#                  if num % i == 0:
#                      break
#              else:
#                  count += 1
#                  print("Prime numbers in a list :",num)
#      return count
#  mass = [int(s) for s in input("Enter whole numbers separated by spaces : ").split()]
#  print(f"List : {mass}")
#  print(f"The number of primes in the list of integers : {prime_numbers(mass)}")
# except ValueError as error:
#   print(error)
# v2
# try:
#  def prime_numbers(mass):
#      count = 0
#      for num in mass:
#          if num < 2:
#              continue
#          else:
#              for i in range(2, num):
#                  if num % i == 0:
#                      break
#              else:
#                  count += 1
#                  print("Prime numbers in a list :",num)

#      return count
#  mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#  print(f"List : {mass}")
#  print(f"The number of primes in the list of integers : {prime_numbers(mass)}")
# except ValueError as error:
#   print(error)

# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.
# try:
#  def delete_number(numbers, number_to_delete):
#    count = 0
#    for i in numbers.copy():
#      if i == number_to_delete:
#        numbers.remove(i)
#        count += 1
#    return count
#  initial_numbers = [int(s) for s in input("Enter whole numbers separated by spaces : ").split()]
#  number = int(input("Enter the number you want to delete : "))
#  print(f'Number of numbers removed : {delete_number(initial_numbers, number)}')
#  print(f"Remaining numbers : {initial_numbers}")
# except ValueError as error:
#   print(error)

# v2
# try:
#  def delete_number(numbers, number_to_delete):
#    count = 0
#    for i in numbers.copy():
#      if i == number_to_delete:
#        numbers.remove(i)
#        count += 1
#    return count
#  initial_numbers = [1, 2, 3, 3, 3, 4, 5]
#  number = (3)
#  print(f'Number of numbers removed : {delete_number(initial_numbers, number)}')
#  print(f"Remaining numbers : {initial_numbers}")
# except ValueError as error:
#   print(error)

# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
# try:
#  def combine_scroll(scroll1, scroll2):
#   combined = scroll1 + scroll2
#   return combined
#  scroll1 = [int(s) for s in input("Enter whole numbers separated by spaces : ").split()]
#  scroll2 = [int(s) for s in input("Enter whole numbers separated by spaces : ").split()]
#  combined_list = combine_scroll(scroll1, scroll2)

#  print(f"First list : {scroll1}")
#  print(f"Second list : {scroll2}")
#  print(f"List Combination Result : {combined_list}")
# except ValueError as error:
#   print(error)

# v2
# try:
#  def combine_scroll(scroll1, scroll2):
#   combined = scroll1 + scroll2
#   return combined
#  scroll1 = [1, 2, 3, 4, 5]
#  scroll2 = [6, 7, 8, 9, 10]
#  combined_list = combine_scroll(scroll1, scroll2)
#  print(f"First list : {scroll1}")
#  print(f"Second list : {scroll2}")
#  print(f"List Combination Result : {combined_list}")
# except ValueError as error:
#   print(error)

# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр, список також передається як параметр. Функція повертає новий список, який містить отримані результати.
# try:
#  def produce_a_degree(scroll, degree):
#   result = []
#   for i in scroll:
#     result.append(i**degree)
#   return result

#  numbers = [int(s) for s in input("Enter whole numbers separated by spaces : ").split()]
#  degrees = produce_a_degree(numbers, 3)
#  print(f"Result of exponentiation {degrees}")
# except ValueError as error:
#   print(error)

# v2
# try:
#  def produce_a_degree(scroll, degree):
#   result = []
#   for i in scroll:
#     result.append(i**degree)
#   return result

#  numbers = [1, 2, 3, 4, 5]
#  degrees = produce_a_degree(numbers, 3)
#  print(f"Result of exponentiation {degrees}")
# except ValueError as error:
#   print(error)