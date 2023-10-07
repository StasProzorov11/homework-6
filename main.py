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