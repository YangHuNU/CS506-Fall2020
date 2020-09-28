from collections import defaultdict
from math import inf, sqrt
import random
import csv



def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)

    Returns a new point which is the center of all the points.
    """
    total = [0 for x in range(len(points[0]))]
    for point in points:
        for j in range(len(total)):
            total[j] += point[j]
    return [x/len(points) for x in total]

def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    grouped = defaultdict(list)
    res_centers = []
    for point, assignment in zip(dataset, assignments):
        grouped[assignment].append(point)
    for _,c in grouped.items():
        res_centers.append(point_avg(c))
    return res_centers

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    length = 0
    squared_sum = 0

    if (len(a)>len(b)): # for length isn't equal
        length = len(b)
    else:
        length = len(a)

    if length==0:   # return when either one list is empty
        return 0
    for i in range(length):
        squared_sum += (a[i]-b[i])**2
    res = sqrt(squared_sum)
    return res

def distance_squared(a, b):
    return distance(a,b)**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(dataset, k)

def cost_function(clustering):
    center_dist = 0
    for _, cluster in clustering.items():
        center = point_avg(cluster) # find center point
        for point in cluster:
            center_dist += distance_squared(point, center)
    return center_dist


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centers = []
    init_c = generate_k(dataset, k)
    distances = []
    for point in dataset:
        distances.append(distance_squared(point, init_c[0]))
    mylist = [i for i in range(len(dataset))]
    probabilities = [x/sum(distances) for x in distances]
    for i in range(k):
        index = random.choices(mylist, weights=probabilities, k=k)
        centers.append(dataset[index[0]])
        probabilities[index[0]] = 0
    return centers


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
