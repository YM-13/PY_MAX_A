from functools import wraps
import hashlib
from collections import OrderedDict

def cache_decorator(max_buckets):
    """
    Кеширующий декоратор с ограничением на количество записей (бакетов) в кеше.

    Args:
        max_buckets (int): Максимальное количество элементов в кеше.

    Returns:
        Обёрнутая функция с кешированием.
    """
    def decorator(func):
        cache = OrderedDict()  # Используем OrderedDict для контроля порядка вставки

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Преобразование изменяемых аргументов в неизменяемые
            immutible_args = tuple([tuple(arg) if isinstance(arg, list) else arg for arg in args])
            immutible_kwargs = tuple(sorted((k, v) for k, v in kwargs.items()))

            # Генерация ключа кеша на основе аргументов
            hash_key = hashlib.sha256(
                str(immutible_args).encode() + str(immutible_kwargs).encode()
            ).hexdigest()

            if hash_key in cache:
                print(f"Cache hit for {hash_key}")
                return cache[hash_key]

            # Если ключа нет в кеше, вызываем функцию и сохраняем результат
            result = func(*args, **kwargs)
            cache[hash_key] = result

            # Ограничиваем количество бакетов в кеше
            if len(cache) > max_buckets:
                removed_key, _ = cache.popitem(last=False)  # Удаляем самый старый элемент
                print(f"Cache full. Removed oldest cache entry: {removed_key}")

            return result

        return wrapper

    return decorator
