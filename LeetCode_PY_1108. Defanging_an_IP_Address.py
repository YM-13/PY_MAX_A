class Solution:
	def defangIPaddr(self, address: str) -> str:
		new_str = address.replace(".", "[.]")
		return new_str




g = Solution()

print(g.defangIPaddr("1.1.1.1"))
print(g.defangIPaddr("255.100.50.0"))