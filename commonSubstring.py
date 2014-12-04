
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

def findCommon(data):
	listSeq = []
	common = []
	for string in data.values():
		listSeq.append(string)

	first = listSubstrings(listSeq[0])
	print(first)

	# for sub in first:
	# 	count = 0
	# 	for seq in listSeq:
	# 		if sub in seq:
	# 			count += 1
	# 			if count == len(listSeq):
	# 				common.append(sub)

	print(common)
	return common

def listSubstrings(string, listSeq):
	subStrings = []
	common = []
	l = len(string)
	for n in range(l):					# length of substrings
		for m in range(l-n):			# start position
			sub = string[m:m+n]
			count = 0
			for seq in listSeq:
				if sub in seq:
					count += 1
					if count == len(listSeq):
						print(sub)
						common.append(sub)
	print(common)
	return common
	# print(subStrings)
	# return subStrings

def main():
	dataDict = genDataDict()
	a = dataDict['>Rosalind_1895']

	listSeq = []
	for string in dataDict.values():
		listSeq.append(string)

	listSubstrings(a, listSeq)
	# findCommon(dataDict)

if __name__ == '__main__':
	main()