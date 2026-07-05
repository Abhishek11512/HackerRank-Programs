#Captains_Room Prog
K = int(input().strip())
rooms = list(map(int, input().split()))

SoL= sum(rooms)
SoS = sum(set(rooms)) * K
Diff = SoS - SoL
CapRoom = Diff//(K-1)
print(CapRoom)

