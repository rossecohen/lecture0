###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    start = time.time()
    all_trips, used_cows, remaining_cows = [], [], []
    all_cows = [(k, cows[k]) for k in sorted(cows, key=cows.get, reverse=True)]
    for i in range(len(all_cows)):
        c = all_cows[i][0]
        remaining_cows.append(c)
    for i in remaining_cows:
        this_trip_weight_remaining, this_trip_cows = limit, []
        for i in range(len(all_cows)):
            a, b = all_cows[i][0], all_cows[i][1]
            if a not in used_cows and b <= this_trip_weight_remaining:
                this_trip_weight_remaining -= b
                this_trip_cows.append(a)
                used_cows.append(a)
        all_trips.append(this_trip_cows)
    end = time.time()
    print(end - start)
    return all_trips



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    start = time.time()
    best_trip_count = len(cows)
    best_answer = []
    for partition in get_partitions(cows):
        any_bad_trips = 0
        for trip in partition:
            weight = 0    
            for cow in trip:
                weight += cows[cow]
            if weight > limit:
                any_bad_trips = 1
        if any_bad_trips == 0 and len(partition) <= best_trip_count:
            best_trip_count = len(partition)
            best_answer = partition
    end = time.time()
    print(end - start)
    return best_answer




# make sure each trip in the partition has weight < limit
# if so, count trips in the partition
# capture # of trips in variable and the partition if it's the shortest so far
# at end, return the list of trips that was the shortest
#(should I only evaluate it if the length of partition is shorter than solution so far?)


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


