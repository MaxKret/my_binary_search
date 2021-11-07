"""
Portfolio Python Project - Binary Search Implementation by Maxwell Kretschmer

Website: https://maxwellkretschmer.tech
Github: https://www.github.com/MaxKret
"""

import random
import time
from typing import List

# Implementation of Binary Search algorithm (comparison to Linear Search)

# On an ordered list:
# Binary search ~ O(log(n)), linear search ~ O(n)

# l is a list (ascending order), and target is what we're looking for
# Returns index or -1 if not found


def linear_search_list(l: list, target) -> int:
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search_list(l: List, target, low=None, high=None) -> int:
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search_list(l, target, low, midpoint-1)
    else:# target > l[midpoint]
        return binary_search_list(l, target, midpoint+1, high)

		

def generate_sorted_list(length: int) -> list:
	sorted_list = set()
	while len(sorted_list) < length:
		sorted_list.add(random.randint(-3*length, 3*length))
	return sorted(list(sorted_list))


def linear_list_unit_test(data_structure: list) -> float:
	start = time.time()
	for target in data_structure:
		linear_search_list(data_structure, target)
	end = time.time()
	return end-start


def binary_list_unit_test(data_structure: list) -> float:
	start = time.time()
	for target in data_structure:
		linear_search_list(data_structure, target)
	end = time.time()
	return end-start



if __name__=='__main__':

    sorted_list = generate_sorted_list(10000) #length

    print("Linear search time:", linear_list_unit_test(sorted_list), "seconds")

    print("Binary search time:", binary_list_unit_test(sorted_list), "seconds")