
n = int(input("N: "))
n = list(range(1, n+1))         
permutations = []

def permute(remainder, output = []):
    if not remainder:
        permutations.append(tuple(output))
        output.pop()
        return

    new_remainder = list(remainder)
    for x in remainder:
        output.append(x)
        new_remainder.remove(x)
        permute(new_remainder, output)
        new_remainder = list(remainder)
    if output:
        output.pop()
    return permutations

permute(n)

for combo in permutations:
    output = ""
    for num in combo:
        output += str(num)
    print(" ".join(output))


