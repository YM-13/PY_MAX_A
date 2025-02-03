from functools import wraps
import hashlib

def hash_decorator(func):
	cache = {}

	@wraps(func)
	def wrapper(*args, **kwargs):
		immutible_args = tuple([tuple(arg) if isinstance(arg, list) else arg for arg in args])
		immutible_kwargs = tuple(sorted((k, v) for k, v in kwargs.items()))

		hash_key = hashlib.sha256(str(immutible_args).encode() + str(immutible_kwargs).encode()).hexdigest()

		if hash_key in cache:
			print(f"Cache hit for {hash_key}")
			return cache[hash_key]


		result = func(*args, **kwargs)
		cache[hash_key] = result
		return result

	return wrapper()