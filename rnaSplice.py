
from genDict import genDataDict
from dna2rna import dna2rna
from rna2protein import rna2protein

def main():
	dataset = genDataDict()
	sequences = list(dataset.values())
	main = max(sequences)

	sequences.remove(main)
	print('\n\n', dataset,'\n\n', sequences, '\n\n', main, '\n\n')

	for seq in sequences:
		if seq in main:
			main = main.replace(seq, '')
	
	mainR = dna2rna(main)
	protein = rna2protein(mainR)
	print(protein)
	if '0' in protein:
		end = protein.index('0')
		protein = protein[:end]
		print(protein,'\n')

if __name__ == '__main__':
	main()
