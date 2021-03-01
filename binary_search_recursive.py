""" The sequence should be sorted and indexable """
""" following is a recursive algorithm """

""" time complexity => O(log(n)) """


def recursive_binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:						# interval is empty, unsuccessful binary search
        return False

    else:
        mid = (low + high) // 2

        if data[mid] == target:			# found a match, returns the index
            return mid

        elif data[mid] < target:        # recur on the portion right of the middle

            return recursive_binary_search(data, target, mid + 1, high)

        else:							# recur on the portion left of the middle

            return recursive_binary_search(data, target, low, mid - 1)
