
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

for each in eachSeq:
	eachSeq[each] = eachSeq[each].replace("\n", "")
	length = len(eachSeq[each])
	print(each)
	print(eachSeq[each])



######### EXAMPLE SET #########

# eachSeq = {
# 	">Rosalind_1": "ATCCAGCT",
# 	">Rosalind_2": "GGGCAACT",
# 	">Rosalind_3": "ATGGATCT",
# 	">Rosalind_4": "AAGCAACC",
# 	">Rosalind_5": "TTGGAACT",
# 	">Rosalind_6": "ATGCCATT",
# 	">Rosalind_7": "ATGGCACT"
# 	}

# length = 8

###############################



countA = [0] * length
countC = [0] * length
countG = [0] * length
countT = [0] * length

for each in eachSeq:
	DNA = eachSeq[each].rstrip()
	for i, n in enumerate(DNA):
		if n == "A":
			countA[i] += 1
		elif n == "C":
			countC[i] += 1
		elif n == "G":
			countG[i] += 1
		elif n == "T":
			countT[i] += 1

matrix = [countA, countC, countG, countT]
# print(matrix)

sequence = ""

for n in range(length):
	compare = [countA[n], countC[n], countG[n], countT[n]]
	high = max(compare)
	for i in range(4):
		if high == compare[i]:
			if i == 0:
				sequence = sequence + "A"
			elif i == 1:
				sequence = sequence + "C"
			elif i == 2:
				sequence = sequence + "G"
			elif i == 3:
				sequence = sequence + "T"

print(sequence)

a = "A:"
for n in countA:
	a += " " + str(n)

c = "C:"
for n in countC:
	c += " " + str(n)

g = "G:"
for n in countC:
	g += " " + str(n)

t = "T:"
for n in countT:
	t += " " + str(n)

print(a)
print(c)
print(g)
print(t)

