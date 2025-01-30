from collections import  Counter

class Solution:
	def frequencySort(self, s: str):
		counter = Counter(s)#.items()
		l = [key * counter[key] for key in counter]
		l.sort(key=len, reverse=True)
		return ''.join(l)




g = Solution()
g.frequencySort("asdddaoprop")