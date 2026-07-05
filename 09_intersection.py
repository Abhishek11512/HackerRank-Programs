# Intersection Prog

E = int(input().strip())
ER = set(map(int, input().split()))
F = int(input().strip())
FR = set(map(int, input().split()))

IS = ER.intersection(FR)
N = len(IS)
print(N)