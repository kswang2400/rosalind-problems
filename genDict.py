
def genDataDict():
	data = input("Name of file: ")
	dataDict = {}

	isName = False
	with open('{}.txt'.format(data), 'r') as dataset:
		for line in dataset:
			if line[0] == '>':
				isName = True
				current = line.strip()
			else:
				isName = False

			if isName:
				dataDict[current] = ''
			else:
				dataDict[current] += line.strip()

	return dataDict