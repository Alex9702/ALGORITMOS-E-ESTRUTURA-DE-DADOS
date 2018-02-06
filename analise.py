import time

def sumOfN(n):
	start = time.time()
	s = 0
	for i in range(1, n + 1):
		s += i
	end = time.time()
	return s, end - start

for _ in range(5):
	print('sum is %d required %.7f seconds'%sumOfN(1000000))	
print('----------------------------------')

def sumOfN3(n):
	start = time.time()
	s = (n*(n+1))/2
	end = time.time()
	return s, end - start

for _ in range(5):
	print('sum is %d required %.7f seconds'%sumOfN3(1000000))	


# sum is 500000500000 required 0.0467997 seconds
# sum is 500000500000 required 0.0467997 seconds
# sum is 500000500000 required 0.0467997 seconds
# sum is 500000500000 required 0.0467997 seconds
# sum is 500000500000 required 0.0467997 seconds
# ----------------------------------
# sum is 500000500000 required 0.0000000 seconds
# sum is 500000500000 required 0.0000000 seconds
# sum is 500000500000 required 0.0000000 seconds
# sum is 500000500000 required 0.0000000 seconds
# sum is 500000500000 required 0.0000000 seconds