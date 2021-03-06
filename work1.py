
# organize the text file into a dictionary 

eachSeq = {}

with open('rosalind_cons.txt') as dataset:
	for line in dataset:
		# print(line)
		if line[0] == ">":
			line = line.replace("\n", "")
			eachSeq[line] = 0
			current = line
		else:
			if eachSeq[current] == 0:
				eachSeq[current] = line
			else:
				eachSeq[current] += line

for DNA in eachSeq:
	eachSeq[DNA] = eachSeq[DNA].replace("\n", "")
	length = len(eachSeq[DNA])
	# print("Name: ", DNA)
	# print("Sequence: ", eachSeq[DNA])
	
A = [0] * length
C = [0] * length
G = [0] * length
T = [0] * length

# iterate through each sequence for the same position and append count to arrays
# continue through range(len(DNA))

for position in range(length):
	for DNA in eachSeq:
		x = eachSeq[DNA][position]
		if x == "A":
			A[position] += 1
		elif x == "C":
			C[position] += 1
		elif x == "G":
			G[position] += 1
		elif x == "T":
			T[position] += 1
