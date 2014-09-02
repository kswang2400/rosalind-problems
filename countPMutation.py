
string1 = input("What is the first string? ")
string2 = input("What is the second string? ")

table = {}

for index, nuc in enumerate(string1):
	# print(index, nuc)
	table[index] = [nuc]

for index, nuc in enumerate(string2):
	table[index] = table[index] + [nuc]

def count(table):
	count = 0
	for key in table:
		set = table[key]
		if set[0] != set[1]:
			count += 1
	return count

print(count(table))
