
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
