# Problem

# An RNA string is a string formed from the alphabet 
# containing 'A', 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, 
# its transcribed RNA string u is formed by replacing all 
# occurrences of 'T' in t with 'U' in u.

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.

dataset = input("What is the genomic sequence? ")

def changeRNA(DNAsequence):
	sequence = list(str(DNAsequence.upper()))
	for n, i in enumerate(sequence):
		if i == "T":
			sequence[n] = "U"
	answer = ''.join(sequence)
	print(" ")
	print(answer)
	return None

changeRNA(dataset)




# WAY BETTER answer

answer = input("DNA? ").replace('T','U')
print(answer)
