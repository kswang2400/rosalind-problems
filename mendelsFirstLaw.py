
k = float(input("What is k? "))
m = float(input("What is m? "))
n = float(input("What is n? "))

t1 = float(k + m + n)
t2 = float(k + m + n - 1)

aa = (n / t1) * ((n - 1)/ t2)				# aa x aa
mix = (m / t1) * (n / t2)					# Aa x aa
Aa = (m / t1) * ((m -1) / t2) * (0.25)		# Aa x Aa

recessive = aa + mix + Aa

domPhen = 1 - recessive

# print(t1, t2)
# print(aa)
# print(mix)
# print(Aa)
# print(recessive)
print(domPhen)