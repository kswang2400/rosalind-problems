
n = int(input("N: "))
n = list(range(1, n+1))

answer = []

def permute(remainder, output = []):

	print('remainder', remainder, 'output', output)

	if len(remainder) == 1:
		print('remainder', remainder[0])
		output.append(remainder[0])
		answer.append(output)
		print('answer', answer)

	temp = list(remainder)

	for x in remainder:
		output = []
		print('x', x)
		output.append(x)
		temp.remove(x)
		print('temp', temp)
		print('output', output)
		permute(temp, output)
		temp = list(remainder)
		print("""
			""")
	return answer

permute(n)
print('answer', answer)