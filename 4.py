import re

def infixToPostfix(str):
	stack = []
	output = []
	open_brackets = 0
	for char in str:
		if re.search('[+*-/^]',char):
			stack.append(char)
		elif char == '(':
			stack.append(char)
		elif char == ')':
			while stack[-1] != '(':
				output.append(stack.pop())
			stack.pop()
		else: output.append(char)
	return "".join((output))

for tests in range(int(input())):
	print(infixToPostfix(input()))
