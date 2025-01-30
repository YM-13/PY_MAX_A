from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file  # Передаём объект файла в блок with
    finally:
        file.close()  # Закрываем файл

# Использование
with file_manager("example.txt", "w") as file:
    file.write("This is a context manager using a decorator.")


# ИЗ КУРСАЖ
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()