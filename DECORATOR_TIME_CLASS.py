import time

class Timer:
    def __init__(self, unit="s"):
        """Декоратор с параметром unit ('s' - секунды, 'ms' - миллисекунды)."""
        self.unit = unit

    def __call__(self, func):
        """Вызывается при декорировании функции."""
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            if self.unit == "ms":
                elapsed *= 1000  # Перевод в миллисекунды
            print(f"[*] Функция '{func.__name__}' выполнена за {elapsed:.3f} {self.unit}")
            return result
        return wrapper  # Возвращаем обёрнутую функцию

@Timer(unit="ms")
def slow_function():
    time.sleep(1)
    print("Функция выполнена!")

slow_function()

'''Функция выполнена!
[*] Функция 'slow_function' выполнена за 1002.345 ms

Как это работает?

@Timer(unit="ms") передаёт "ms" в __init__, сохраняя параметр unit.
wrapper() замеряет время, переводит его в ms, если нужно, и выводит результат.
'''