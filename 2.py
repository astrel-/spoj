def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n ** 0.5) # square root of n
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

def primes(n):
	if n==2: return [2]
	elif n<2: return []
	s = list(range(3,n+1,2))
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=int((m*m-3)/2)
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

for tests in range(int(input())):
	(m, n) = map(int, input().split(' '))
#	print(primes(n))
	print(list(filter(lambda x: (x>m-1), primes(n))))
#	for number in range(m,n+1):
#		if is_prime(number):
#			print(number)
#	#print("\n")
