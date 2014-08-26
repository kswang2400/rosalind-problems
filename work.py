
def GCcontent(sequence):
	gc = 0
	total = 0
	for nuc in sequence:
		if nuc == "G" or nuc == "C":
			gc += 1
			total += 1
		else:
			total += 1
	percent = gc / float(total)
	print(percent, gc, total)
	return percent

eachSeq = {}
eachSeqPer = {}

with open('rosalind_gc.txt') as dataset:
	for line in dataset:
		# print(line)
		if line[0] == ">":
			eachSeq[line] = 0
			current = line
		else:
			if eachSeq[current] == 0:
				eachSeq[current] = line
			else:
				eachSeq[current] += line

for name in eachSeq:
	eachSeq[name] = eachSeq[name].replace('\n','')

print(eachSeq)

for name in eachSeq:
	sequence = eachSeq[name]
	percent = GCcontent(sequence)
	eachSeqPer[name] = percent

maxGC = max(eachSeqPer, key = eachSeqPer.get)

print(maxGC)
print(eachSeqPer[maxGC])

####### SOLUTION FROM ROSALIND (GAIK TAMAZIAN) ####### 

# f = open('rosalind_gc.txt', 'r')

# max_gc_name, max_gc_content = '', 0

# buf = f.readline().rstrip()
# while buf:
#     seq_name, seq = buf[1:], ''
#     buf = f.readline().rstrip()
#     while not buf.startswith('>') and buf:
#         seq = seq + buf
#         buf = f.readline().rstrip()
#     seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
#     if seq_gc_content > max_gc_content:
#         max_gc_name, max_gc_content = seq_name, seq_gc_content

# print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
# f.close()



