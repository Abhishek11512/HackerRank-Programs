#Strict Superset

A = set(map(int, input().split()))
nos = int(input().strip())
is_strict_superset = True

for i in range(nos):
    SetN= set(map(int, input().split()))
    if not (A > SetN):
        is_strict_superset = False
        
print(is_strict_superset)
