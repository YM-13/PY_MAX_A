# Здесь объявляется класс Factory
class Factory:

	def build_sequence(self):
		return []

	def build_number(self, string):
		return float(string)


class Loader:
	def parse_format(self, string, factory):
		g = factory
		print(g.__dict__)
		print(factory.__dict__)
		print(Factory.__dict__)
		seq = factory.build_sequence()
		for sub in string.split(","):
			item = factory.build_number(sub)
			seq.append(item)

		return seq


# эти строчки не менять!
ld = Loader()
s = input()

res = ld.parse_format(s, Factory())
