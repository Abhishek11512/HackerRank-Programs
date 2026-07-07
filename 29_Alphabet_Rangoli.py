#Alphabet_Rangoli

import string
def print_rangoli(size):
    alp_low = string.ascii_lowercase
    row = []
    wid = (size * 4) - 3
    for i in range(size):
         si = None if (i == size - 1) else (size - 1 - (i + 1))
         uc = list(alp_low[size - 1 : si : -1])
         stp = "-".join(uc + uc[-2::-1])
         row.append(stp.center(wid,"-"))
    print("\n".join(row + list(reversed(row[:-1]))))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

    #needed Help for this one too sad to say but yeah