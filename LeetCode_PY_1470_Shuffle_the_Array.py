from typing import List


class Solution:
	def shuffle(self, nums: List[int], n: int) -> List[int]:
		n_l = [None] * 2 * n
		a = 0
		for i in range(n):
			b = a + 1
			n_l[a], n_l[b] = nums[i], nums[i + n]
			a += 2

		return n_l


g = Solution()
print(g.shuffle([1,1,2,2], 2))

