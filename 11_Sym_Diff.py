# Symmetric Difference

E = int(input().strip())
ER = set(map(int, input().split()))
F = int(input().strip())
FR = set(map(int, input().split()))

DF = ER ^ FR
N = len(DF)
print(N)