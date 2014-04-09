def nextPalindrome(string):
	if len(string) == 1:
		if string == '9':
			return '11'
		else:
			return str(int(string)+1)
	n = len(string)/2
	if n == int(n):
		n = int(n)
		if string[n:] >= string [n-1::-1]:
			if string[n-1] == '9':
				counter = 0
				for j in range(1,n):
					if string[n-1-j] != '9':
						out = string[:n-1-j]+str(int(string[n-1-j])+1) + '0'*j
						output = out + out[::-1]
						counter += 1
						break
				if counter == 0:
					out = '1'+'0'*(n-1)
					output = out + '0' + out[::-1]
			else:
				output = string[:n-1]+str(int(string[n-1])+1)
				output = output + output[::-1]
		else:
			output = string[:n]
			output = output + output[::-1]
		return output
	else:
		n = int(n)
		if string[n+1:] >= string [n-1::-1]:
			if string[n] == '9':
				counter = 0
				for j in range(1,n+1):
					if string[n-j] != '9':
						out = string[:n-j] + str(int(string[n-j])+1) + '0'*(j-1)
						output = out +'0' + out[::-1]
						counter += 1
						break
				if counter == 0:
					out = '1'+'0'*n
					output = out + out[::-1]
			else:
				out = string[:n] + str(int(string[n])+1)
				output = out + out[-2::-1]
		else:
			output = string[:n+1]
			output = output + output[-2::-1]
		return output

for tests in range(int(input())):
	print(nextPalindrome(input()))
