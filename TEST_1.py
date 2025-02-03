from functools import wraps
import time
import requests

def benchmark(items):

	def decorator(func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			total = 0
			for _ in range(items):
				start = time.time()
				result = func(*args, **kwargs)
				end = time.time()
				total += (end - start)

			print(f"[*] Среднее время выполнения функции {total / items}")
			return result

		return wrapper
	return decorator


@benchmark(items=10)
def fetch_webpage(url):
	webpage = requests.get(url)
	return webpage.text