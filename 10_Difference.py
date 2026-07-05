#Set Difference Prog!


E = int(input().strip())
ER = set(map(int, input().split()))
F = int(input().strip())
FR = set(map(int, input().split()))

DF = ER.difference(FR)
N = len(DF)
print(N)