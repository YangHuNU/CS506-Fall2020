def read_csv(csv_file_path):
	"""
		Given a path to a csv file, return a matrix (list of lists)
		in row major.
	"""
	data = []
	with open(csv_file_path, 'r') as csv_file:
		lines = csv_file.readlines()
		for line in lines:
			row = line.split(",")
			# convert string to int
			new_row = []
			for i in range(len(row)):
				new_row.append(eval(row[i]))
			data.append(new_row)
	return data