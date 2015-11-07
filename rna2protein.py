
def main():
	RNA = input("RNA: ")
	print(rna2protein(RNA))

def rna2protein(RNA):
	f = open('codon.txt', 'r')
	s = f.readlines()

	codon = {}

	for pair in s:
		if tuple([pair[:3]]) in codon:
			codon[pair[:3]].append(pair[4])
		else:
			codon[pair[:3]] = pair[4]
			
	answer = []

	for i in range(0, len(RNA), 3):
		triplet = RNA[i:i+3]
		if triplet in codon:
			answer.append(codon[triplet])

	f.close()

	output = ''.join(answer)
	return output

if __name__ == '__main__':
	main()