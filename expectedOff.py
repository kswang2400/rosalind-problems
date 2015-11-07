
AAAA = int(input("AA - AA: "))
AAAa = int(input("AA - Aa: "))
AAaa = int(input("AA - aa: "))
AaAa = int(input("Aa - Aa: "))
Aaaa = int(input("Aa = aa: "))
aaaa = int(input("aa - aa: "))

answer = 2 * (
	(AAAA + AAAa + AAaa) + 		
	(.75 * (AaAa)) + 			
	(.50 * Aaaa)				
	)

print(answer)
