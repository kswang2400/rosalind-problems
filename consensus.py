
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

count = {
	"A": A, 
	"C": C, 
	"G": G, 
	"T": T
}

# iterate through each sequence for the same position to find most consensus string

consensus = ""

for position in range(length):
	tracker = {}
	for nuc in count:
		tracker[count[nuc][position]] = nuc
		# print(tracker)
	high = max(tracker.keys())
	# print(high)
	# print(tracker[high])
	consensus += tracker[high]


print(consensus)
print("A: ", " ".join(str(x) for x in A))
print("C: ", " ".join(str(x) for x in C))
print("G: ", " ".join(str(x) for x in G))
print("T: ", " ".join(str(x) for x in T))

