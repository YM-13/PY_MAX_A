import time
from functools import wraps

def retry(max_retrys=3, delay=1, exeptions=(Exception, )):

	def decorator(func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			for attempt in range(max_retrys):
				try:
					return func(*args, **kwargs)
				except exeptions as e:
					print(f"Attempt {attempt + 1} failed {e}")
					if attempt + 1 == max_retrys:
						print("You have reached max num of attempts.")
						raise
					time.sleep(delay)

		return wrapper
	return decorator