import re
from typing import Callable
from functools import reduce

def generator_numbers(text: str):  # створюємо генератор
    income_list =[float(x) for x in re.findall(r"\s\d+\.\d+\s", text)]  # шукаємо числа в рядку і передаємо в список
    for income in income_list: # перебираємо значення в списку
        yield income

def sum_profit(text: str, func: Callable):  # створюємо функцію для обрахунку суми
    income_sum = reduce(lambda x,y:x+y ,func(text))  # підрахунок суми за допомогою генератора
    return income_sum   # повернення результату

text = "Загальний дохід працівника складається з декількох частин: 1000.01  як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."   # задаємо аргумент функції
total_income = sum_profit(text, generator_numbers)  # викликаємо функцію обрахунку суми
print(f"Загальний дохід: {total_income}")           # виводимо результат
