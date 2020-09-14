def draw_road():
	lanes()
	crossing()
	lanes()

def lanes():
	road = "|"
	for i in range(17):
		print(road+road, end="")
		for j in range(27):
			print(end=" ")
		print(road, end="")
		for j in range(27):
			print(end=" ")
		print(road+road)

def crossing():
	walkside = "-"
	for i in range(3):
		for j in range(59):
			print(walkside, end="")
		print()