''' Fibonacci series = 1, 1, 2, 3, 5, 8, 13, 21 ... '''

def fibonacci(n):  # Time complexity => O(n)
''' return pair of Fibonacci number F(n) and F(n - 1) '''
	if n <= 1:
		return (n, 0)
	else:
		(a, b) = fibonacci(n - 1)  # here function returns a tuple (a, b) where 'a' is F(n) and 'b' is F(n - 1)
		return (a + b, a)
