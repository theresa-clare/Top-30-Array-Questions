""" Python answers to the Top 30 Array Interview Questions and Answers for Programmers
	from http://javarevisited.blogspot.com/2015/06/top-20-array-interview-questions-and-answers.html

	Notes: 
	- Multiple versions of a problem does not mean the subsequent version is 'better' than the
	previous, just another way of solving the problem 
	- I made the wording of the prompts more clear; prompts aren't exactly word for word from the article"""


###############################################################################

""" 1. Find a missing number in integer array of 1 to 100 """

def missing_one_int(num_list):
	""" Works only if one integer is missing; returns single integer """
	expected_sum = 0
	actual_sum = 0

	for i in range(1,101):
		expected_sum += i
	for num in num_list:
		actual_sum += num

	return expected_sum - actual_sum

def missing_one_int_v2(num_list):
	""" Works only if one integer is missing; returns single integer """
	return sum(range(1,101)) - sum(num_list)

def missing_multiple_ints(num_list):
	""" Works if multiple integers are missing; returns a list of multiple integers """
	return list(set(range(1,101)) - set(num_list))


###############################################################################

""" 2. Find a duplicate number in an integer array

	Input: [0, 3, 1, 2, 3]

	Output: 3 

"""

# returns first duplicate encountered
def duplicate_num(num_list):
	sorted_num_list = sorted(num_list)

	for i in range(len(num_list) - 1):
		if sorted_num_list[i] == sorted_num_list[i + 1]:
			return sorted_num_list[i]
	return None


###############################################################################

""" 3. Check if an array contains a certain number """

def in_list(num_array, num):
	for element in num_array:
		if element == num:
			return True
	return False

def in_list_v2(num_list, num):
	num_set = set(num_list)

	if num in num_set:
		return True
	return False


###############################################################################

""" 4. Find largest and smallest number in an unsorted array """

def find_max_and_min(num_list):
	max_num = num_list[0]
	min_num = num_list[0]

	for num in num_list:
		if num > max_num:
			max_num = num
		elif num < min_num:
			min_num = num

	return max_num, min_num

def find_max_and_min_v2(num_list):
	sorted_num_list = sorted(num_list)
	max_num = sorted_num_list[-1]
	min_num = sorted_num_list[0]

	return max_num, min_num


###############################################################################

""" 5. Find all pairs in an integer array whose sum is equal to a given number """

def pairs_equal_to_sum(num_list, target_sum):
	pairs = set()

	for i, num1 in enumerate(num_list):
		for j, num2 in enumerate(num_list):
			if i != j and num1 + num2 == target_sum and (num2, num1) not in pairs:
				pairs.add((num1, num2))

	return list(pairs)

# Spin-off of current question -- find all pairs whose sum is equal to ZERO

# Input: [1,2,3,-2,-1,0,8,0,2,2,0]
# Output: [[2, -2], [1, -1], [0, 0]]
def pairs_sum_zero(num_list):
	pairs = []
	num_dict = {}
	for num in num_list:
		num_dict[num] = num_dict.get(num,0) + 1
		if num != 0 and num_dict.get(-num,0) > 0:
			pairs.append([-num, num])
			num_dict[-num] -= 1
			num_dict[num] -= 1
	pairs.append([0,0] * (num_dict.get(0,0)/2))
	return pairs


###############################################################################

""" 6. Find repeated numbers in an array if it contains multiple duplicates """

def duplicate_num_v2(num_list):
	""" Returns a list of multiple, unique duplicates """
	duplicates = []
	sorted_num_list = sorted(num_list)

	for i in range(len(num_list) - 1):
		if sorted_num_list[i] == sorted_num_list[i + 1]:
			duplicates.append(sorted_num_list[i])

	return list(set(duplicates))

def duplicate_nums(num_list):
	""" Returns a list of multiple, unique duplicates """
	duplicates = []
	num_dict = {}

	for num in num_list:
		num_dict[num] = num_dict.get(num, 0) + 1

	for number, count in num_dict.iteritems():
		if count > 1:
			duplicates.append(key)

	return duplicates


###############################################################################

""" 7. Remove duplicates from an array """

def remove_duplicates(num_list):
	return [set(num_list)]


###############################################################################

""" 8. Implement QuickSort in place """

def python_quicksort(num_list):
	pass


###############################################################################

""" 9. Find the intersection of two sorted arrays. Can assume numbers are unique """

def intersection(list1, list2):
	intersection = []
	pointer1 = 0
	pointer2 = 0

	while pointer1 < len(list1) and pointer2 < len(list2):
		if list1[pointer1] == list2[pointer2]:
			intersection.append(list1[pointer1])
			pointer1 += 1
			pointer2 += 1
		elif list1[pointer1] < list2[pointer2]:
			pointer1 += 1
		else:
			pointer2 += 1

	return intersection

# if two arrays are unsorted, see following two functions:
def unsorted_intersection(list1, list2):
	set2 = set(list2)
	intersection_set = set()

	for element in list1:
		if element in set2:
			intersection_set.add(element)

	return list(intersection_set)


def unsorted_intersection_v2(list1, list2):
	combined = [set(list1), set(list2)]
	return list(set.intersection(*combined))


###############################################################################

""" 10. There is an array with every element repeated twice except one. Find that element 

	Input: [1, 1, 2, 2, 3, 4, 4, 5, 5]

	Output: 3

"""

def element_not_repeated(num_list):
	num_dict = {}

	for num in num_list:
		num_dict[num] = num_dict.get(num, 0) + 1

	for number, count in num_dict.iteritems():
		if count == 1:
			return number


###############################################################################

""" 11. Find the kth smallest element in an unsorted array 

	Input: [1, 2, 3, 9, 4]
		    2

	Output: 2

"""

def kth_smallest(num_list, k):
	sorted_num_list = sorted(num_list)
	return sorted_num_list[k - 1]


###############################################################################

""" 12. Find the kth largest element in an unsorted array 

	Input: [10, 20, 30, 50, 40]
			3

	Output: 30

"""

def kth_largest(num_list, k):
	sorted_num_list = sorted(num_list)
	return sorted_num_list[-k]


###############################################################################

""" 13. Find common elements in 3 sorted arrays 

	Input: [1, 5, 10, 20, 40, 80]
		   [6, 7, 20, 80, 100]
		   [3, 4, 15, 20, 30, 70, 80, 120]

	Output: [20, 80]

"""
# Note to self: Find solution to take into account the ***sorted*** aspect

def common_elements(list1, list2, list3):
	list_of_sets = [set(list1), set(list2), set(list3)]
	return list(set.intersection(*list_of_sets))

def common_elements_v2(list1, list2, list3):
	set2 = set(list2)
	set3 = set(list3)
	common_elements = set()

	for element in list1:
		if element in set2 and element in set3 and element not in common_elements:
			common_elements.add(element)

	return list(common_elements)


###############################################################################

""" 14. Find the first repeating element in an array of integers """

def first_repeated(num_list):
	num_set	= set()

	for num in num_list:
		if num in num_set:
			return num
		num_set.add(num)

	return None


###############################################################################

""" 15. Find first non-repeating element in an array of integers """

def first_nonrepeated(num_list):
	num_dict = {}
	for num in num_list:
		num_dict[num] = num_dict.get(num,0) + 1
	for number in num_list:
		if num_dict[number] == 1:
			return number
	return None


###############################################################################

""" 16. Find the top two maximum numbers from an integer array """

def top_two_maximum(num_list):
	if len(num_list) < 2:
		return "There are not enough numbers"
	elif len(num_list) == 2:
		return num_list

	sorted_num_list = sorted(num_list)
	return sorted_num_list[-1], sorted_num_list[-2]

def top_two_maximum_v2(num_list):
	if len(num_list) < 2:
		return "There are not enough numbers"
	elif len(num_list) == 2:
		return num_list

	maximum = num_list[0]
	second_max = num_list[1]

	for num in num_list:
		if num > maximum:
			second_max = maximum
			maximum = num
		elif second_max < num < maximum:
			second_max = num

	return maximum, second_max


###############################################################################

""" 17. Find the smallest positive integer value that cannot be represented as 
	the sum of any subset of a given sorted array 

	Input: [1, 3, 6, 10, 11, 15]

	Output: 2

"""
# Note to self: Find solution to take into account the ***sorted*** aspect

def smallest_nonsubset_sum(num_list):
	positive_totals = set()
	smallest_pos_int = 1

	for i in range(len(num_list)):
		total = 0
		for j in range(i, len(num_list)):
			total += num_list[j]
			if total > 0:
				positive_totals.add(total)
	
	while True:
		if smallest_pos_int not in positive_totals:
			return smallest_pos_int
		smallest_pos_int += 1


###############################################################################

""" 18. Rearrange array in alternating positive and negative numbers. 

	Given an array of positive and negative numbers, arrange them in an alternate
	fashion such that every positive number is followed by negative and vice-versa
	maintaining the order of appearance.

	Number of positive and negative numbers need not be equal. If there are more
	positive numbers, they appear at the end of the array and vice-versa. 

	Input: [1, 2, 3, -4, -1, 4]
	Output: [-4, 1, -1, 2, 3, 4]

	Input: [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
	Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]

"""

def alternating_pos_neg(num_list):
	alternating = []

	# Can initialize positives and negatives to empty list, then loop through list 
	# only once instead of twice by list comprehensions
	positives = [x for x in num_list if x >= 0]
	negatives = [y for y in num_list if y < 0]

	zipped_pairs = zip(positives, negatives)
	for pos, neg in zipped_pairs:
		alternating.extend([pos,neg])

	if len(positives) > len(negatives):
		alternating.extend(positives[len(zipped_pairs):])
	else:
		alternating.extend(negatives[len(zipped_pairs):])

	return alternating


###############################################################################

""" 19. Find if there is a subarray with a sum equal to zero 

	Input: [4, 2, -3, 1, 6]
	Output: True
	There is a sub-array with zero sum from index 1 to 3 ([2, -3, 1])

"""

def subarray_sum_zero(num_list):
	for i in range(len(num_list)):
		total = 0
		for j in range(i, len(num_list)):
			total += num_list[j]
			if total == 0:
				return True
	return False


###############################################################################

""" 20. Remove duplicates from an array in place. Return length of array without duplicates

	Input: [1, 1, 2]
	Output: 2
			Array is now [1, 2]

"""

def remove_duplicates(num_list):
	nums_seen = set()

	for i,  num in enumerate(num_list):
		if num in nums_seen:
			num_list.pop(i)
		nums_seen.add(num)

	return len(num_list)


###############################################################################

""" 21. Remove a given element from an array in place, preserving the order """

def remove_value(num_list, value):
	for i, num in enumerate(num_list):
		if num == value:
			num_list.pop(i)


###############################################################################

""" 22. Merge two sorted arrays 

	Input: [1, 2, 3, 4, 5, 6]
		   [4, 5, 6, 7, 8]

	Output: [1, 2, 3, 4, 5, 6, 7, 8]

"""

# Does not include duplicates
def merge_lists(list1, list2):
	merged = []
	reached_both_ends = False
	i = 0
	j = 0

	# add the items until one list reaches the end
	while i < len(list1) and j < len(list2):
		if list1[i] > list2[j]:
			merged.append(list2[j])
			j += 1
		elif list1[i] < list2[j]:
			merged.append(list1[i])
			i += 1
		else:
			merged.append(list1[i]) # to include duplicates, add this twice
			i += 1
			j += 1

	# add the remainder of the unfinished list
	while not reached_both_ends:
		if i == len(list1):
			merged.append(list2[j])
			j += 1
		elif j == len(list2):
			merged.append(list1[i])	

		if i == len(list1) and j == len(list2):
			reached_both_ends = True

	return merged

def merge_lists_v2(list1, list2):
	combined = list1 + list2

	return sorted(combined)

###############################################################################

""" 23. Find the subarray with the maximum sum in an array of positive and 
	negative numbers 

	Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

	Output: [4, -1, 2, 1]
			(has the largest sum = 6)

"""

def max_sum_subarray(num_list):
	subarray = []
	max_sum = num_list[0]

	for i in range(len(num_list)):
		total = 0
		for j in range(i, len(num_list)):
			total += num_list[j]
			if total > max_sum:
				subarray = num_list[i:j + 1] # note: add 1 b/c list slicing end is exclusive
				max_sum = total

	return subarray


###############################################################################

""" 24. Find the subarray with the largest product in an array of both positive 
	and negative numbers """

def max_product_subarray(num_list):
	subarray = []
	max_sum = num_list[0]

	for i in range(len(num_list)):
		total = 0
		for j in range(i, len(num_list)):
			total *= num_list[j]
			if total > max_sum:
				subarray = num_list[i:j + 1] # note: add 1 b/c list slicing end is exclusive
				max_sum = total

	return subarray


###############################################################################

""" 25. Given an unsorted array of integers, find the length of the longest
	consecutive elements sequence. Should be O(n) complexity 

	Input: [100, 4, 200, 1, 3, 2]

	Output: 4
		   (longest consecutive is [1, 2, 3, 4])

"""
# Note to self: Find solution in O(n) complexity

def len_longest_consecutive(num_list):
	num_set = set(num_list)
	longest_length = 1

	for num in num_list:
		current_length = 0
		finished = False

		while not finished:
			if num in num_set:
				current_length += 1
				num += 1
			else:
				finished = True
				if current_length > longest_length:
					longest_length = current_length

	return longest_length


###############################################################################

""" 26. Find minimum value in a rotated sorted array. Assume no duplicates exist.

	Input: [4, 5, 6, 7, 0, 1, 2]

	Output: 0

"""

def min_in_rotated(num_list):
	previous = num_list[0]

	for num in num_list:
		if previous > num:
			return num
		previous = num


###############################################################################

""" 27. Given an array of size n and a number k, find all elements that appear 
	more than n/k times 

	Input: [3, 1, 2, 2, 1, 2, 3, 3]
		   4
		   (size n = 8, so need to find elements that appear more than 2 (or 8/4))

	Output: [2, 3]

"""

def n_div_k_occurrences(num_list, k):
	n = len(num_list)
	num_dict = {}
	occurrences = []

	for num in num_list:
		num_dict[num] = num_dict.get(num, 0) + 1
	for number, count in num_dict.iteritems():
		if count > n/k:
			occurrences.append(number)

	return occurrences


###############################################################################

""" 28. Reverse an array in place """

def reverse(num_list):
	length = len(num_list)

	for i in range(len(num_list)/2):
		temp = num_list[i]
		num_list[i] = num_list[length - 1 - i]
		num_list[length - 1 - i] = temp


###############################################################################

""" 29. What are the differences between an array and a linked list? """

""" list 								linked list
	----								-----------

- contiguous memory allocation			- scattered memory allocation
										--> better at utilizing limited memory space
										in comparison to list of same length 

- O(1) lookup if know index				- O(n) lookup for node at certain index
										--> need to traverse linked list to get there 

- allows random access					- does not allow random access; must traverse

- fixed length data structure b/c 		- dynamic data structure
  initialize length during creation
  (in java)

- ideal for fast caches which require	- linear performance for retrieval
  constant lookup time with hashtables

- one or multi-dimensional				- singly, doubly, or circular
"""


###############################################################################

""" 30. Check if array contains a duplicate using T/F-ness of adding a number 
	already present in a set """

""" Python does not evaluate to false if add a preexisting number to set """

