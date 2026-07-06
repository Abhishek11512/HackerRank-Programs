#Designer Door Mat
# Struggled a bit for top half, mid is simple, bottom is easy if you use reversed function

N, M = map(int, input().split())

for i in range(N//2):
    print ( (".|." * ((2*i)+1)).center(M, "-") )

print ("WELCOME".center(M, "-"))

for i in reversed(range(N // 2)):
    print((".|." * ((2 * i) + 1)).center(M, "-"))