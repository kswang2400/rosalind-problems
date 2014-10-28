
n = int(input("N: "))
n = list(range(1, n+1))

answer = []

def permute(remainder, output = []):

	print('remainder', remainder, 'output', output)

	if len(remainder) == 1:
		print('remainder', remainder[0])
		output.append(remainder[0])
		print('output', output)
		answer.append(output)
		output = []
		print('answer', answer)

	temp = list(remainder)

	for x in remainder:
		print('x', x)
		output.append(x)
		temp.remove(x)
		# print('temp', temp)
		# print('output', output)
		permute(temp, output)
		temp = list(remainder)
		output = []
		print("""
			""")

	return answer

permute(n)
print('answer', answer)

######

# d-205-175-113-78:RosalindProblems KWangAir$ python3 -i geneOrder.py
# N: 3
# remainder [1, 2, 3] output []
# x 1
# remainder [2, 3] output [1]
# x 2
# remainder [3] output [1, 2]
# remainder 3
# output [1, 2, 3]
# answer [[1, 2, 3]]
# x 3
# remainder [] output [3]

			

			
# x 3
# remainder [2] output [3]
# remainder 2
# output [3, 2]
# answer [[1, 2, 3], [3, 2]]
# x 2
# remainder [] output [2]

			

			

			
# x 2
# remainder [1, 3] output [2]
# x 1
# remainder [3] output [2, 1]
# remainder 3
# output [2, 1, 3]
# answer [[1, 2, 3], [3, 2], [2, 1, 3]]
# x 3
# remainder [] output [3]

			

			
# x 3
# remainder [1] output [3]
# remainder 1
# output [3, 1]
# answer [[1, 2, 3], [3, 2], [2, 1, 3], [3, 1]]
# x 1
# remainder [] output [1]

			

			

			
# x 3
# remainder [1, 2] output [3]
# x 1
# remainder [2] output [3, 1]
# remainder 2
# output [3, 1, 2]
# answer [[1, 2, 3], [3, 2], [2, 1, 3], [3, 1], [3, 1, 2]]
# x 2
# remainder [] output [2]

			

			
# x 2
# remainder [1] output [2]
# remainder 1
# output [2, 1]
# answer [[1, 2, 3], [3, 2], [2, 1, 3], [3, 1], [3, 1, 2], [2, 1]]
# x 1
# remainder [] output [1]

			

			

			
# answer [[1, 2, 3], [3, 2], [2, 1, 3], [3, 1], [3, 1, 2], [2, 1]]
# >>> 
