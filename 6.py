def add(a, b):
	sum = str(int(a)+int(b))
	len1 = len(a)
	b = '+' + b
	len2 = len(b)
	m = max(len1, len2)
	if len1 > len2:
		b = ' '*(len1-len2) + b
	else:
		a = ' '*(len2-len1) + a
	sum = ' '*(m-len(sum)) + sum
	s = "%s\n%s\n%s\n%s\n" % (a,b,'-'*m,sum)
	return s

def subtract(a, b):
	res = str(int(a)-int(b))
	len1 = len(a)
	b = '-' + b
	len2 = len(b)
	m1 = max(len1, len2)
	if len1 > len2:
		b = ' '*(len1-len2) + b
	else:
		a = ' '*(len2-len1) + a
	m = max(len(res), len2)
	dashes = ' '*(m1-m) + '-'*m
	res = ' '*(m1-len(res)) + res
	s = "%s\n%s\n%s\n%s\n" % (a,b,dashes,res)
	return s

def multiply(a, b):
	prod = str(int(a)*int(b))
	li = [a,'*' + b]
	m = max(len(a), len(b) + 1)
	i = 0
	if len(b) > 1:
		li.append('-'*max((len(b)+1), len(str(int(b[-1])*int(a)))))
		for char in b[::-1]:
			li.append(str( int(char)*int(a) )+' '*i)
			i += 1
		li.append('-'*len(prod))
	else: li.append('-'*len(prod))
	li.append(prod)
	li.append('')
	return("\n".join([ putSpaces(elem, max(len(prod),len(b)+1)).rstrip() for elem in li]))

def putSpaces(string, m):
	output = ' '*(m-len(string)) + string
	return output

def parse(string):
	symbols = ('+','-','*')
	for symbol in symbols:
		if string.find(symbol) != -1:
			[a, b] = string.split(symbol)
			if symbol == '+':
				c = add(a, b)
			elif symbol == '-':
				c = subtract(a, b)
			else:
				c = multiply(a, b)
	return c

for test in range(int(input())):
	print(parse(input()))
