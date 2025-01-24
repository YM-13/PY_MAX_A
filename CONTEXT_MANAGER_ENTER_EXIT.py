class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file  # Возвращаем объект файла для использования в блоке with

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()  # Закрываем файл
        return False  # Не подавляем исключения

# Использование
with FileManager("example.txt", "w") as file:
    file.write("This is a custom context manager.")
