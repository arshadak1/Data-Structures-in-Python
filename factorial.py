""" n! = n * (n-1) * (n-2) * (n-3) * ... * 3 * 2 * 1 
    n! = n * (n-1)! """
def factorial(n):  # time complexity => O(n)
	if n <= 1:
		return 1
	else:
		return n * factorial(n - 1)  # recursively calling factorial of n-1
