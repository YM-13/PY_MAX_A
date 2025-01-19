import functools


def fabrica_of_decorators(param1, param2):

	def decorator(func):
		@functools.wraps(func)   # == from functools import wraps
		def wrapper(*args, **kwargs):
			print(f"Параметры фабрики декораторов на печать {param1}, {param2}")
			resalt = func(*args, **kwargs)
			return resalt

		return wrapper
	return decorator



def pupkin(n: int):
	pass


pupkin = fabrica_of_decorators("lol", "LLOOLL")(pupkin)
pupkin(8)


# ********************************************

def logging_deco(name: str):
	...

@logging_deco('my_custom_name')
async def func(*args, **kwargs):
	pass

'''==== Тоже самое что ===='''

func = logging_deco('my_custom_name')(func)