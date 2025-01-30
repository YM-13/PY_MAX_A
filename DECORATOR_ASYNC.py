import asyncio

def logging_deco(name: str):
	def wraps(func):
		if asyncio.iscoroutine(func):
			async def a_wrapper(*args, **kwargs):  # <-- Асинхронность нужна только тут
				# do something
				result = await func(*args, **kwargs)
				# do something
				return result
			return a_wrapper
		else:
			def wrapper(*args, **kwargs):
			# do something
				result = func(*args, **kwargs)
				# do something
				return result
			return wrapper
	return wraps

@logging_deco('my_custom_name')
async def kek(*args, **kwargs):
	pass

@logging_deco('lol Name')
def lol():
	pass


# kek = logging_deco('my_custom_name')(kek) -> async
# lol = logging_deco('lol Name')(lol) -> sync