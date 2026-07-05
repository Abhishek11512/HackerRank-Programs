#First prog that does things a bit differently

n = int(input().strip())
Nl = set(map(int, input().split()))
Num_Com = int(input().strip())

for i in range(Num_Com):
    com_line = input().split()
    com_name = com_line[0]
    ots = set(map(int, input().split()))
    if com_name=="update":
        Nl.update(ots)
    elif com_name=="intersection_update":
        Nl.intersection_update(ots)
    elif com_name=="difference_update":
        Nl.difference_update(ots)
    else:
        Nl.symmetric_difference_update(ots)
        
print(sum(Nl))
    
    
        