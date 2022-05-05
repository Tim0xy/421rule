n = 5
step = 0
y = 0
"""
def count(n):
	if n % 2 == 0:
		new_n = n / 2
	else:
		new_n = (3 * n) + 1
	n = new_n
	if n == 1:
		y = 1
		print(step)
		"""
print("Step || Count")
while True:
	if n % 2 == 0:
		new_n = n / 2
		step += 1
	else:
		new_n = (3 * n) + 1
		step += 1
	n = new_n
	print(step, n)

	if n == 1:
		break
