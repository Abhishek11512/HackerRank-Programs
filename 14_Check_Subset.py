#Check Subset
Cases = int(input().strip())
for i in range(Cases):
    A = int(input().strip())
    SetA = set(map(int, input().split()))
    B = int(input().strip())
    SetB = set(map(int, input().split()))
    print(SetA <= SetB)