
from math import factorial

# 1		12		123		1234		
# 						1243		
# 						1423		
# 				132		1324		
# 						1342		
# 						1432		
# 		21		213		2134		
# 						2143		
# 						2413		
# 				231		2314		
# 						2341		
# 						2431		
# 				312		3124		
# 						3142		
# 						3412		
# 				321		3214		
# 						3241		
# 						3421		
# 						4123		
# 						4132		
# 						4213		
# 						4231		
# 						4312		
# 						4321		

# 	build(1) = [1]
# 	build(2) = [[1, 2], [2, 1]]
# 	build(3) = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

n = int(input("N: "))

def build(n):

	lst = [0] * n
	skeleton = [lst] * factorial(n)
	length = len(skeleton)

	for i in range(length):
		j = int(i/2)
		print(i, j)
		skeleton[i][j] = n

	return skeleton

print(factorial(n))
print(build(n))

########

# lst = list(range(1, n)) 		# [1. 2, 3 .. n]





