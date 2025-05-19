import random

def get_numbers_ticket(min_value, max_value, quantity):
    # Задаємо обмеження функції
    if min_value < 1 or max_value > 1000 or quantity > (max_value - min_value + 1):
        return []

    # Генеруємо вказану кількість випадкових, унікальних чисел в заданому діапазоні і сортуємо список
    numbers = sorted(random.sample(range(min_value, max_value + 1), quantity))
    return numbers

# Перевірка на коректність введення даних
try:
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print('Excesize 2:')
    print('Your lottery numbers: ', lottery_numbers)
except NameError:
    print('Всі значення мають бути введені числом')


"""
Доопрацював функцію. Якщо параметри не відповідають заданим обмеженням, 
то функція повертає не пустий список, а повідомлення з помилкою. 
"""
# import random
#
# def get_numbers_ticket(min_value, max_value, quantity):
#
#     if min_value < 1:
#         return f'Мінімальне значення не може бути менше 1'
#     elif max_value > 1000:
#         return f'Максимальне значення не може бути більше 1000 '
#     elif quantity > (max_value - min_value + 1):
#         return f'Кількість випадкових варіантів чисел перевищує доступний діапазон'
#     elif quantity == 0:
#         return f'Кількість випадкових варіантів чисел не може дорівнювати нулю'
#     numbers = sorted(random.sample(range(min_value, max_value + 1), quantity))
#     return numbers
# try:
#     lottery_numbers = get_numbers_ticket(min_value=int(input('Enter min value: ')), max_value=int(input('Enter max value: ')), quantity=int(input('Enter quantity: ')))
#     print('Your lottery numbers: ', lottery_numbers)
# except ValueError:
#     print('Всі значення мають бути введені числом')