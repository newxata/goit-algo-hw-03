from datetime import datetime

# Створення функції
def get_days_from_today(date):
    # Запускаємо оператор try для винятку
    try:
        # Претворюємо параметр date у обʼєкт datetime
        date = datetime.strptime(date,'%Y-%m-%d')
        # Отримаємо поточну дату
        current_date = datetime.today()
        # Розраховуємо різницю між поточною датою та заданою датою як ціле число
        diff_date = current_date.toordinal() - date.toordinal()
        # Повертаємо наш розрахунок
        return diff_date
    # Додаємо виняток на випадок введення заданої дати у неправильному форматі
    except ValueError:
        return f'{date} invalid date format. Please enter the date in the correct format: YYYY-MM-DD'

print('Excesize 1:')
print(get_days_from_today("2024-10-01"))

print('-' * 50)