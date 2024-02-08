def caching_fibonacci():        # створюємо функцію для чисел ряду Фібоначчі
    cache = {}                  # створюємо порожній словник для кеш пам'яті
    def fibonacci(n):           # створюємо фукцію для визначення чила з ряду Фібоначчі
        if n <= 0:              # перевірка умови коли число = 0 та 1 відповідно
              return 0
        elif n==1:
              return 1
        else:                   
            if n not in cache:   # умова при якій число ще не знаходиться в кеш пам'яті
                cache[n] = fibonacci(n-1) + fibonacci(n-2) # визначення числа за умови, що воно !=1 та !=0
                return cache[n]  # повернення числа з ряду Фібоначчі та внесення числа в кеш
            else:
                return cache[n]  # повернення числа з кеш пам'яті
    return fibonacci             # повернення чисел внесених в кеш

fib = caching_fibonacci()        # Отримуємо функцію Фібоначчі
print(fib(10))  # Використовуємо функцію Фібоначчі для обчислення чисел 
print(fib(15))  # Використовуємо функцію Фібоначчі для обчислення чисел 