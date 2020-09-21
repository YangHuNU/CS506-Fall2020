import math

def euclidean_dist(x, y):
	length = 0
	squared_sum = 0

	if (len(x)>len(y)):	# for length isn't equal
		length = len(y)
	else:
		length = len(x)

	if length==0:	# return when either one list is empty
		return 0
	for i in range(length):
		squared_sum += (x[i]-y[i])**2
	res = math.sqrt(squared_sum)
	return res

def manhattan_dist(x, y):
	length = 0
	abs_sum = 0
	if (len(x)>len(y)): # for length isn't equal
		length = len(y)
	else:
		length = len(x)
	if length==0:	#return when either one list is empty
		return 0
	for i in range(length):
		abs_sum += abs(x[i]-y[i])
	return abs_sum

def jaccard_dist(x, y):
	if len(x)==0 and len(y)==0:
		return 1
	a = set(x)
	b = set(y)
	intersect = len(a.intersection(b))
	union = len(a.union(b))
	return 1-intersect / union	# dissimilarity

def cosine_sim(x, y):
	if len(x)==0 and len(y)==0:
		return 0
	mulpt = 0
	squared_sum = 0
	if (len(x)>len(y)): # for length isn't equal
		length = len(y)
	else:
		length = len(x)
	if length==0:	#return when either one list is empty
		return 0

	for i in range(length):
		squared_sum += (x[i]-y[i])**2
		mulpt += x[i]*y[i]

	if squared_sum==0:	# denomeanator cannot be 0
		return 1
	return mulpt/ math.sqrt(squared_sum)


# Feel free to add more
