# Problem

# An RNA string is a string formed from the alphabet 
# containing 'A', 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, 
# its transcribed RNA string u is formed by replacing all 
# occurrences of 'T' in t with 'U' in u.

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.

def main():
	dataset = input("What is the genomic sequence? ")
	changeRNA(dataset)

def changeRNA(DNAsequence):
	sequence = list(str(DNAsequence.upper()))
	for n, i in enumerate(sequence):
		if i == "T":
			sequence[n] = "U"
	answer = ''.join(sequence)
	print(" ")
	print(answer)
	return None

# WAY BETTER answer

def dna2rna(dna):
	rna = dna.replace('T','U')
	return rna