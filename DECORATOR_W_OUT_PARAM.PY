from functools import wraps

def decorator(func):
	@wraps(func) # wrapper = functools.wraps(func)(wrapper) => functools.wraps(func) здесь  специнструмент питона BИНСПЕКТ_ОР заглянет везде
	def wrapper(*args, **kwargs):  # и вытянет все: докстринг, аргументы, типы ....  ВСЕ wrapper УНИКАЛЬНЫ. КАЖДЫЙ ВЫЗОВ wrapper УНИКАЛЬНЫЙ
		print('Before the function call')
		func(*args, **kwargs)
		print('After the function call')

		return func
	return wrapper



def pranik():
	pass


pranik = decorator(pranik)

pranik()

####################################################


def logging_deco(name: str):
	...

@logging_deco("параметр декоратора")
def function():
	...

"""== = Тоже самое что == ="""

function = logging_deco("параметр декоратора")(function)