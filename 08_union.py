#Union function Prog!

E = int(input().strip())
ERoll = set(map(int, input().split()))
F = int(input().strip())
FRoll = set(map(int, input().split()))

UN = ERoll.union(FRoll)
N = len(UN)
print(N)