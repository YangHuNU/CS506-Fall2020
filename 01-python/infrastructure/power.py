def draw_power_plant():
	vda = "~"


	for i in range(7, 40, 2):
		for j in range((40-i-1)//2):
			print(end=" ")
		for k in range(i):
			print(vda, end="")
		print()