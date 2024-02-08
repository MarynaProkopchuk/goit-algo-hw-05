import re
from typing import Callable

def generator_numbers(text: str):                  # створюємо генератор
    income_list = re.findall(r"\d+\.\d+", text)    # шукаємо дійсні числа в рядку і передаємо в список
    for income in income_list:                     # перебираємо значення в списку
        income = float(income)                     # перетворюємо значення з рядка в дійсне число
        yield income

def sum_profit(text: str, func: Callable):         # створюємо функцію для обрахунку суми
    income_sum = sum(generator_numbers(text))      # підрахунок суми за допомогою генератора
    return income_sum                              # повернення результату

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,"\
    " доповнений додатковими надходженнями 27.45 і 324.00 доларів."     # задаємо аргумент функції
total_income = sum_profit(text, generator_numbers)  # викликаємо функцію обрахунку суми
print(f"Загальний дохід: {total_income}")           # виводимо результат