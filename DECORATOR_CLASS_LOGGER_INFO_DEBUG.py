class Logger:
    def __init__(self, log_level="INFO"):
        """Инициализация декоратора с параметром log_level ('INFO', 'DEBUG')."""
        self.log_level = log_level

    def __call__(self, func):
        """Вызывается при декорировании функции."""
        def wrapper(*args, **kwargs):
            if self.log_level == "DEBUG":
                print(f"[DEBUG] Вызов функции '{func.__name__}' с аргументами {args}, {kwargs}")
            elif self.log_level == "INFO":
                print(f"[INFO] Выполнение функции '{func.__name__}'")
            result = func(*args, **kwargs)
            print(f"[INFO] Функция '{func.__name__}' завершила выполнение")
            return result
        return wrapper

@Logger(log_level="DEBUG")
def add(a, b):
    return a + b

print(add(5, 3))


'''[DEBUG] Вызов функции 'add' с аргументами (5, 3), {}
[INFO] Функция 'add' завершила выполнение
8
'''

'''Как это работает?

Logger(log_level="DEBUG") передаёт "DEBUG" в __init__, сохраняя уровень логирования.
wrapper() логирует вызовы в зависимости от уровня.'''

'''
Метод	Описание
__init__	Получает и сохраняет параметры декоратора.
__call__	Вызывается при декорировании функции.
wrapper()	Выполняет логику перед и после вызова функции.
✅ Когда использовать декораторы-классы?

Если нужно сохранять состояние (например, счётчик вызовов).
Если нужны параметры (например, логирование, таймер, количество повторений).
Если декоратор должен быть гибким и расширяемым.'''