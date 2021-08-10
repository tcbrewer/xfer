# HW0: Sieve (sol)

# use the Sieve of Eratosthenes or something like it to find the first n prime numbers 

# Name:   nPrimes
# Inputs: some integer _n_, the number of primes to output
# Output: an integer list of the n least prime numbers, ordered least to greatest
# nPrimes(5) will return [2,3,5,7,11]
# nPrimes(0) will return []
def nPrimes(n):
	# start with an empty sieve and the first prime
	toRet = []
	i = 2
	while(len(toRet) < n):
		# see if _i_ passes through the sieve
		prime = True
		for j in toRet:
			if i % j == 0: # this would mean j divides i, so i not prime
				prime = False
		# if _i_ passes through, add to sieve
		if prime:
			toRet.append(i) # append to preserve least to greatest
		# increment i
		i += 1
	return toRet
	
print(nPrimes(5)) # should print [2,3,5,7,11]
