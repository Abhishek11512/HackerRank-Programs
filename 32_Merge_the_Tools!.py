#Merge The Tools

def merge_the_tools(string, k):
    l=len(string)
    for i in range(0,l,k):
        uc=string[i:i+k]
        subLis=[]
        for char in uc:
            if char not in subLis:
                subLis.append(char)
        print ("".join(subLis))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)