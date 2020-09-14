def draw_tree():
	#print top
	star = "*"
	for i in range(1, 20, 2):
		for j in range((20-i-1)//2):
			print(end=" ")
		for k in range(i):
			print(star, end="")
		print()

	#print bottom
	ver = "|"
	for i in range(4):
		for j in range(5):
			print(end=" ")
		for k in range(9):
			print(ver, end="")
		print(end="\n")