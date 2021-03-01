""" The sequence should be sorted and indexable """
""" following is an iterative algorithm """


""" time complexity => O(log(n)) """


# here 'data' is the sequence whereas 'target' is the searching element
def iterative_binary_search(data, target):

    low = 0
    high = len(data) - 1

    while low <= high:

        mid = (low + high) // 2

        if data[mid] == target:   			# returns the index if found a match, ie, successful binary search
            return mid

        elif data[mid] < target:  			# only consider right of mid
            low = mid + 1

        else:                     			# only consider left of mid
            high = mid - 1

    return False                  			# unsuccessful binary search
