# def factorial(n):
#     # Базовый случай: факториал 0 или 1 равен 1
#     if n == 0 or n == 1:
#         return 1
#     # Рекурсивный случай
#     return n * factorial(n - 1)
#
# # Тестируем
# print(factorial(5))  # Вывод: 120


# def factorial(n):
# 	res = 1
# 	for i in range(1, n + 1):
# 		res *= i
# 	return res
#
#
# print(factorial(3))


# class Contecst_men:
# 	def __init__(self, file, mode):
# 		self.file = file
# 		self.mode = mode
# 		self.work_file = None
#
# 	def __enter__(self):
# 		self.work_file = open(self.file, self.mode)
# 		return self.work_file
#
# 	def __exit__(self, exc_type, exc_value, traceback):
# 		if self.work_file:
# 			self.work_file.close()
#
# 		return False


# MULTIPROCESSING
# from multiprocessing import Process
#
# def warker():
# 	pass
#
# p = Process(target=warker)
# p.start()
#
# import time
# def wait_worker():
# 	time.sleep(5)
#
# # p.terminate()
# p.join()


# import os
# import psutil
#
# def show_process_priority():
# 	process = psutil.Process(os.getpid)
#
# 	print(f"Приоритет процесса: {process.nice()}")
# 	try:
# 		process.nice(10)
# 	except

class Point:
	def __new__(cls, *args, **kwargs):
		print("TOOOOOOO")
		return super().__new__(cls)

