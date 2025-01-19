'''try:
    # Код, который может вызвать исключение
except <ТипИсключения>:
    # Код, который выполнится при возникновении указанного исключения
else:
    # Код, который выполнится, если исключение НЕ произошло (опционально)
finally:
    # Код, который выполнится в любом случае (опционально)'''

try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to access this file.")
else:
    print("File read successfully.")
finally:
    print("Execution completed.")
    if 'file' in locals() and not file.closed:
        file.close()

""" The file does not exist.

    Execution completed.
"""
